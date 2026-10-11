DRAFT, not reviewed by a person

# 04 · Screen & state specification (prototype-ready)

Scope: the **Client** portal only (the part this project builds). Accountant (R9) and firm-admin
(R10 branding) touchpoints live in Ledgerly and are referenced, not specified here.

Conventions: mobile-first (320px up), since the client "Often reads the invoice email on a phone"
(PRD). Each screen lists its purpose, the content it shows (every field traces to a PRD requirement),
its states, and its actions. **[assumption]** = a choice the prototype makes that Maya confirms.
All sample data below is **SYNTHETIC** (the PRD itself is synthetic).

---

## Screen map

```
Invoice email ──tap link──► S1 Portal home ──┬─► S2 Invoice detail ─► S3 Review & pay ─► [hosted page] ─► S5 Processing ─► S6 Confirmation
   (R1)                      (R2,R3,R9,R10)   │                        (R4,R5,R6,R8)                        (R4)            (R4,R5)
                                              └─► S4 Multi-select mode (R5)  ─────────────────┘
Expired link ──► S0 Expired-link page (R1,U1)
Empty variants: S1a All paid up (U6) · S1b Nothing here yet (U7)
Failure variants: S7 Payment failed (U2) · inline states for abandoned/already-paid/processing-stall
```

---

## S0 · Expired-link page  (R1 · U1)
- **Purpose:** recover a client who clicked a link older than 30 days.
- **Shows:** firm branding (R10); "This link has expired"; one line of plain reassurance.
- **Actions:** **Email me a new link** → inline confirmation "A new link is on its way to {email}".
- **States:** default; request-sent confirmation. **[gap: delivery mechanism/owner undefined — 01-C]**

## S1 · Portal home  (R2 · R3 · R9 · R10)
- **Purpose:** the client sees everything they owe this firm and can act.
- **Header:** firm logo + brand colour (R10); plain-language title ("Your invoices from {Firm}") to
  build trust against the phone-instead risk (02).
- **Total owed (R3):** shown **per currency** (01-A), e.g. a card per currency: "You owe **$1,200.00
  USD**". No mixed-currency single number. **[assumption: Plan A]**
- **Open invoices (R2):** sorted by due date ascending, above paid. Each row: invoice number, issue
  date, due date, amount **+ currency**, status badge. Overdue rows flagged (text + icon, not colour
  alone). Row actions: open detail; quick **Pay**.
- **Paid invoices (R2):** last 12 months, collapsed/secondary, below open.
- **Actions:** open an invoice (S2); **Pay** a single invoice (→S3); **Select** to enter multi-select
  (S4); download PDF (R7) from the row menu.
- **On load:** records "Viewed" for the accountant (R9) **[gap: trigger — 01-C]**.
- **States:**
  - **S1 default** (has open invoices).
  - **S1a All paid up (U6):** no open invoices → positive empty state; total reads nothing owed; paid
    history still shown.
  - **S1b Nothing here yet (U7):** no invoices at all → plain empty state, no actions.
  - **Bank-transfer-only variant (01-D8):** no "Pay by card" anywhere; "Pay by bank transfer" is the
    primary action. This is the **common** case (<50 firms have card on).
  - **Multi-currency:** one total card per currency; selection scoped to one currency (S4/U8).

## S2 · Invoice detail  (R2 · R4 · R6 · R7 · R8)
- **Purpose:** show one invoice and start payment.
- **Shows:** number, issue date, due date, amount + currency, status; **the same invoice number and
  amount as the email/PDF** so the client can match them (trust, 02).
- **Actions:** **Pay by card** (R4, hidden in bank-transfer-only firms); **Pay by bank transfer**
  (R6); **Pay part** (R8, only if the firm allows it on this invoice); **Download PDF** (R7).
- **States:** open; overdue; **Partially paid** (shows paid + remaining — R8); **Awaiting bank
  transfer** (R6); **Processing** (U4); **Paid**; **Already paid** notice (U5); PDF-download error (U9).

## S3 · Review & pay  (R4 · R5 · R6 · R8)
- **Purpose:** confirm amount + method before leaving to the hosted page.
- **Shows:** the amount and **currency** to be paid (single invoice, selected total R5, or partial
  amount R8); the method chosen.
- **Actions:** **Pay by card** → partner hosted page (R4); **Pay by bank transfer** → S_bank; Back.
- **States:** default; partial-amount entry (R8) with validation (AC-R8.2: >0 and < total).

## S4 · Multi-select mode  (R5 · U8)
- **Purpose:** pay several open invoices in one card payment.
- **Shows:** checkboxes on open rows; a **sticky bar with the running selected total** (R5), in one
  currency.
- **Rules:** only same-currency invoices selectable together (01-A); selecting another currency is
  blocked with a message (U8); partially-paid invoices not selectable in v1 (AC-R8.4). **[assumption]**
- **Actions:** **Pay selected** (→S3 with the combined total); Clear; Cancel.

## S_bank · Bank transfer details  (R6)
- **Purpose:** give the client what they need to pay from their bank.
- **Shows:** firm bank details + unique reference, in the invoice currency (AC-R6.1); which
  invoice(s) it covers. **[all proposed — PRD R6 was blank]**
- **After:** invoice stays **Awaiting bank transfer** and still counts as owed (AC-R6.3) until the
  firm confirms. No charge happens in the portal.

## S5 · Processing  (R4 · U4)
- **Purpose:** cover the "paid within 1 minute" settle window (R4).
- **Shows:** Processing indicator on the invoice; pay actions disabled to prevent double pay.
- **States:** resolves to Paid (→S6); or **still-processing** message if it exceeds the expected
  window **[gap: window length undefined]**.

## S6 · Confirmation + receipt  (R4 · R5)
- **Purpose:** close the loop.
- **Shows:** success message; the invoice(s) now Paid; note that a **receipt email** was sent (R4).
  For multi-invoice (R5), lists every invoice paid. **[gap: receipt for R5/R8/R6 not specified in PRD]**
- **Actions:** back to home (now showing reduced/nil total); download receipt/PDF (R7).

## S7 · Payment failed  (U2)
- **Shows:** card declined/failed; invoice still open; nothing charged.
- **Actions:** **Try again** (card); **Pay by bank transfer** (R6); back.

### Cross-cutting inline states
- **Abandoned (U3):** silent return, invoice open, no error.
- **Already paid (U5):** inline notice, row → Paid, drops from selection/total.
- **PDF unavailable (U9):** inline error, invoice still payable.

---

## State matrix (every invoice row can be in exactly one)

| Status | From | Shown as | Payable? | Counts toward total owed (R3)? |
|---|---|---|---|---|
| Open | R2 | badge "Open" (+"Overdue" if past due) | yes | yes |
| Processing | R4/U4 | "Processing" | no (disabled) | yes (until resolved) |
| Awaiting bank transfer | R6 | "Awaiting transfer" | no (already initiated) | yes |
| Partially paid | R8 | "Partially paid" + remaining | yes (remaining) | yes (remaining only) |
| Paid | R4/R5/R6 | "Paid" + date | no | no |

---

## Accessibility notes per screen (target WCAG 2.2 AA — 01-E, all [suggestion])
- Status is never colour-only: every badge has text (and icon for overdue).
- Focus moves to the new message on S5→S6 and on S7 so screen-reader users hear the result.
- The sticky selected-total bar (S4) is announced on change.
- Amounts announced with currency (AC-A11Y.3). Targets ≥44px; works at 320px (AC-A11Y.4).
- Brand colour (R10) only applied where it passes contrast; otherwise accessible fallback (AC-R10.3).

---

## What the prototype covers vs. not
**Covered (clickable):** S0, S1 (+S1a all-paid, +bank-transfer-only variant), S2, S3, S4 (with
cross-currency block), S_bank, S5, S6, S7, and the multi-currency home.
**Shown as static note, not fully wired:** partial-payment entry math (R8), PDF file download (R7 —
prototype shows the action, not a real PDF), the accountant's Ledgerly "Viewed"/paid views (R9,
outside this project).
