# 02 · User flows — invoice email to paid invoice

Each flow lists the happy path and the unhappy paths. Steps trace to PRD requirements (Rn). The
client is on a phone (line 23) unless noted. Where multi-currency bites, both readings from gap B
are shown.

## Flow 1 — The spine: email → portal → paid (card, single invoice)
**Happy path**
1. Client receives the invoice email with a portal link (R1).
2. Taps the link → portal opens, no password (R1). First open logs "Viewed" for the accountant (R9).
3. Sees the firm's logo/brand (R10), the total owed per currency (R3, as revised in gap B), and the
   invoice list — open first by due date, paid below (R2).
4. Taps the invoice → taps **Pay by card**.
5. Redirected to the payments partner's hosted page (R4, line 29). Enters card, pays.
6. Returns to the portal → confirmation screen. Invoice shows **Paid** within 1 minute (R4).
7. Receipt emailed (R4). Client can still download the PDF (R7).

**Unhappy paths**
- **Card declined** → partner page shows the error; client returns, invoice still **Open**, a
  message invites retry. No status change.
- **Partner page times out / unreachable** → client returns to portal; invoice still **Open**;
  "we couldn't reach the payment page, try again" message. (Judgment: confirm the partner's return
  behaviour.)
- **Client closes the tab mid-payment** → no confirmation received; invoice stays **Open** until the
  partner confirms. If the charge actually went through, reconciliation marks it **Paid** on the
  next update and the receipt email still fires (R4). Needs a "payment pending" state (04).
- **Invoice already paid** between page-load and pay (paid by someone else, or by bank transfer) →
  portal blocks the pay action and shows **Paid**; if a charge was already in flight, flag for the
  firm to refund (judgment item — refunds are not in the PRD).
- **Double-submit / taps Pay twice** → second attempt is blocked once the first is in flight.

## Flow 2 — Pay several invoices in one card payment (R5)
**Happy path**
1. In the list, client selects several **open** invoices **in the same currency** (gap B).
2. A running total of the selected invoices is shown before payment (R5, line 38).
3. Taps **Pay selected** → partner hosted page for the combined amount → pays.
4. Every selected invoice is marked **Paid** by the one payment (R5). One receipt (or one per
   invoice — judgment item, not specified).

**Unhappy paths**
- **Selection spans currencies** → the portal prevents it: selecting a second currency either
  disables mismatched rows or warns "one currency per payment" (gap B). This is the behaviour that
  depends on confirming R5's currency rule.
- **One selected invoice gets paid elsewhere before submit** → it drops out of the selection with a
  notice; the total recomputes; client confirms the new total.
- **Partial-paid invoice in the selection** → only allowed if paying the full remaining balance;
  otherwise routed to the partial flow (Flow 4). Judgment item.
- Card declined / timeout / closed tab → as Flow 1; **no** invoice in the set changes status.

## Flow 3 — Pay by bank transfer (R6)
**Happy path**
1. Client taps **Pay by bank transfer** on an invoice (or on the whole balance).
2. Portal shows the firm's bank details and a reference to quote. Client pays from their bank.
3. Invoice shows **Payment pending** (new state — see gap A). It is **not** auto-marked paid: the
   problem statement says accountants mark invoices paid by hand (line 7) and R4's 1-minute rule is
   card-only.
4. When the firm reconciles, status becomes **Paid** and (if we decide to) a receipt is sent.

**Unhappy paths / open behaviour**
- **How long is "pending"?** Undefined. The client may return and still see pending — the screen
  must explain "your firm will confirm once the transfer arrives." Judgment item.
- **No "paid" email guaranteed** for bank transfer (R4 is card-only). Confirm whether bank-transfer
  payers get a receipt at all.

## Flow 4 — Partial payment (R8)
**Happy path**
1. On an invoice the firm has enabled partial payment for, client sees a **Pay part of this**
   control (must be visibly distinct — gap C/R8).
2. Client enters an amount lower than the invoice total (R8, line 41) → pays by card (R4 path).
3. Invoice becomes **Partially paid**; remaining balance shown; balance still counts toward the
   owed total (R3) and remains payable.

**Unhappy paths / open behaviour**
- **Firm has not enabled it** → no partial control shown; full amount only.
- **Amount entered = 0, negative, or ≥ total** → validation blocks; "enter an amount between the
  minimum and the full balance." Minimum is undefined (judgment item).
- Partial via bank transfer → combines Flow 3's manual reconciliation with partial state; confirm
  it's in scope for v1.

## Flow 5 — Expired or broken link (R1)
**Happy path (recovery)**
1. Client taps a link older than 30 days → **Link expired** screen (R1, line 34).
2. Client taps **Email me a new link** → confirmation that a new link is on its way.
3. New email arrives with a fresh link → back to Flow 1. (Who sends this — person or automation —
   is a judgment item; see gap C.)

**Unhappy paths**
- **PDF on an expired link**: allow download so the client can "keep a copy" (line 23)? Judgment.
- **Revoked / invalid link** (firm turned the portal off, link malformed) → a distinct
  "this link isn't available" screen pointing the client to contact the firm.

## Flow 6 — Nothing owed (empty state)
Client opens the portal and owes nothing (all paid): show a clear **"You're all paid up"** state
with paid history below (R2) and PDF downloads (R7). Prevents the "is this broken?" phone call.

## Flow 7 — Accountant: did they see it / pay it? (R9, open Q2)
- Accountant views the invoice list in Ledgerly → sees **Viewed** with date/time once the client
  opens it (R9, line 42). Confirm "viewed" = opened the specific invoice vs opened the portal.
- Open question 2 (line 59): notify the accountant when a client **pays**, or is the "Paid" status
  enough? Flagged as judgment — affects whether there's a payment notification at all.
