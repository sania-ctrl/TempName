"""OpenAI client wrapper local to ontology_kg -- deliberately not shared with metalmind, so
this project has no code dependency on the Renishaw/metalmind work. Only implements
`complete_json`, the only call ontology_kg's extraction pipeline needs (no vision/video support
here, unlike metalmind's client).
"""
import json

from .config import settings


class LLMClient:
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

    def _track_usage(self, response) -> int:
        usage = getattr(response, "usage", None)
        tokens = usage.total_tokens if usage else 0
        self.total_tokens += tokens
        return tokens
