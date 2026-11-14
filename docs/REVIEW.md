# Repository review — 14 November 2026

Reviewed main at 6eb51bd77fb1b3dc72d2216b4a651d0b050497a9 before this evidence update.

## Checks completed

- Inspected the complete 32-file tree, all 31 text files and extracted text from
  the matching three-page PDF report. The PDF blob matched its GitHub SHA.
- Ran all 49 tests against the retrieved current source: passed locally.
- Latest three inspected GitHub Actions runs succeeded. Latest reviewed run:
  https://github.com/AlokKevadiya/AI-Escape-Room/actions/runs/43273108573
- Confirmed main, version-1 and version-2 branches and 21 commits before this update.
  Version branches are historical milestones; the current app exposes both versions.
- .env is excluded and absent from the current tree. .env.example contains blank
  API-key fields. No common Google, GitHub, Groq token or private-key patterns were
  found in the current text files. This is not an exhaustive historical secret audit.
- Source implements five fixtures, three puzzles, session state, confirmation,
  inventory prerequisites, deterministic V2 validation and a clear escape outcome.
- Both architecture diagrams, installation instructions, more than five documented
  test cases, meaningful commit history and a design report are present.

## New evidence

The user-provided v2-online-success.json records Gemini / gemini-3.6-flash, eight
user actions, three solved puzzles, key and note collected, and escaped=true.
Replaying its commands through the deterministic engine reproduced every final
state field. The screenshot shows the online toggle enabled and successful escape.
No credentials or unrelated personal content were found in the JSON.

Original uploaded JSON SHA256:
03528dfdaeda59a95a75755a7daac56da9d993cb21c6dfd8829cd830eb2cd46a

Evidence limitations: one happy-path run, no timestamps/request IDs or raw parser
proposals in the export, and no live adversarial comparison yet. A replay proves
state consistency, not independent verification of remote API traffic.

## Remaining submission work

1. Run at least five online challenge cases in both V1 and V2, preserving actual
   outcomes including correct V1 refusals. Offline rejection evidence is separate.
2. Demonstrate V1's normal online gameplay and capture its screenshots/transcript.
3. Refresh Project_Report.pdf after comparison testing. Its 11 November statements
   about no key, no screenshots, no publication and 40 tests are historical, not
   current. README and this review explicitly identify it as the initial report.
4. Give the instructor access: the repository is currently private.
5. Review and understand the code and personalize the report before submission.

## Known limits from code review

- V2 can propose a legal but unintended action; confirmation is still necessary.
- Repeating use-key or answer-time after solving the desk can repeat an old riddle
  or note-reveal message even though state stays solved. This is a remaining
  narration-consistency edge case, not evidence of state corruption.
- V1 trusts an LLM escape marker; this is the baseline limitation to evaluate.
- Provider failures remain possible. The Interactions and Groq alternatives have
  local mocked tests but no successful live evidence here.
- Session state is lost on restart. Exports do not restore saved games.

Verdict: V2 online happy path is evidenced and automated checks pass. The repository
is suitable for continued testing, but is not yet a fully evidenced final submission.
