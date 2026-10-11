# 04 · Self-check (quality, not publication)

> Run A01 · 2026-10-11 · Graded by the producing session — a separate reviewer is still required before
> this is treated as final (PM.md §7).

## Rubric (PM.md §7), 1–5

| Criterion | Score | Evidence line |
|---|---|---|
| Clarity | 5 | "The call (one line)" states the cut and the reason in one sentence. |
| Visual | 5 | Scenario table (02) shows 40 needed vs 38 available; plan table (03) shows cut in one glance. |
| Concise | 4 | Plan is one page; capacity file is longer but is the backing, not the artifact. |
| Decision | 5 | Makes the call (cut SSO) and lists "What would reverse this call". |
| Honesty | 5 | Google-login dependency flagged as the key assumption; confidence tagged per item; synthetic labelled. |

## Accuracy (pass/fail per claim)

| Claim | Traces to | Pass? |
|---|---|---|
| SSO/audit/roles must-have, dashboard nice-to-have, launch 15 Nov | Doc 1 (quoted) | PASS |
| "Google login is fine for the pilot"; SAML "can wait until… next year" | Doc 2 (quoted) | PASS |
| "They care most about the audit log… compliance review starts in December" | Doc 2 (quoted) | PASS |
| SSO 3w / audit 2w / roles 1w / dashboard 2w; two engineers from 20 Oct | Doc 3 (quoted) | PASS |
| "launch… 15 November no matter what. Do not slip the date." | Doc 4 (quoted) | PASS |
| 38 engineer-days available; 40 needed; 15 Nov is a Sunday | Calculation, labelled inference | PASS (math shown) |

## Artifact-specific checks (A01)
- Every requirement cites the file it came from — **pass** (table in 02).
- Every contradiction shows both sources, not silently resolved — **pass** (Conflicts 1 & 2 in 02).
- Superseded documents not used as current — **pass** (none superseded; stated in 01).
- No requirement/date/number appears that is not in the documents, except calculations marked as
  inference — **pass**.
- Ranking states the decision it serves — **pass** (header of 03).

## Flags
- Baseline for the success metric is unknown and is marked unknown, not invented (PM.md §6).
- The dashboard "fits" conclusion depends on the Google-login assumption; if that breaks, re-grade.
