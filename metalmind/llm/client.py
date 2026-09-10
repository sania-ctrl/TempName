import json

from ..config import settings


class LLMClient:
    """Thin wrapper around the OpenAI chat completions API.

    Tracks cumulative token usage so pipelines/eval can report the token-efficiency
    numbers the paper measures (Table 1).
    """

    def __init__(self, model: str = None, api_key: str = None):
        from openai import OpenAI

        self._client = OpenAI(api_key=api_key or settings.openai_api_key)
        self.model = model or settings.openai_model
        self.total_tokens = 0

    def complete_json(self, system: str, user: str) -> dict:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
            temperature=0,
        )
        self._track_usage(response)
        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except (TypeError, json.JSONDecodeError):
            return {}

    def complete_text(self, system: str, user: str) -> tuple:
        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            temperature=0,
        )
        tokens = self._track_usage(response)
        return response.choices[0].message.content, tokens

    def complete_vision(self, system: str, user_text: str, image_data_urls: list) -> tuple:
        """Like `complete_text`, but attaches one or more images (as data: URLs) to the user
        turn. Used for describing video frames -- requires a vision-capable model (GPT-4o
        qualifies; set OPENAI_MODEL accordingly if you swap models)."""
        content = [{"type": "text", "text": user_text}]
        content.extend({"type": "image_url", "image_url": {"url": url}} for url in image_data_urls)

        response = self._client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": content},
            ],
            temperature=0,
        )
        tokens = self._track_usage(response)
        return response.choices[0].message.content, tokens

    def _track_usage(self, response) -> int:
        usage = getattr(response, "usage", None)
        tokens = usage.total_tokens if usage else 0
        self.total_tokens += tokens
        return tokens
