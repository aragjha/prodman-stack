DRAFT, not reviewed by a person

# 03 · Q1 2027 roadmap — "chase, pay, reconcile" lives in Ledgerly

**Decision it serves:** ship, by 31 March 2027, a collections workflow that pulls chasing, payment and
reconciliation into Ledgerly so firms move staff onto it — targeting 300 net new seats.

**The honest seat math first (derived, flagged).** Seats grew 1,760 → 1,840 last quarter = **+80**.
The goal of **300** is **3.75× that pace** (300 ÷ 80 = 3.75). At $25/seat/month, 300 seats ≈ **$7,500**
new monthly recurring revenue, ≈ **$90,000** annualised (300 × $25 × 12). These are my arithmetic from
`idea.md`, not figures from it. **Net new seats is a lagging metric**: features that ship in Feb–Mar
cannot drive a full quarter of adoption inside the same quarter, so the plan tracks **leading
indicators** (firms with the workflow live, staff added) and treats 300 seats as the outcome the work
*sets up*, likely landing partly after Q1. Whether 300 is achievable from this work in this window is
the first thing for leadership's judgment.

## Capacity (an assumption to confirm with the squads)
- **Squad A — 5 engineers, ~30% on bank-feed maintenance** → ~3.5 engineers on new work. Owns
  money-movement, so it takes the **payments/portal/reconcile** track (B2, B3, B4).
- **Squad B — 4 engineers, free from the first week of January**, finishing recurring invoices
  (invoicing domain) → takes the **reminders** track (B1).
- **No build estimates exist** (`idea.md`), so sequencing is by dependency and value; every item's
  effort says "size with the squad." I have not invented durations.

## How the two tracks run across the quarter
| | January | February | March |
|---|---|---|---|
| **Squad B (reminders)** | B1 reminders MVP: firm-set schedule, email until paid, **stop on payment** | B1 controls: exclude/choose who gets chased, edit message, per-client overrides (customer 3) | Harden, firm-facing reminder status; wire "stop on payment" to real payment events |
| **Squad A (payments)** | B4 card-activation flow + B2 portal foundation (one link, all of a client's invoices) | B2 pay-by-card/bank in portal | B3 auto mark-as-paid / reconciliation; rollout to card-enabled firms |

Dependency spine: **B4 (card on) → B2 (portal pays) → B3 (auto-reconcile)**; B1 runs parallel but its
"stop on payment" depends on payment events from the Squad A track in March.

---

## Roadmap items (outcomes, not features)

### Outcome 1 — Firms stop chasing late payers by hand
- **Metric it moves (leading):** number of firms with automatic reminders active; share of overdue
  invoices covered by a reminder sequence.
- **The bet:** B1 reminders with firm controls.
- **Evidence & confidence:** MEDIUM. Customer 1 (verbatim) ties this to moving two juniors onto
  Ledgerly; late payment is the most common complaint. Reminders are table stakes vs Xero/QuickBooks
  ([report](01-research-REPORT.md)), so the **controls** are the differentiator.
- **Effort:** M — size with Squad B.
- **Dependencies:** invoice due-date and payment-status data; "stop on payment" needs Outcome 3's
  payment events (so full stop-on-payment lands in March).
- **Guardrail metric:** zero reminders sent after an invoice is paid; no rise in firms' client
  complaints or opt-outs (directly addresses customer 3's "robot nagging my biggest clients" fear).
- **What would make us drop or shrink it:** the late-payment data pull (the report's test) shows the
  median firm has few overdue invoices — then reminders become a thin feature and Outcome 2 leads.

### Outcome 2 — A firm's clients see and pay everything in one place
- **Metric it moves:** number of firms with the portal live; share of invoices paid through the portal.
- **The bet:** B2 client payment portal.
- **Evidence & confidence:** MEDIUM. Customer 2 (verbatim) wants "one link where they can see
  everything they owe us and pay it"; the portal is the differentiated half of the idea. A vendor
  claims portals roughly halve payment wait time ([Paidnice](https://www.paidnice.com/blog/what-is-a-customer-payment-portal)) — vendor claim, weak signal only.
- **Effort:** L — size with Squad A.
- **Dependencies:** **B4 card activation must come first** — the portal's pay-online value is near-zero
  for a firm that cannot take card (fewer than 50 firms can today).
- **Guardrail metric:** payment success rate and failed-payment/support volume do not worsen.
- **What would make us drop it:** card activation (Outcome 4) stalls, leaving too few firms able to use
  the portal to justify the build this quarter.

### Outcome 3 — Accountants stop marking invoices paid by hand
- **Metric it moves:** share of payments auto-reconciled (auto mark-as-paid) vs manual.
- **The bet:** B3 auto-reconciliation.
- **Evidence & confidence:** LOW (assumption). Inferred from `idea.md` ("Accountants then mark each
  invoice as paid themselves"); no customer asked for it directly. This is the keystone of the seat
  argument — it is the staff work that justifies putting AR people on Ledgerly — so it is a bet to
  **validate**, not a certainty.
- **Effort:** M — size with Squad A.
- **Dependencies:** B2 portal and card payments producing payment events.
- **Guardrail metric:** zero invoices wrongly marked paid (false reconciliations); reconciliation
  errors do not exceed today's manual error rate.
- **What would make us drop it:** a data pull shows manual reconciliation is already light (few manual
  payments), so automating it saves little and frees no staff to redeploy.

### Outcome 4 — Many more firms can take card payments
- **Metric it moves:** number of firms with card payments enabled (from "fewer than 50" today).
- **The bet:** B4 card activation.
- **Evidence & confidence:** MEDIUM. `idea.md` states fewer than 50 firms have card on; the portal
  depends on it. Whether the blocker is supply (the payments partner's onboarding) or demand is unknown
  — a gap to check before building.
- **Effort:** S — size with Squad A.
- **Dependencies:** existing payments partner; find out why adoption is low first.
- **Guardrail metric:** no increase in failed onboarding or chargebacks.
- **What would make us drop it:** the blocker turns out to be a payments-partner contract/compliance
  limit we cannot move this quarter — then escalate, do not keep building around it.

---

## The seat outcome these four set up
- **Metric (lagging, the leadership goal):** net new seats, target 300 in Q1 2027. Baseline pace +80
  last quarter.
- **Leading proxy to watch weekly:** number of firms running the full chase→pay→reconcile workflow in
  Ledgerly, and staff added to collections roles on those firms (customer 1's mechanism).
- **The bet:** B1+B3 make Ledgerly the place the collections workflow happens; B2 is the client-facing
  surface; firms then move AR staff onto Ledgerly.
- **Confidence:** LOW on hitting 300 from this work inside this quarter — one data point for the
  feature→seat link, an aggressive 3.75× target, and lagging adoption. The product is deliverable by
  31 March; the seat number is not guaranteed by it.
- **What would make us change the plan:** if, by early February, firms turning reminders on are **not**
  adding collections staff, the seat thesis is wrong and the quarter should pivot to packaging/pricing
  levers (a leadership call), because no amount of this feature work will move seats on its own.

## Guardrails that span the whole roadmap
1. No reminder ever fires after payment (brand risk; customer 3).
2. Bank-feed maintenance stays covered (Squad A's standing ~30%); this plan does not borrow from it.
3. Every number a firm sees in reminders/portal (amount owed, due date, paid status) is correct —
   a wrong "you owe" is worse than a late payment.
