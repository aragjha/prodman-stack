# 04 · Prototype-ready screen & state specification

Every screen, every state, including empty and error. Mobile-first (clients are on a phone,
line 23). Each screen lists: purpose, elements, states, and the PRD requirement it serves. This is
the spec the clickable prototype (in `prototype/`) is built from.

Legend: **[PRD]** = specified in the PRD · **[proposed]** = suggestion for Maya to confirm.

---

## S0 · Invoice email (entry point) — R1
- **Purpose.** Get the client to the portal.
- **Elements.** Firm branding; invoice summary (number, amount, due date); **View & pay** button
  linking to the portal (R1); the PDF still attached (R7, line 40).
- **States.**
  - Default.
  - (Email itself has no error state; a dead link is handled at S6.)

## S1 · Portal home — the invoice list — R2, R3, R10
- **Purpose.** Show everything owed to this firm and start a payment.
- **Elements.**
  - Header: firm logo + brand colours (R10); a one-line "invoices from [Firm]" trust label [proposed].
  - **Amount owed**, shown **per currency** (R3 + gap B): e.g. "You owe: $1,240 USD · €300 EUR".
  - **Open invoices** first, sorted by due date (R2); each row: number, issue date, due date,
    amount, status (R2, line 35).
  - **Paid invoices** (last 12 months) below (R2).
  - Per open row: **Pay** and **Download PDF** (R7). Overdue rows flagged [proposed].
  - Multi-select affordance to pay several (R5) — checkboxes per open row, within one currency.
- **States.**
  - **Default** — has open invoices.
  - **Empty / all paid up** — no open invoices → "You're all paid up" + paid history (Flow 6).
  - **Bank-transfer-only firm** — no card buttons, no multi-select; only bank transfer (gap F).
  - **Multi-select active** — a sticky bar shows the running total of selected invoices and
    **Pay selected** (R5); selecting a second currency is blocked with a message (gap B).
  - **Loading** — skeleton rows.
  - **Mixed statuses** — open, overdue, partially paid, payment pending, paid all visible with
    distinct labels.

## S2 · Invoice detail — R4, R6, R7, R8
- **Purpose.** Pay or download one invoice.
- **Elements.** Invoice number, dates, line amount, status; **Pay by card** (R4); **Pay by bank
  transfer** (R6); **Download PDF** (R7); **Pay part of this** control *only if the firm enabled it*
  (R8).
- **States.**
  - **Open** — all pay actions available (subject to firm settings).
  - **Overdue** — same actions, overdue flag [proposed].
  - **Partially paid** — shows amount paid + remaining balance; pay-remaining available (R8).
  - **Payment pending** — bank transfer initiated, awaiting firm confirmation; pay actions hidden
    (Flow 3).
  - **Paid** — pay actions disabled; **Download PDF** and receipt link remain (R4, R7).
  - **Card-off firm** — no card button; bank transfer only (gap F).

## S3 · Card payment — partner hosted page — R4, R5
- **Purpose.** Take the card payment off-site on the partner's page (line 29).
- **Elements.** Owned by the payments partner, not us. Shows the amount (single or combined total,
  R5) and returns to the portal.
- **States (as the portal must handle on return).**
  - **Success** → go to S4 confirmation; invoice(s) **Paid** within 1 minute (R4).
  - **Declined** → return to S2/S1; invoice stays **Open**; retry offered (Flow 1).
  - **Timeout / unreachable** → return with "couldn't reach payment"; invoice **Open** (Flow 1).
  - **Abandoned (tab closed)** → no return; invoice **Open** or **Payment pending** until the
    partner confirms (Flow 1). *Dependency: confirm partner return URLs and statuses.*

## S4 · Payment confirmation — R4
- **Purpose.** Reassure the client the payment landed.
- **Elements.** Success message; what was paid (invoice number(s) + amount); "receipt emailed to
  you" (R4); **Download PDF**; back to portal.
- **States.**
  - **Card success** — invoice(s) marked Paid (R4).
  - **Pending** — payment is processing (fallback if the partner hasn't confirmed within 1 minute).

## S5 · Bank transfer instructions — R6
- **Purpose.** Give the client what they need to pay by transfer.
- **Elements.** Firm bank details; a reference to quote; the amount; "your firm will confirm once
  the transfer arrives"; back to portal.
- **States.**
  - **Default** — details shown; invoice now **Payment pending** (Flow 3).
  - **Not available** — if the firm offers no bank transfer, this screen isn't reachable.

## S6 · Link expired / unavailable — R1
- **Purpose.** Recover a client who arrived on a dead link.
- **Elements.** Plain explanation; **Email me a new link** action (R1); on success, "a new link is
  on its way."
- **States.**
  - **Expired (>30 days)** — request-new-link available (R1, line 34).
  - **Revoked / invalid** — "this link isn't available," contact-the-firm message (Flow 5).
  - **Request sent** — confirmation.

## S7 · Partial payment entry — R8
- **Purpose.** Let the client pay part of an invoice when the firm allows it.
- **Elements.** Remaining balance; amount input (R8); validation message; **Continue to card**.
- **States.**
  - **Default** — empty input.
  - **Valid amount** (> 0 and < remaining) — continue enabled.
  - **Invalid** (0, negative, ≥ remaining) — blocked with a message (Flow 4).
  - **Not enabled** — screen not reachable for this invoice.

---

## State model summary (invoice statuses)
PRD R2 names only Open and Paid. The flows require these additional statuses — **confirm this set**:

| Status | In PRD? | Trigger |
|---|---|---|
| Open | yes (R2) | issued, unpaid |
| Overdue | no [proposed] | past due date, unpaid |
| Partially paid | no [proposed] | a partial payment made (R8) |
| Payment pending | no [proposed] | bank transfer initiated, firm not yet reconciled (R6) |
| Paid | yes (R2/R4) | fully paid, or firm reconciled a transfer |

## Cross-cutting
- **Responsive:** every screen designed phone-first, scaling up (gap D).
- **Accessibility baseline:** keyboard operable, labelled controls, visible focus, amounts/currency
  announced, 4.5:1 contrast floor on brand colours (gap D, R10).
- **Trust:** firm branding on every screen (R10); a plain "why you're seeing this" line (gap E).
- **Viewed tracking:** first portal open and/or invoice open logs "Viewed" for the accountant (R9).
