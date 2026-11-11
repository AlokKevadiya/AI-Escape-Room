"""Small Gemini adapter; no keys or raw API exception messages are logged."""
import os


class ModelUnavailable(RuntimeError):
    pass


def generate(system, contents, schema=None):
    from google import genai
    from google.genai import types

    key = os.getenv("GEMINI_API_KEY", "").strip()
    model = os.getenv("GEMINI_MODEL", "").strip()
    if not key or not model:
        raise ModelUnavailable("Set GEMINI_API_KEY and GEMINI_MODEL in your local .env.")
    config = {"system_instruction": system, "temperature": 0.2,
              "max_output_tokens": 2048}
    if schema:
        config.update(response_mime_type="application/json", response_schema=schema)
    try:
        with genai.Client(api_key=key, http_options=types.HttpOptions(timeout=20000)) as client:
            response = client.models.generate_content(
                model=model, contents=contents,
                config=types.GenerateContentConfig(**config))
        if not response.text:
            raise ValueError("Empty model response")
        return response.text
    except Exception:
        raise ModelUnavailable(
            "The model is unavailable. Check your key, model and free-tier quota. "
            "No action was applied; you can retry or use V2 offline practice."
        ) from None
