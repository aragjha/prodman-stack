DRAFT, not reviewed by a person

# 02 · The idea split into bets, with evidence and scores

The decision this serves: what to commit the two squads to for Q1 2027 so the work can ship by
31 March 2027 and support the goal of 300 net new seats. Full research: [01-REPORT.md](01-REPORT.md).

## The seat-goal reality check (do this math first)
- Seats grew from 1,760 (end June 2026) to 1,840 (end Sep 2026) = **+80 net seats last quarter**
  (source: idea.md).
- The Q1 2027 goal is **300 net new seats** = **3.75× last quarter's actual +80**, and about **+16%**
  on the current 1,840 base in a single quarter (300 ÷ 1,840 = 16.3%).
- At the list price of $25 per seat per month, 300 seats is about **$7,500/month ≈ $90,000/year** of new
  recurring revenue *at list* (expansion-seat pricing for existing firms was not given, so treat as a
  ceiling, not a forecast).
- **The only evidence-backed path from this work to seats is one firm's quote** (S7): remove the manual
  Friday chase, and the office manager would move "our two new juniors onto Ledgerly instead of the
  spreadsheet." That is a real mechanism but it is sized at one firm (+2 seats). Nothing in the inputs
  sizes how many firms share that pattern. **300 is a leadership target, not an evidence-backed forecast.**

## The three bets

### Bet A — Automatic payment reminders *with per-customer control*
Scheduled reminder emails that run until an invoice is paid, **plus** the controls to choose who gets
chased, pause a client, and edit the message and tone.
- **Evidence:** office manager would move 2 juniors onto seats if this existed (S7, from the PM, HIGH
  demand / MEDIUM seat-link); firm admin "I'd need to control who gets chased and what it says" (S9);
  a major competitor gives reminders free but on "one schedule that applies to every customer"
  ([Xero](https://trove.works/xero-invoice-reminders/), S2) — the control is the gap; over-automation
  "can damage trust" ([Chaser](https://www.chaserhq.com/blog/automated-payment-reminders), S6).
- **Why control is in-scope, not a nice-to-have:** plain reminders are already free elsewhere, so
  shipping them without control is a worse copy of a free feature; control is both the differentiator
  and the direct answer to the one objection a customer raised.
- **Confidence:** HIGH that firms want this; MEDIUM that it drives seats (single quote).

### Bet B — Client payment portal (one link, all invoices, pay)
One link per client to see every invoice from that firm and pay by card or bank.
- **Evidence:** partner "I want one link where they can see everything they owe us and pay it" (S8,
  from the PM, one firm); portals in this market earn on transaction fees, not seats — QuickBooks charges
  "2.99%" on card and "1%" on ACH with "No monthly fees or minimums"
  ([QuickBooks](https://quickbooks.intuit.com/payments/invoicing/), S3).
- **Seat link:** indirect at best. This is a get-paid-faster and retention/stickiness play, not a seat
  driver. Monetisation would be transaction fees, which is a different metric than seats.
- **Dependency:** card payments must be on — "Fewer than 50 firms have turned card payments on" (S12),
  so for most firms the portal would start as bank-transfer-only unless card activation moves.
- **Confidence:** MEDIUM demand (one quote); LOW that it moves the seat metric.

### Bet C — Card-payments activation push (enabler for Bet B)
Get more of the 300 firms to turn card payments on, so the portal can actually take card payment.
- **Evidence:** "Fewer than 50 firms have turned card payments on" (S12) out of ~300 paying firms.
- **Seat link:** none directly; it unlocks the portal's value and transaction-fee revenue.
- **Confidence:** this is an adoption/ops bet, not a build; effort is partner- and onboarding-dependent.

## Scores
Impact is **on the seat goal** (the metric leadership set). Effort is a **rough T-shirt size — nobody
has estimated it (idea.md), so these are placeholders for the squads to replace, not facts.**

| Bet | Impact on seats | Confidence | Effort (rough, unestimated) | Notes |
|---|---|---|---|---|
| A · Reminders + control | Medium–High (the only evidence-backed seat path, but sized at one firm) | Medium | Reminder engine M; control + tone S–M | Differentiator vs free built-in reminders; answers the control objection |
| B · Payment portal | Low (indirect; retention + faster cash, not seats) | Medium demand / Low seat-link | L (external surface, auth, payments, security review) | Earns on transaction fees, not seats; largest and riskiest build |
| C · Card activation | Low direct (enabler for B) | Medium | S–M, mostly ops/onboarding, partner-dependent | Without it the portal is bank-transfer-only for most firms |

**The close call to flag:** Bet B (portal) is the most-requested-sounding idea and the biggest build, yet
it is the one *least* connected to the seat goal. If the quarter's job is seats, A outranks B. If the
quarter's job is retention or payments revenue, B rises — but that is a different goal than the one stated.
