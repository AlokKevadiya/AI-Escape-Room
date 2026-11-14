# Observed online comparison — 14 November 2026

Both sessions used Gemini gemini-3.6-flash. Each version received the two inputs
in order in a fresh session. These are single observations, not repeated trials.

| Input | V1 observed response | V2 observed response |
|---|---|---|
| use key on desk | Refused: player has no key; desk remains locked. | Rejected: item must be collected before use. |
| enter 0000 on drawer | Refused: code incorrect; drawer remains locked. | Rejected: incorrect code; lock unchanged. |

Sources: [V1 transcript](v1-online-validation-tests.json) and
[V2 transcript](v2-online-validation-tests.json).

**Both versions correctly refused both attempts. No V1 failure was observed in
these two cases.** These results do not demonstrate an empirical improvement in
refusal rate. The improvement is architectural: V1 relies on generated statements;
V2 has independent Python inventory, code and prerequisite checks. V1 exports
state=null by design; V2 exports explicit unchanged structured state. The V2 second
response also preserved the factual outcome despite unavailable AI atmosphere.

The V1 completed-game screenshot shared by the user shows online Gemini 3.6,
the final puzzle interactions and the escape banner. The full V1 success transcript
was not downloaded before restart; it must not be reconstructed or represented as
captured evidence. The V2 success transcript was preserved separately.

Five offline rejection cases and automated tests provide additional engine
coverage; they are not five live V1/V2 comparisons. Broader adversarial robustness
and relative model reliability remain unmeasured. Earlier checklist/report claims
that all V1 live observations were pending are superseded by these observations.
