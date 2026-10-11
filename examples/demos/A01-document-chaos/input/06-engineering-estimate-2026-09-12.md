SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# Engineering estimate: recurring invoices, PRD v2 scope
From: Kwame (eng lead)
Date: 12 September 2026
Team: Squad B, 4 engineers. Start: Monday 21 September.

## In scope
| Item | PRD ref | Weeks for Squad B |
|---|---|---|
| Series engine: create, schedule, send | R1 | 3 |
| Upcoming invoices list, 60 days | R3 | 1 |
| Pause and resume | R4 | 0.5 |
| Preview email | R5 | 1 |
| Edit future invoices only | R6 | 1.5 |
| Custom recurrence rules | R7 | 2 |
| QA and release hardening | | 1 |
| Total | | 10 |

10 weeks from 21 September puts general availability on Monday 30 November.

## Not in scope, estimated on request
| Item | Weeks | Note |
|---|---|---|
| Autopay | 5 | plus an outside security review with 3 to 4 weeks lead time |
| Multi currency series | 2 | |
| Automatic payment reminders | 2 | reuses the series scheduler, so it can only start after the engine is done |

## Risks
- No buffer for holidays or sickness.
- Bounced email handling is not designed yet.
