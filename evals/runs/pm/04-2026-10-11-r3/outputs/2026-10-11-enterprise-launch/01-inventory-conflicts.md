DRAFT, not reviewed by a person

# 01 · Requirements, conflicts, and timeline

All four source documents are SYNTHETIC (so labelled by the user).

## Requirements extracted (one line each, with source)

| Item | Priority in PRD | Eng estimate | Source |
|---|---|---|---|
| SSO with SAML | Must have | 3 weeks | Doc 1 PRD; Doc 3 eng |
| Audit log | Must have | 2 weeks | Doc 1 PRD; Doc 3 eng |
| Admin roles | Must have | 1 week | Doc 1 PRD; Doc 3 eng |
| Usage dashboard | Nice to have | 2 weeks | Doc 1 PRD; Doc 3 eng |

## Conflict (this one decides the plan)

| | PRD v2 (Doc 1, product) | Sales call notes (Doc 2, sales) |
|---|---|---|
| SSO with SAML | "Must have: SSO with SAML for the pilot customer" | "Their IT lead said Google login is fine for the pilot; SAML SSO 'can wait until we roll out to the whole company next year'" |
| Audit log | Listed as a must-have, no urgency stated | "They care most about the audit log, because their compliance review starts in December" |

The PRD treats SAML as required for the pilot. The customer (via sales) says SAML is not needed for the pilot and can wait until next year's company-wide rollout, and that the audit log is their real priority. Both cannot be top priority under a fixed date and fixed capacity. **This is the call the human must make** (PM.md section 10, hard-to-reverse scope decision).

## Timeline math (verified with python3, see run notes)

- Engineers start: **Tuesday 2026-10-20**. Launch target: **Sunday 2026-11-15** (note: a Sunday).
- Runway: 27 calendar days inclusive = **3.71 calendar weeks**; 19 business days = **3.8 work-weeks**.
- Capacity: 2 engineers × 3.71 calendar weeks ≈ **7.4 engineer-weeks**.
- Work (treating each estimate as one engineer's weeks):
  - Three must-haves = 3 + 2 + 1 = **6 engineer-weeks**
  - All four items = 6 + 2 = **8 engineer-weeks** (exceeds the ~7.4 capacity → the full scope does not fit).

## Assumptions behind the math
- Each estimate is one engineer's effort (engineer-weeks), so two items can run in parallel on two engineers. Confirm with engineering. [ASSUMPTION]
- Estimates carry no built-in buffer; they are taken at face value. [ASSUMPTION]
- Work can start 20 October and the date is 15 November as stated. [from Doc 3, Doc 1]
