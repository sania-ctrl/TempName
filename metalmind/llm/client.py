import json
import re
import time

from ..config import settings

_MAX_RETRIES = 8
_BASE_DELAY_SECONDS = 2.0


class LLMClient:
    """Thin wrapper around the OpenAI chat completions API.

    Tracks cumulative token usage so pipelines/eval can report the token-efficiency
    numbers the paper measures (Table 1). Retries on rate limits and transient API errors
    rather than letting a 429 crash a long multi-hundred-call build partway through.
    """

    def __init__(self, model: str = None, api_key: str = None):
        from openai import OpenAI

        self._client = OpenAI(api_key=api_key or settings.openai_api_key)
        self.model = model or settings.openai_model
        self.total_tokens = 0

    def complete_json(self, system: str, user: str) -> dict:
        response = self._request_with_retry(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
        )
        self._track_usage(response)
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except (TypeError, json.JSONDecodeError):
            return {}

    def complete_text(self, system: str, user: str) -> tuple:
        response = self._request_with_retry(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ]
        )
        tokens = self._track_usage(response)
        return response.choices[0].message.content, tokens

    def complete_vision(self, system: str, user_text: str, image_data_urls: list) -> tuple:
        """Like `complete_text`, but attaches one or more images (as data: URLs) to the user
        turn. Used for describing video frames -- requires a vision-capable model (GPT-4o
        qualifies; set OPENAI_MODEL accordingly if you swap models)."""
        content = [{"type": "text", "text": user_text}]
        content.extend({"type": "image_url", "image_url": {"url": url}} for url in image_data_urls)

        response = self._request_with_retry(
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": content},
            ]
        )
        tokens = self._track_usage(response)
        return response.choices[0].message.content, tokens

    def _request_with_retry(self, **kwargs):
        from openai import APIError, RateLimitError

        last_error = None
        for attempt in range(_MAX_RETRIES):
            try:
                return self._client.chat.completions.create(model=self.model, temperature=0, **kwargs)
            except RateLimitError as error:
                last_error = error
                delay = _retry_delay_seconds(error, attempt)
                print(f"  [rate limited, attempt {attempt + 1}/{_MAX_RETRIES}, waiting {delay:.1f}s]")
                time.sleep(delay)
            except APIError as error:
                # Transient server-side errors (5xx, dropped connections) -- worth a few retries too.
                last_error = error
                if attempt == _MAX_RETRIES - 1:
                    raise
                delay = _BASE_DELAY_SECONDS * (2**attempt)
                print(f"  [API error, attempt {attempt + 1}/{_MAX_RETRIES}, retrying in {delay:.1f}s: {error}]")
                time.sleep(delay)
        raise last_error

    def _track_usage(self, response) -> int:
        usage = getattr(response, "usage", None)
        tokens = usage.total_tokens if usage else 0
        self.total_tokens += tokens
        return tokens


def _retry_delay_seconds(error, attempt: int) -> float:
    """Prefer the server's own suggested wait time (its message includes e.g. "Please try
    again in 1.488s") over blind exponential backoff, since token-per-minute limits reset on
    a per-second cadence and the suggested wait is usually far shorter than 2**attempt."""
    match = re.search(r"try again in ([\d.]+)s", str(error))
    if match:
        return float(match.group(1)) + 0.5  # small buffer
    return _BASE_DELAY_SECONDS * (2**attempt)
