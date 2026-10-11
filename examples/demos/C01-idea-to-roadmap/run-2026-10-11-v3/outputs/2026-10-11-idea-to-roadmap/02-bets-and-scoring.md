DRAFT, not reviewed by a person

# 02 · The idea, split into bets, and scored against the goal

**The goal the scoring serves:** 300 net new seats in Q1 2027 from existing firms adding seats
(expansion revenue), at $25 per seat per month. All evidence traces to `idea.md` (synthetic) or the
research report ([01-research-REPORT.md](01-research-REPORT.md)).

## The seat-expansion logic, stated plainly (this is the crux)
Leadership wants seats. The research found that reminders and portals are **not** monetised per seat by
anyone in the market, so the feature itself is not a seat lever. The only evidence that this work adds
seats is one customer (the office manager, 9-seat firm): *"If Ledgerly did that for me, I'd move our
two new juniors onto Ledgerly instead of the spreadsheet."* That is the mechanism: **when the chasing
and collection workflow lives in Ledgerly, firms put the staff who do that work onto Ledgerly, and each
of those staff is a seat.** The roadmap is therefore built to pull a whole workflow (chase → pay →
reconcile) into Ledgerly, not just to ship two features. The link is real but rests on **one data
point** — the single biggest risk in this plan, carried into "needs your judgment."

## The bets
The two-part idea plus its unavoidable dependencies split into four bets:

- **B1 — Automatic reminders, with firm controls.** Firm sets a schedule; Ledgerly emails overdue
  clients until paid; the firm controls who gets chased, the wording, and reminders stop when the
  invoice is paid.
- **B2 — Client payment portal.** One link per client showing every invoice from that firm, payable by
  card or bank transfer.
- **B3 — Auto-reconciliation (auto mark-as-paid).** When a client pays (portal or card), Ledgerly marks
  the invoice paid automatically, removing the step accountants do by hand today.
- **B4 — Card-payment activation.** Get far more than the current "fewer than 50 firms" onto card
  payments, since the portal's pay-online value is near-zero for a firm that cannot take card.

## Why each bet is or is not a seat-expansion lever
| Bet | Evidence | Confidence | Note |
|---|---|---|---|
| B1 Reminders | Customer 1 (verbatim) ties automated reminders directly to moving two juniors onto Ledgerly; late payment is the complaint the PM hears most | MEDIUM | Strongest *seat* link, but n=1. Reminders alone are table stakes vs Xero/QuickBooks, so controls are what differentiate |
| B2 Portal | Customer 2 (verbatim) wants "one link where they can see everything they owe us and pay it"; portal is the differentiated half vs built-in reminders | MEDIUM | Drives client usage and retention; seat link is indirect |
| B3 Auto-reconcile | Inferred from `idea.md`: "Accountants then mark each invoice as paid themselves." No customer asked for it directly | LOW (assumption) | This is the workflow staff do; automating it in Ledgerly is what makes the firm run collections here. Flagged assumption |
| B4 Card activation | `idea.md`: "Fewer than 50 firms have turned card payments on." Portal pay-online is useless without it | MEDIUM | Enabler, not a seat lever itself; gates B2's value |

## Scores
Scored 1–5 on **impact on the seat goal** and **confidence in the evidence**. Effort is **relative
(S/M/L) and must be confirmed by the squads** — `idea.md` states nobody has estimated build time, and
the C02 workflow note (workflows/INDEX.md) says "effort estimates should come from your engineers,
not from the model." So effort below is an **assumption to confirm**, not an estimate.

| Bet | Impact on seats (1–5) | Confidence (1–5) | Relative effort (assumption) | Inputs behind the score |
|---|---|---|---|---|
| B1 Reminders + controls | 4 | 3 | M | Only bet with a direct seat quote; controls needed to beat parity and calm customer 3's fear |
| B2 Client payment portal | 3 | 3 | L | Clear verbatim demand (customer 2); differentiated; but seat link indirect; larger surface |
| B3 Auto-reconciliation | 3 | 2 | M | Completes the workflow that justifies putting staff on Ledgerly; but no direct customer ask |
| B4 Card activation | 2 | 3 | S | Low direct seat impact; high as the gate that makes B2 worth anything |

## What this scoring says
- **No bet is a strong, well-evidenced seat lever on its own.** The seat case is a *workflow* case
  (B1+B3 together, with B2 as the client-facing surface), not a single-feature case.
- **Reminders must ship** (B1) because their absence is now conspicuous next to Xero/QuickBooks, and it
  carries the only direct seat evidence — but it is table stakes unless the **controls** (who gets
  chased, what it says) are good, which is also exactly what customer 3 demanded.
- **The portal (B2) is the differentiator** but is worthless where firms cannot take card, so **B4
  gates it**.
- **Auto-reconciliation (B3) is the quiet keystone** of the seat argument and has the weakest evidence;
  treat it as a bet to validate, not a certainty.

## The two closest calls (what would flip the order)
1. **B3 vs B2 priority.** If a quick data pull shows most firms already reconcile easily (few manual
   payments), B3 drops below B2. If manual reconciliation is a large time sink, B3 rises — it becomes
   the clearest reason to add AR staff seats.
2. **B1 scope — reminders vs controls.** If the late-payment data (the test in the report) shows the
   median firm has few overdue invoices, B1 shrinks to a thin feature and B2 becomes the lead bet.
