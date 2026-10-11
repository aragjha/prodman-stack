DRAFT, not reviewed by a person

# 03 · Contradictions, side by side

Each row shows both sources, which is newer, and who has to decide. None is silently resolved. "Resolved by supersession" means a later document explicitly replaced an earlier one; the rest need a human.

## C1 · Launch date — the headline conflict (NEEDS LEADERSHIP)
| Side A | Side B |
|---|---|
| **31 October**, to all customers. CEO #10 (9 Sep): "I told the board that recurring invoices will be live for all customers by 31 October. The board is counting on it for the Q4 seat expansion story, so please plan to that date." | **30 November.** Engineering estimate #06 (12 Sep, 3 days *after* the CEO message): 10 weeks from Mon 21 Sep → "general availability on Monday 30 November." PRD v2 #02 (28 Aug): "late November". Roadmap #01 (16 Sep): "GA 30 November". |

- Newer: the estimate (#06) and roadmap (#01) are **both newer** than the CEO's board commitment (#10) and both say 30 Nov.
- The math: 21 Sep → 31 Oct is **40 days (~5.7 weeks)**; the full estimate is **10 weeks**. 31 Oct is a **Saturday**. Even dropping R7 (−2 weeks → 16 Nov, see C6) does not reach 31 Oct.
- 30 Nov is a **Monday** (as the estimate states).
- **Decider: Daniel / leadership.** The board was told a date that the latest engineering estimate does not support by ~4 weeks. This is the first thing to settle before the CEO meeting.

## C2 · Multi-currency (EUR) at launch — sales commitment vs spec (NEEDS LEADERSHIP + SALES)
| Side A | Side B |
|---|---|
| **Committed at launch.** Sales #03 (14 Aug): "I told them multi currency recurring invoices will be there at launch. They want that in writing before they sign." Slack #04 (3 Sep) Tom: "I told them yes on the 14 August call, I thought it was in." The 40-seat firm "only signs if EUR works on day one." | **Non-goal at launch.** PRD v2 #02 (28 Aug): non-goal is "Recurring invoices in any currency other than the firm's default currency." Maya #04: "PRD v2 has other currencies as a non goal for launch." |
- Newer: PRD v2 (28 Aug) and the Slack thread (3 Sep) both post-date the verbal commitment (14 Aug); the conflict is unresolved in Slack.
- Cost to add: Kwame #04 "about 2 weeks"; estimate #06 lists multi-currency series at 2 weeks.
- **Decider: leadership + sales.** Either honour the written commitment (and add ~2 weeks) or go back to the 40-seat prospect before they sign. A verbal promise is already outstanding.

## C3 · "How late are payments, really?" — contradictory numbers (NEEDS LEADERSHIP)
| Side A | Side B |
|---|---|
| Support #05 (22 Jul): "Per the July collections dashboard, **43% of invoices sent through Ledgerly are paid after their due date.**" | CEO #10 (9 Sep): "**Only 18% of our invoices are paid late,** so payment reminders are a nice to have, not a priority this quarter." |
- These describe the same thing (invoices paid late) with very different numbers (43% vs 18%). The CEO's strategic call to deprioritise reminders rests on the 18% figure.
- **Decider: leadership.** Reconcile the two figures before the reminders priority is settled (C4). If 43% is right, the premise for parking reminders is weak.

## C4 · Payment reminders — parked by leadership vs top signal in the evidence (NEEDS LEADERSHIP)
| Side A (deprioritise) | Side B (strong demand) |
|---|---|
| CEO #10 (9 Sep): reminders are "a nice to have, not a priority this quarter. Recurring billing is where the seat growth is." PRD v2 #02: non-goal, "not planned this year". Roadmap #01: parked. | Five independent sources say chasing is the top pain: support #05 (31 tickets, the #1 theme, up from 22 in Jun); interview #08 (chasing "came up first and took most of the call"); sales #03 (lost a 25-seat firm to Falcon over reminders); competitor #11 (lost 2 of 4 Falcon deals over reminders; reminders "table stakes"); Slack #04 (Owen: 2 of last 3 churned firms, "I hear it on every renewal call"). |
- Newer: the CEO message (9 Sep) is the newest single voice; the five demand sources span 22 Jul–3 Sep.
- Cost: reminders are 2 weeks and "reuses the series scheduler, so it can only start after the engine is done" (#06) — a natural fast-follow, not a competing build.
- **Decider: leadership.** This is a strategy call, not a documents call. The evidence base points one way and the CEO's stated priority the other; the two should meet before the Q4 plan is locked. Tie to C3 (the 18%/43% discrepancy).

## C5 · Autopay in launch — RESOLVED by supersession (confirm only)
| Earlier | Current |
|---|---|
| Kickoff #14 (9 Jul) Rosa: autopay "has to be in the first version." PRD v1 #09: R2 autopay = Must. | PRD v2 #02 (28 Aug): autopay out of launch → phase 2 (Q1 2027), needs a security review. Roadmap #01: Q1 2027. Estimate #06: 5 weeks + 3–4 week security-review lead time. |
- Resolved: v2 supersedes v1. Interview #08 also supports: "Most would never give us their card." No action unless leadership reopens it.

## C6 · Custom recurrence rules (R7) — in the spec vs questioned everywhere else (NEEDS YOUR DECISION)
| In scope | Questioned |
|---|---|
| PRD v1 & v2: R7 = Should (launch). | Design #12 (1 Sep): "not agreed", builder had 9 controls, "tested badly with 2 internal users". Kwame #04 (3 Sep): "does anyone actually need every second Tuesday? custom rules are the gnarliest part of the build." Interview #08: monthly + a few quarterly is all this firm needs. Estimate #06: **2 weeks** — the biggest optional item. |
- **Decider: you (PM).** Cutting R7 saves ~2 weeks (full scope 30 Nov → ~16 Nov) and removes the one launch item with evidence against it. Lowest-regret lever you control.

## C7 · Preview email timing — 24 hours vs 3 days (minor; NEEDS YOUR DECISION)
| PRD v2 | Design review |
|---|---|
| #02 R5: preview "24 hours before an invoice is sent". | #12 (1 Sep, newer): preview "3 days before send, so mistakes can be caught over a weekend." |
- Newer: design review. Low stakes, but the PRD and design spec disagree; pick one before build. Interview #08 supports wanting a look before send ("I'd still want to look at them before they go out").

## C8 · Pricing — RESOLVED by supersession (confirm only)
| Earlier (#07, 8 Jul) | Current (#15, 5 Sep) |
|---|---|
| Recurring invoices as a paid **add-on, $6/firm/month**; autopay 0.5%/transaction. "Do not quote." | Recurring invoices **included in every plan, no add-on**. New list price from 1 Oct: **$25/seat/mo annual, $29 monthly** (was $22/$26). Existing firms keep price to renewal. Proposals before 1 Oct can keep $22 if signed by 31 Oct. Autopay pricing TBD; "do not quote the 0.5%". |
- Resolved: #15 explicitly replaces #07. Roadmap #01 reflects "included in all plans". No action; the 8 Jul add-on model is dead.

## Date / fact checks (for your confidence)
- "Monday 21 September" (#06/#01 start) — **correct**, 21 Sep 2026 is a Monday.
- "Monday 30 November" (#06 GA) — **correct**, 30 Nov 2026 is a Monday.
- 10-week estimate sums correctly: 3+1+0.5+1+1.5+2+1 = **10**.
- CEO #10 "Grace sent the details on Saturday" — **consistent**: Grace's update #15 is dated 5 Sep 2026, a Saturday.
- 31 October 2026 is a **Saturday** (a weekend GA, if that date is held).
