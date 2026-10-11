DRAFT, not reviewed by a person

# 03 · Q1 2027 roadmap (Jan–Mar), two squads

Serves the decision in [00-frame.md](00-frame.md); bets and scores in [02-bets-and-scores.md](02-bets-and-scores.md).
All effort sizes are rough placeholders — "Nobody has estimated it" (idea.md) — for the squads to replace.

## Capacity this quarter (from idea.md)
- **Squad A:** 5 engineers, but "About 30% of its time goes to bank feed maintenance, every quarter" →
  roughly **3.5 engineers effective** (5 × 0.70; derived, not stated).
- **Squad B:** 4 engineers, "finishing recurring invoices and is free from the first week of January" →
  **~4 engineers effective, unencumbered, from Jan 1.**
- Shared: 2 designers, 1 PM (Maya). Hard deadline: everything ships by **31 March 2027**.

## Recommended plan (A): run the squads in parallel
Squad B takes the seat lever (it is free and unencumbered from day one); Squad A takes the portal
(payments/banking adjacency via bank feeds), scoped as an MVP because A is the taxed, lower-capacity squad
and the portal is the largest, riskiest build.

### Outcome 1 — Firms stop chasing late payers by hand
- **Squad / window:** Squad B · Jan → ~mid-Feb
- **The bet:** automatic payment reminders (scheduled emails until the invoice is paid).
- **Metric it moves:** *leading* — number of firms with reminders enabled and invoices on an active
  schedule; *lagging* — net new seats via the chase-removal mechanism (S7).
- **Evidence / confidence:** office manager would move 2 juniors onto seats (S7); firm admin wants it (S9).
  HIGH that firms want it; MEDIUM that it drives seats.
- **What would make us drop or recut it:** if the "chasing today" count (the test in 01-REPORT) shows the
  spreadsheet-chaser pattern is rare, reminders still ship as table stakes but stop being sold as the seat
  driver, and the seat goal needs a second lever.

### Outcome 2 — Firms trust reminders on their biggest clients
- **Squad / window:** Squad B · ~mid-Feb → Mar 31
- **The bet:** per-customer control and tone — choose who gets chased, pause a client, edit the message.
- **Metric it moves:** share of firms that enable reminders on their named/top clients; this is the
  leading indicator that the control objection (S9) is cleared and reminders are safe to turn on widely.
- **Evidence / confidence:** S9 directly; Xero's built-in reminders use "one schedule that applies to
  every customer" (S2), so control is the differentiator. HIGH that it is wanted.
- **What would make us recut it:** if control needs more than the weeks left, ship a minimal "exclude this
  client" toggle and editable subject line first; defer full tone editing to Q2.

### Outcome 3 — Clients can see and pay everything in one place
- **Squad / window:** Squad A · Jan → Mar 31 (MVP)
- **The bet:** payment portal MVP — one link per client to see all their invoices and pay via the existing
  card/bank partner — plus a push to turn card payments on.
- **Metric it moves:** invoices paid through the portal; share of firms with card payments on (baseline
  "fewer than 50", S12); time-to-pay / DSO. **Not seats** — this is a get-paid-faster and retention play.
- **Evidence / confidence:** partner wants one link (S8, one firm); portals earn on transaction fees, not
  seats (S3). MEDIUM demand, LOW seat-link.
- **Dependencies:** card payments on (<50 firms today, S12); a security review for a new external,
  authenticated surface.
- **What would make us de-scope it:** if card activation stays near its <50 baseline, or the security
  review cannot finish by Mar 31, ship a view-only "see all your invoices" link this quarter and defer
  in-portal card payment to Q2.

## Alternative plan (B): point both squads at reminders, defer the portal
If leadership's only Q1 goal is seats, both squads build Outcomes 1 and 2 (reminders + control), shipping
the seat lever faster and at lower risk, and the portal (Outcome 3) moves to Q2.
- **Gains:** fastest, lowest-risk path to the one lever with an evidence-backed seat mechanism.
- **Gives up:** the partner's one-link request this quarter (S8), and any payments-revenue/retention upside
  from the portal.

**This is the call to make:** Plan A serves both the seat goal and the loudest customer ask but spreads a
taxed squad across a large build; Plan B maximises the seat lever but ships nothing on the portal this
quarter. The choice depends on whether Q1 is strictly a seats quarter — a leadership decision, flagged in
the handback.

## What this roadmap does not claim
- It does not claim 300 seats will be hit. 300 is 3.75× last quarter's actual +80 and rests on one
  customer's quote; the roadmap builds the conditions and a leading indicator, not a forecast.
- It does not use any internal late-payment rate (not provided) or any engineer effort estimate (none exist).
