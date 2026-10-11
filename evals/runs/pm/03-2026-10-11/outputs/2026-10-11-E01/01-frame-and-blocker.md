# E01 · Why did activation drop in September — frame & blocker

Run date: 2026-10-11 · Route: E01 (Product analytics to decisions) · Skill: pm

## Decision this serves
- **Decision:** what to do about the September activation drop — fix it now, investigate further, or accept it.
- **Decider and date:** the user's VP, by Thursday 2026-10-16.
- **Done looks like:** a one-page decision brief — candidate causes ranked by evidence + confidence, definitional/seasonal effects ruled out, one cheap test with a primary + guardrail metric.
- **Inputs in hand:** none yet.

## Prerequisites (E01 "You need") vs. what we have
| Needed | Have it? | If missing, it blocks |
|---|---|---|
| Metrics as a table/export (weekly or daily) | No — no Amplitude connector, no export provided | The entire "what happened / when it started" step |
| Event & metric definitions (what "activation" counts) | No | Step 2 — a definition change can masquerade as a trend |
| Release log / list of changes in the period | No | Step 4 — lining the drop up against causes |
| context/PRODUCT.md | No (only templates present) | Segment, baseline, stakeholders |

## Blocker
No Amplitude connector exists in this environment. Per PM.md (unknown is valid, invented is not) and E01
("without an analytics connector it works only from what you export"), no activation numbers or causes are
produced until real data is supplied. Nothing in this file is fabricated.

## Smallest unblock
A CSV/table export from Amplitude of the activation metric by week (ideally by day for Sept), Jul–Sep 2026,
plus the activation event definition and the Q3 release/change log. See handback for the exact export spec.
