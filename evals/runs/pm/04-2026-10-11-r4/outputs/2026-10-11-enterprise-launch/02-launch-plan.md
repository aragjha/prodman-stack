DRAFT, not reviewed by a person

# Enterprise pilot launch plan — fit to the team and the date (C04)

All figures trace to the four synthetic documents in the request.

## 1. Usable capacity (working shown)
- Two engineers available from 20 October (Doc 3). Target launch 15 November (Doc 1, Doc 4).
- 20 October 2026 is a Tuesday; 15 November 2026 is a Sunday, so the last working day before launch is Friday 13 November.
- Working days, Tue 20 Oct through Fri 13 Nov inclusive: **19 days = 3.8 weeks** per engineer.
- Two engineers × 3.8 weeks = **7.6 engineer-weeks nominal**, before any time off, support duty, integration or testing (none of which were given — see assumptions).

## 2. The scope and its estimates (Doc 3; must/nice tags from Doc 1)

| Item | Estimate | PRD tag | Customer signal (Doc 2) |
|---|---|---|---|
| SSO with SAML | 3 weeks | Must have | IT lead: can wait until next year's company-wide rollout |
| Audit log | 2 weeks | Must have | Cares most about this; compliance review starts December |
| Admin roles | 1 week | Must have | not mentioned |
| Usage dashboard | 2 weeks | Nice to have | not mentioned |
| **Total** | **8 weeks** | | |

Everything in the PRD plus the nice-to-have is 8 engineer-weeks. The three PRD must-haves alone are 6 engineer-weeks, which fits 7.6 only with near-zero margin — the opposite of what "do not slip the date" needs.

## 3. Recommended committed plan (assumes the decider approves deferring SAML SSO — see 01-conflict-brief.md)

| Item | Estimate | Why it stays |
|---|---|---|
| Audit log | 2 weeks | The customer's stated top priority; needed before their December compliance review |
| Admin roles | 1 week | PRD must-have, cheapest item |
| **Committed total** | **3 engineer-weeks** | Leaves ~4.6 engineer-weeks of margin against the fixed date |

**Sequencing (both engineers from 20 Oct):**
- Engineer A: audit log first (2 weeks), finishing in early November with time to harden it before the December compliance review.
- Engineer B: admin roles (1 week), then wire up / verify Google login for the pilot customer and support audit-log testing.
- Final week before 13 Nov: integration, pilot-readiness testing, and sign-off with the pilot customer.

## 4. What to cut, and why (your answer to "what to cut to hit the date")

| Cut / defer | Estimate freed | Reason |
|---|---|---|
| **SAML SSO** → defer to next year's company-wide rollout; run the pilot on Google login | 3 weeks | The customer's IT lead says it can wait; it is the single biggest time sink; deferring it is what makes the date safe. Needs the decider to approve amending PRD v2. |
| **Usage dashboard** → drop from the pilot, revisit after launch | 2 weeks | PRD lists it as nice to have only; no customer asked for it for the pilot. |

**Stretch (only if audit log and admin roles land early and the margin holds):** usage dashboard.

## 5. Success measure
- **Primary metric:** unknown — no pilot success metric was given. Proposed: the pilot customer passes its December compliance review using the audit log. Baseline: unknown (first pilot). Cheapest way to get it: agree the pass/fail criterion with the customer's compliance owner before launch.
- **Guardrail:** no pilot-blocking regression in sign-in (Google login) or admin access.

## 6. Risks and assumptions
- **Estimates are engineering's own point estimates (Doc 3), un-buffered.** If the audit log slips, it threatens the customer's December compliance review before it threatens the 15 Nov date.
- **ASSUMPTION — Google login is already production-ready for the pilot customer.** The notes say it is fine for the pilot but do not confirm it is built. Test: ask engineering this week. Cost if wrong: Google login becomes new build work and eats the margin.
- **ASSUMPTION — both engineers are full-time on this, with no time off or support duty.** None was stated. Test: check the team calendar. Cost if wrong: the 7.6 engineer-week figure drops.
- **ASSUMPTION — nobody besides the customer's IT lead requires SAML for this pilot.** Test: the decider confirms when approving the cut.
- **Date note:** 15 November is a Sunday; the real cutover is likely the preceding week. Confirm the intended go-live working day.
