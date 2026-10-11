# Q1 2027 roadmap — Ledgerly late-payment (DRAFT, for Maya + leadership)

*All Ledgerly numbers are SYNTHETIC demo data (idea.md). Effort is a rough model sizing, NOT a squad
estimate — idea.md says "Nobody has estimated it." Replace with squad estimates before commit.*

## The decision this serves
What to commit the two squads to in Q1 2027 (Jan 1 – Mar 31) so it ships by 31 Mar 2027 and drives
**expansion revenue: 300 net new seats**. See `02-REPORT.md` for the opportunity call.

## The goal, sized honestly
| | Value | Note |
|---|---|---|
| Target | 300 net new seats in Q1 2027 | from leadership (idea.md) |
| Last quarter's pace | +80 seats (1,760 end-Jun → 1,840 end-Sep 2026) | idea.md |
| Target vs pace | **3.75×** | 300 ÷ 80 |
| Seats needed per firm | **~1.0 each** across ~300 firms | 300 ÷ 300; or concentrate in firms that chase by hand |
| Revenue if hit | **$7,500 MRR / $90,000 ARR** | 300 × $25/seat/mo; annual billing |

**Read this first:** 3.75× the current pace almost certainly will not come from one feature. Product
makes firms *want* more seats; sales/packaging converts that into *booked* seats. This roadmap owns
the product half and flags the rest (see Needs your judgment).

## Capacity we actually have
| Squad | Engineers | Effective | Availability | Best fit |
|---|---|---|---|---|
| A | 5 | **3.5** (≈30% on bank-feed upkeep every quarter) | full quarter | portal (touches payments/bank domain) |
| B | 4 | 4 | **free from week 1 of January** | reminders (greenfield, ships fastest) |
| Design | 2 | shared | — | both |
| PM | 1 (Maya) | — | — | both |

## The bets, scored against the seat goal
Scale 1–5. Impact = effect on net-new seats. Confidence = strength of evidence. Effort = build size
(5 = largest). Inputs shown; "unknown" where unknown.

| # | Bet | Impact (why) | Confidence (why) | Effort (why) |
|---|---|---|---|---|
| 1 | **Reminders engine** (auto-chase overdue invoices on the firm's schedule, stop when paid) | **4** — carries the only evidence-backed seat mechanism: Q1 "I'd move our two new juniors onto Ledgerly instead of the spreadsheet" | **3** — demand HIGH, but the seat link is an assumption to test | **3** — scheduling, send-state, stop-on-paid, dedupe, deliverability setup |
| 2 | **Reminder controls + approval** (choose who gets chased, edit wording, exclude big clients, approve before send) | **3** — unlocks adoption by cautious firms; without it they won't turn it on | **4** — Q3 explicit ("control who gets chased and what it says") + deliverability risk (Leanpay) | **2** — settings, exclusion list, template editor, approval step |
| 3 | **Client payment portal MVP** (one link per client: see every invoice, pay) | **2** — serves the firm's *external clients*, not seats; indirect, retention-leaning | **2** — Q2 wants it, but seat link weak; table stakes | **4** — external auth, security review, payments, multi-invoice pay |
| 4 | **Card-payment activation** (turn card on for more firms; prerequisite for portal "pay") | **2** — enabler; today <50 of ~300 firms (16.7%) have card on | **2** — inferred from low attach, no demand data | **2** — onboarding flow via existing payments partner |

**Close call:** Bets 1 and 3 are the "two parts that might be one product" from idea.md. Against the
*seat* goal they are not equal — 1 pulls staff onto Ledgerly, 3 serves outside clients. The seat goal
breaks the tie toward reminders. If the goal were retention or card revenue, 3 would rank higher.

## The sequence (both squads in parallel, all shipping by 31 Mar 2027)

### Outcome 1 — Firms stop chasing late payers by hand (→ seats)
- **Metric it moves:** net new seats from firms that enable reminders (lagging); **leading:** # firms
  that switch reminders on, # overdue invoices auto-chased, # staff added to those firms.
- **The bet:** Bets 1 + 2 together. Reminders ship *with* controls — controls are a launch
  requirement, not a fast-follow.
- **Evidence & confidence:** Q1 (verbatim, HIGH) for the seat mechanism; Q3 + Leanpay (HIGH) for why
  controls ship first; market (QuickBooks/Xero/FreshBooks) shows it's table stakes. Overall MEDIUM.
- **Squad & effort:** **Squad B** (free from Jan wk 1). Rough sizing: Bet 1 ~6–7 wks, Bet 2 ~3 wks,
  overlapping → target ship **end Feb 2027**, buffer into March. *Needs squad estimate.*
- **Dependencies:** email deliverability/domain setup; existing invoice + overdue data.
- **What would make us drop it:** by **mid-Feb 2027**, if <25% of firms that enable reminders add ≥1
  seat within 30 days, stop treating it as expansion — keep as hygiene, and move the seat goal to
  sales/packaging.

### Outcome 2 — Clients can see and pay everything in one place (→ fewer resends, card attach)
- **Metric it moves:** % of invoices paid via the portal; # firms with card on (toward reducing the
  <50 today); manual "mark as paid" actions removed (today accountants mark each invoice paid by
  hand, idea.md).
- **The bet:** Bet 3, with Bet 4 as its prerequisite for the "pay" step.
- **Evidence & confidence:** Q2 (verbatim, HIGH) for the pain; seat impact LOW/indirect; table
  stakes. Overall LOW on the *seat* goal, MEDIUM on retention/value.
- **Squad & effort:** **Squad A** (3.5 effective). Rough sizing: Bet 4 onboarding ~2–3 wks first,
  then Bet 3 MVP ~7–8 wks. **Risk: may not fully ship by 31 Mar.** Scope hard to "view all invoices +
  pay where card is already on"; defer branded/full card rollout. *Needs squad estimate + security
  review slot.*
- **Dependencies:** existing payments partner; **security review for external-facing auth** (name the
  reviewer and book the slot in January, or this slips).
- **What would make us drop/defer it:** security review can't complete in-quarter, OR the card-on base
  (<50 firms) is judged too small to move any metric this quarter → defer portal to Q2, keep Squad A
  on card activation only.

## Why this sequence fits the constraints
- Squad B's free-in-January start goes to the greenfield, seat-carrying work (reminders) so it ships
  earliest and can be measured by mid-Feb.
- Squad A's payments/bank familiarity (and its 30% bank-feed tax) goes to the heavier, payments-touching
  portal, which is allowed to run the full quarter and is the one scoped to flex.
- Nothing here depends on a connector or data Ledgerly doesn't have, except the two baselines flagged.
