# Enterprise pilot launch plan — ship 15 November

> DRAFT · Run A01 · 2026-10-11 · **SYNTHETIC inputs — labelled synthetic on every page.**
> Decision this serves: what to cut so the pilot ships 15 November without slipping.

## The call (one line)
**Cut SAML SSO from the pilot; ship audit log + admin roles on Google login; treat the usage dashboard
as a stretch item.** This is the only scope that fits two engineers in the available window, and it cuts
the one thing the pilot customer said they don't need yet.

## Why cut SSO
- The pilot customer's own IT lead said **"Google login is fine for the pilot"** and that SAML SSO
  **"can wait until we roll out to the whole company next year"** (Doc 2). We'd be building a 3-week
  feature the user asked us not to prioritise.
- It is the **biggest item (15 of 40 engineer-days)**. Removing it is what makes the date reachable —
  full scope needs 40 engineer-days against 38 available (see `02-...-capacity.md`).
- It is not lost — it moves to the company-wide rollout next year, which is the customer's own timeline.

## What ships (the plan)

| Priority | Item | Effort | Why it stays | Confidence |
|---|---|---|---|---|
| 1 | **Audit log** | 2 wks | Customer's #1; their compliance review starts in December (Doc 2). PRD must-have. | HIGH |
| 2 | **Admin roles** | 1 wk | PRD must-have; cheap (1 wk); expected in any enterprise pilot. | HIGH |
| 3 | **Usage dashboard** *(stretch)* | 2 wks | Nice-to-have only (Doc 1). Fits the math, but it is the first thing to drop if anything slips. | HIGH |
| — | ~~SAML SSO~~ **CUT → next-year rollout** | ~~3 wks~~ | Customer said Google login is fine for the pilot (Doc 2). | HIGH |

**Committed must-ship = audit log + admin roles (3 engineer-weeks).** With 7.6 engineer-weeks of
capacity, this lands with large buffer, leaving room for QA and to harden the audit log before the
December compliance review. The dashboard is built only if audit log and Google login land on schedule.

## Suggested sequence (two engineers from 20 Oct)
- **Eng A:** Audit log (wks 1–2), then harden/test it for the Dec compliance review.
- **Eng B:** Admin roles (wk 1), confirm Google login works end-to-end for the pilot tenant (wk 1–2),
  then start the usage dashboard only if the above is clean.
- Leave the final week (9–13 Nov) for integration, QA, and a dry run before the Sunday 15 Nov launch.

## How we'll know it worked
- **Primary:** pilot customer passes its December compliance review using the audit log. *(Baseline:
  unknown — no prior review result in the docs.)*
- **Guardrail:** launch date holds at 15 November (the CEO's fixed constraint, Doc 4).
- **Leading signal (this sprint):** audit log feature-complete and in QA by ~6 November, giving a week
  of slack before the Friday 13 Nov cutoff.

## What would reverse this call
- Google login turns out **not** to be built → auth becomes unestimated work; re-plan immediately.
- The customer's compliance review needs **SAML specifically** (not just an audit log) → SSO re-enters
  scope and the date is at genuine risk; escalate to the CEO, since date and scope then collide.

## Needs your judgment
1. **Confirm the SSO cut.** The PRD calls SAML SSO a pilot must-have; the customer says it can wait. The
   evidence favours cutting, but this reverses a written PRD requirement — your call to make with the
   product owner.
2. **Confirm Google login already exists** and needs no build. The whole plan rests on this.
3. **Dashboard: in or out?** It fits the math as a stretch, but is the natural drop if anything slips.
