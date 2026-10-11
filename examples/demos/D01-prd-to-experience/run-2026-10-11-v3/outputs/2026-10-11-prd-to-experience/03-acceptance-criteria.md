DRAFT, not reviewed by a person

# 03 · Acceptance criteria

For every requirement R1–R10. **From PRD** = quoted/condensed from the acceptance cell in
`prd-client-portal.md` (line cited). **New** = written here because the PRD cell was empty or silent.
**(suggestion)** = adds scope; needs Maya's sign-off. Criteria are written to be testable (Given /
When / Then style, condensed).

## R1 · Invoice email links to the portal (line 34)
- **From PRD:** The link opens the portal without a password.
- **From PRD:** The link expires 30 days after it is issued.
- **From PRD:** On an expired link, the client can request a new one by email.
- **New:** An expired link shows an expired-link screen (not an error page) with a single
  "Send me a new link" action. **[G5 — Maya to confirm: automatic vs. manual, delivery time, and
  which email.]**
- **New (suggestion):** The link token is unique per client per firm and is not guessable by
  enumeration. **[G7 — security model to confirm.]**

## R2 · Portal lists the client's invoices from this firm (line 35)
- **From PRD:** Open invoices appear first, ordered by due date.
- **From PRD:** Paid invoices from the last 12 months appear below the open ones.
- **From PRD:** Each row shows invoice number, issue date, due date, amount and status.
- **New:** When the client has no open invoices, the list shows an "all paid / nothing due" state and
  still shows paid history. **[G8]**
- **New:** When the client has no invoices at all at this firm, an empty state explains the link is
  valid but nothing is outstanding. **[G8]**
- **New:** Only invoices from the firm that issued the link are shown. **[G15 — Open Q1 line 58,
  proposed "no" other firms.]**

## R3 · Portal shows the total owed (line 36)
- **From PRD:** The total equals the sum of all open invoices.
- **New (BLOCKER):** When open invoices span more than one currency, the portal shows **one total per
  currency** rather than a single combined number. **[G1 — Maya to confirm; a single cross-currency
  sum is not definable.]**
- **New (suggestion):** When a partially-paid invoice exists, the total reflects the **remaining
  balance**, not the original amount. **[G3/G4 — depends on the partial-payment decision.]**

## R4 · Pay one invoice by card (line 37)
- **From PRD:** The card payment runs on the partner's hosted page.
- **From PRD:** On success the invoice is marked paid within 1 minute.
- **From PRD:** On success the client is emailed a receipt.
- **New:** If the card is declined, the client returns to a payment-failed state, the invoice stays
  Open, and retry / another method are offered. **[G9]**
- **New:** If the client abandons the hosted page, the invoice stays Open and no receipt is sent.
  **[G9]**
- **New:** If the client returns before confirmation lands, the invoice shows a Processing state
  until the result is known (not success, not failure). **[G9]**
- **New:** A client cannot be charged twice for an invoice already marked paid. **[G9]**
- **New:** The receipt email states the firm, invoice number(s), amount paid and currency, and date.
  **[G10]**

## R5 · Select several invoices, pay in one card payment (line 38)
- **From PRD:** The total of the selected invoices is shown before payment.
- **From PRD:** One payment marks every selected invoice paid.
- **New (BLOCKER):** All selected invoices must be in the **same currency**; the UI prevents
  selecting across currencies in one payment. **[G1]**
- **New:** If a selected invoice changes state (e.g. paid elsewhere) before payment, it is removed
  from the selection and the client is told before paying. **[G9]**

## R6 · Pay by bank transfer (line 39) — **PRD acceptance cell is EMPTY**
- **New (DRAFT, BLOCKER):** Choosing bank transfer shows the firm's bank details and a payment
  reference for the invoice(s). **[G2]**
- **New (DRAFT, BLOCKER):** The invoice state after a bank transfer is chosen, and who/what marks it
  paid and when, must be defined. Proposed interim: invoice stays Open / "Awaiting transfer" until
  reconciled. **[G2/G3 — Maya must decide; this drives the primary metric, line 46.]**
- **Open:** Whether bank transfer supports multi-invoice (R5) and partial (R8) payment. **[G2/G4]**

## R7 · Download any invoice as a PDF (line 40)
- **From PRD:** The downloaded PDF is identical to the PDF attached to the invoice email.
- **New:** Download is available on both open and paid invoices. **[G11 — confirm.]**
- **New:** If the PDF cannot be produced, the client sees a clear retry / contact-firm message rather
  than a broken download. **[G11]**

## R8 · Pay part of an invoice where the firm allows it (line 41)
- **From PRD:** The client can enter an amount lower than the invoice total.
- **New:** The "pay part" option is shown only on invoices the firm has enabled for partial payment,
  and is visibly absent otherwise. **[G4 — how the firm flag is surfaced to confirm.]**
- **New:** After a partial payment, the invoice shows Partially paid with the remaining balance, and
  the total owed (R3) reflects the remaining balance. **[G3/G4 — new status, needs sign-off.]**
- **Open:** minimum partial amount; whether multiple partials are allowed; whether partial works by
  bank transfer; whether a partially-paid invoice can join a multi-select payment. **[G4]**

## R9 · Accountant sees when a client viewed an invoice (line 42)
- **From PRD:** The invoice list in Ledgerly shows "Viewed" with the date and time.
- **New:** "Viewed" is defined as a specific, agreed trigger (portal opened vs. invoice opened; first
  view vs. latest view). **[G12 — Maya to define; this is in Ledgerly, not the client portal.]**

## R10 · Portal shows the firm's logo and brand colours (line 43) — **PRD acceptance cell is EMPTY**
- **New:** The portal displays the firm's logo and brand colours when the firm has set them.
- **New:** When a firm has set no logo or colours, the portal uses a neutral default rather than a
  blank or broken header. **[G13]**
- **New (suggestion):** Brand colours never reduce text or control contrast below the accessibility
  minimum (see A11y below); a brand colour that fails contrast is overridden for text/controls.
  **[G6/G13]**

## Accessibility acceptance criteria (not in PRD — **(suggestion)**, see G6)
The PRD is silent on accessibility, and the client "often reads the invoice email on a phone"
(line 23). Proposed baseline:
- The portal is mobile-first and usable at a phone width without horizontal scrolling.
- Text and interactive controls meet WCAG 2.1 AA contrast; this overrides brand colours (R10) where
  they conflict.
- Amounts, currencies and statuses have text labels available to screen readers (not colour alone to
  signal status).
- All actions are reachable and operable by keyboard, with a visible focus order.
- The partner hosted payment page (line 29) is a third party we do not control; its accessibility is
  a **dependency to confirm**, not something this spec can guarantee.
