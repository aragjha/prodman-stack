# 01 · Document inventory, requirements, and conflicts (A01)

All inputs are SYNTHETIC (written for this test).

## Document inventory
| # | Document | Author role | Date | Says, in short | Supersedes? |
|---|---|---|---|---|---|
| 1 | PRD v2 | Product | not dated ("v2") | Scope + target date | — |
| 2 | Sales call notes | Sales | not dated | What the pilot customer actually wants | — |
| 3 | Engineering estimate | Engineering | not dated | Effort per item + staffing | — |
| 4 | CEO message | Leadership | not dated | The date is fixed | — |

No document is dated, so none can be marked as superseding another. The documents are from four different functions describing the *same* launch, not successive versions — they must be reconciled, not ranked by recency.

## Requirements and claims, each traced to its document
| Item | Claim | Source |
|---|---|---|
| SSO with SAML | "Must have" for the pilot | Doc 1 PRD |
| SSO with SAML | "Google login is fine for the pilot"; SAML SSO "can wait until we roll out to the whole company next year" | Doc 2 Sales |
| SSO with SAML | 3 weeks | Doc 3 Eng |
| Audit log | "Must have" | Doc 1 PRD |
| Audit log | Customer "care most about the audit log, because their compliance review starts in December" | Doc 2 Sales |
| Audit log | 2 weeks | Doc 3 Eng |
| Admin roles | "Must have" | Doc 1 PRD |
| Admin roles | 1 week | Doc 3 Eng |
| Usage dashboard | "Nice to have" | Doc 1 PRD |
| Usage dashboard | 2 weeks | Doc 3 Eng |
| Date | "Target launch: 15 November" | Doc 1 PRD |
| Date | "We launch the pilot on 15 November no matter what. Do not slip the date." | Doc 4 CEO |
| Staffing | "Two engineers available from 20 October" | Doc 3 Eng |

## The conflict that decides the plan
**SSO with SAML — must-have vs can-wait.**

| Side | Source | Exact words |
|---|---|---|
| Must build now | Doc 1 PRD (Product) | SSO with SAML listed under "Must have: ... for the pilot customer" |
| Can wait | Doc 2 Sales (the customer's own IT lead) | "Google login is fine for the pilot"; SAML SSO "can wait until we roll out to the whole company next year" |

This conflict is not resolved here — it is put first in the "Needs your judgment" list and the plan is shown both ways in file 02.

**Not a conflict (worth stating):** The CEO (Doc 4) fixes the *date*, not the *scope*. "Do not slip the date" and "15 November no matter what" are about timing; the CEO names no feature. So cutting scope to protect the date is consistent with the CEO message, not in tension with it. The only scope conflict is PRD vs sales.

## Capacity (recomputed; see calc.py)
- Engineers available from **20 Oct 2026 (a Tuesday)**; target launch **15 Nov 2026 (a Sunday)**.
- Window: **26 calendar days = 3.71 weeks**; **19 working days = ~3.8 working-weeks per engineer**.
- Two engineers → **~7.6 engineer-weeks gross**, before any time for integration, QA, and launch prep. Usable dev capacity is lower — call it **~6 engineer-weeks** once you hold back roughly the last week for testing (last working day before launch is Fri 13 Nov).
- Total of all four estimates = **3 + 2 + 1 + 2 = 8 engineer-weeks.**

**8 weeks of work > ~6–7.6 engineer-weeks of capacity → everything cannot ship. Something must be cut regardless of the conflict.** Two flags: 20 Oct is a Tuesday (not a full Monday-start week), and 15 Nov is a Sunday — confirm whether "launch" means a weekend go-live or the business day around it.
