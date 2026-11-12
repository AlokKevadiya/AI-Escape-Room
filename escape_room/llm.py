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
        transport = os.getenv("GEMINI_TRANSPORT", "generate_content").strip()
        if transport == "interactions":
            from escape_room.interactions import generate_interaction
            return generate_interaction(key, model, system, contents, schema)
        if transport != "generate_content":
            raise ModelUnavailable("GEMINI_TRANSPORT must be interactions or generate_content.")
        with genai.Client(api_key=key, http_options=types.HttpOptions(timeout=60000)) as client:
            response = client.models.generate_content(
                model=model, contents=contents,
                config=types.GenerateContentConfig(**config))
        if not response.text:
            raise ValueError("Empty model response")
        return response.text
    except ModelUnavailable:
        raise
    except Exception as error:
        code = getattr(error, "code", None) or getattr(error, "status_code", None)
        reason = {
            503: "Gemini is overloaded (503). Retry later or test another available model.",
            504: "Gemini timed out (504). Retry later or test another available model.",
            429: "Gemini quota/rate limit reached (429). Check your free-tier allowance.",
            400: "Gemini rejected the request (400). Check model and API compatibility.",
            403: "Gemini denied access (403). Check your key's project and permissions.",
            404: "Gemini model or endpoint was not found (404). Check configuration.",
        }.get(code, "Gemini request failed. Check connectivity, model and configuration.")
        raise ModelUnavailable(reason + " No result was applied by this request.") from None
