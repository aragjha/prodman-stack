# 05 · Ranked plan — what to build first

**Decision this serves:** the Q4 recurring-invoices plan for the CEO, whose stated goal is Q4 **seat
expansion**. Effort figures are Kwame's (#06); confidence is on the demand evidence.

## The build is already scoped and underway
Squad B (4 eng) started Mon 21 Sep on PRD v2 scope; 10 weeks → GA Mon 30 Nov (#06, #01). So "what to
build first" is really: the critical path inside the launch, plus what to add or cut around it.

## Ranked

| Rank | Build | Why / evidence | Effort (Squad B) | Confidence |
|---|---|---|---|---|
| 1 | **Series engine — create, schedule, send (R1)** | The foundation; everything (list, pause, preview, and later reminders + autopay) depends on it. Core need, 5 independent sources. | 3 wks | HIGH |
| 2 | **The agreed launch musts: 60-day list (R3), pause/resume (R4), preview email (R5), edit-future-only (R6)** | All Must in PRD v2, all confirmed in design review + interview; no disagreement. | 1 + 0.5 + 1 + 1.5 = 4 wks | HIGH |
| 3 | **Payment reminders** *(currently out of scope — recommend reopening)* | Strongest demand in the whole file (theme #1, 6 sources); tied to 2 of 3 recent churns and 2 lost deals; "table stakes" vs Falcon. Cheap: 2 wks, reuses the scheduler — but must follow R1. **Blocked by CEO's call (C3) and the 18%/43% number (C2).** | 2 wks (after engine) | HIGH demand / blocked |
| 4 | **Custom recurrence rules (R7)** *(in scope — recommend cutting from launch)* | Should, not Must. No customer asked; interview says everyone bills on the 1st; design tested badly. Costs 2 of the 10 weeks. Cutting it buys back the biggest single chunk of schedule for C1. | 2 wks | ZERO customer evidence |
| 5 | **Multi-currency EUR** *(out of scope — decision needed)* | One 40-seat deal wants it at launch; sales committed it verbally against the PRD. Adds 2 wks → worsens the date. | 2 wks | WEAK (single deal) |
| 6 | **Autopay** *(settled: phase 2 / Q1 2027)* | Needs an outside security review (3–4 wk lead) that can't finish this quarter. Correctly deferred. | 5 wks + review | n/a this quarter |

## Recommendation (for the user's judgment, not a decision taken)
1. **Build first:** R1 engine, then the four agreed musts (R3–R6). That is the defensible launch core.
2. **Cut R7 from launch** unless a customer asks — it has no demand and costs 2 weeks you need for the date.
3. **Reopen reminders with leadership** once C2 (18% vs 43%) is settled — it is 2 weeks, reuses the
   engine, and is the one thing the market is punishing you for not having.
4. **Do not promise 31 October.** The build plan says 30 November; even cutting R7 lands ~mid-November.

## Success metric (from PRD v2, carry into the plan)
30% of active firms have ≥1 live series 60 days after launch. Baseline 0 (new feature). No guardrail
metric is defined in any document — **propose one** (e.g. invoice-send error rate / bounced-email rate,
given bounced-email handling is "not designed yet", #06).
