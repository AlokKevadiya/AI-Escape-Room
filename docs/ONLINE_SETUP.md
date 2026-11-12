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
