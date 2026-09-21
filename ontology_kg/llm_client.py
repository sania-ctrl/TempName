"""OpenAI client wrapper local to ontology_kg -- deliberately not shared with metalmind, so
this project has no code dependency on the Renishaw/metalmind work. Only implements
`complete_json`, the only call ontology_kg's extraction pipeline needs (no vision/video support
here, unlike metalmind's client).
"""
import json
import re
import time

from .config import settings

_MAX_RETRIES = 8
_BASE_DELAY_SECONDS = 2.0


class LLMClient:
    def __init__(self, model: str = None, api_key: str = None):
        from openai import OpenAI

        self._client = OpenAI(api_key=api_key or settings.openai_api_key)
        self.model = model or settings.openai_model
        self.total_tokens = 0

    def complete_json(self, system: str, user: str) -> dict:
        response = self._request_with_retry(system, user)
        self._track_usage(response)
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except (TypeError, json.JSONDecodeError):
            return {}

    def _request_with_retry(self, system: str, user: str):
        from openai import APIError, RateLimitError

        last_error = None
        for attempt in range(_MAX_RETRIES):
            try:
                return self._client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system},
                        {"role": "user", "content": user},
                    ],
                    response_format={"type": "json_object"},
                    temperature=0,
                )
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
