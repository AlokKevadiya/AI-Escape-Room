# Online connection troubleshooting

The original generateContent adapter remains the default. An optional Interactions
REST adapter now supports both V1 conversation history and V2 structured parsing.
It uses Google's official endpoint, store=false, and a 60-second timeout. It does
not switch providers, enable billing, retry indefinitely, or claim offline output
is AI-generated. Use a free-tier project as required by the assignment.

From the project root, with your existing private .env:

```sh
python check_online.py --model gemini-3.8-flash --transport interactions
```

This makes one actual V2 structured-parser request. Only a correct action saves
GEMINI_MODEL and GEMINI_TRANSPORT to .env. On failure, settings stay unchanged.
Use a model available to your project. A successful check is a connection smoke
test, not proof that the full game or V1 adversarial tests passed.

After SUCCESS, stop Streamlit with Ctrl+C and restart:

```sh
python -m streamlit run app.py --server.address 0.0.0.0 --server.port 8501
```

Enable Use Gemini and test both versions. Download session evidence separately
for each. Existing offline evidence must remain labelled offline.

To test the original route, pass --transport generate_content. HTTP 503 means
service overload; 504 means timeout; 429 requires checking the project's quota.
The Interactions route may also fail during service disruption. No live success
is claimed for this change until tested with the user's project credentials.

The adapter has mocked tests for schema transmission, history conversion,
response extraction, failed/empty responses, and credential-safe error messages.
All 45 project tests passed locally after the change.

References:
- https://ai.google.dev/gemini-api/docs/migrate-to-interactions
- https://ai.google.dev/gemini-api/docs/structured-output


## Alternative: Groq free plan

Repeated Gemini 503s were also observed with the Interactions route. The app now
supports Groq explicitly for V1 and V2. This is an alternative, not an automatic
fallback. Model responses and game messages are sent to the selected provider.

1. Create a free Groq account and API key at https://console.groq.com/keys.
2. Add GROQ_API_KEY to your private .env. Do not enable a paid plan.
3. Run:

```sh
python check_online.py --provider groq --model openai/gpt-oss-20b
```

Only a successful real V2 parser request saves LLM_PROVIDER=groq and GROQ_MODEL.
Restart Streamlit, then enable **Use online AI**. The sidebar and evidence export
identify the selected provider and model. Gemini settings remain available.

Groq uses JSON object mode with the schema included in the prompt. This guarantees
neither schema compliance nor correct action interpretation; the existing V2
validator, confirmation step and Python rule engine remain authoritative.
V1 still relies on the LLM and is intentionally not protected by that engine.
Both versions preserve conversation/session behavior. Each V2 confirmed action
still uses an additional constrained atmosphere request, so allow for rate limits.

Local verification: 49 tests passed, including provider routing, V1 role history,
JSON requests, truncated-output rejection and redacted errors. Groq live testing
is pending the user's key; no online success is claimed yet.

Current free-plan model/limits reference:
https://console.groq.com/docs/rate-limits
JSON mode reference:
https://console.groq.com/docs/structured-outputs
