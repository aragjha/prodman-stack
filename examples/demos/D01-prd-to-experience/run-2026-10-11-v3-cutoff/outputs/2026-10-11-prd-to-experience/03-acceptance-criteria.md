DRAFT, not reviewed by a person

# 03 · Acceptance criteria

Two kinds of entry below:
- **Kept as-is** — the PRD's criterion is already testable; repeated so engineering has one list.
- **Proposed** — the PRD left the cell blank or thin; this is a draft criterion for Maya to accept,
  edit or decline. Every proposed line is a **[suggestion]**, not added scope.

All proposed criteria are written to be testable (a tester can make them pass or fail). Accessibility
criteria assume the **WCAG 2.2 AA** target proposed in `01-E` — confirm or drop it.

---

## Requirements that already have criteria (kept, lightly sharpened where noted)

- **R1 — Email link, no password.** Opens the portal without a password; link expires 30 days after
  issue; an expired link shows a page with a working "email me a new link" action. *Sharpen:* define
  who receives/sends the new link and the target time to deliver it.
- **R2 — Invoice list.** Open invoices sorted by due date ascending appear above paid invoices from
  the last 12 months; every row shows invoice number, issue date, due date, amount **with its
  currency**, and status.
- **R3 — Total owed.** The total(s) shown equal the sum of open invoices. *Sharpen (01-A):* totals are
  shown **per currency**; no single number mixes currencies.
- **R4 — Pay one by card.** Payment runs on the partner's hosted page; on success the invoice shows
  Paid within 1 minute and a receipt email is sent to the client. *Add:* a declined/failed payment
  returns the client to the portal with the invoice still open and nothing charged (U2).
- **R5 — Pay several by card.** The combined total of the selected invoices is shown before payment;
  one successful payment marks every selected invoice paid. *Sharpen:* selection is limited to one
  currency (01-A); a single failed charge marks none paid (U2).
- **R7 — Download PDF.** The downloaded file is byte-for-byte the PDF attached to the invoice email;
  available for both open and paid invoices.
- **R9 — "Viewed" for the accountant.** Ledgerly's invoice list shows "Viewed" with date and time.
  *Decide:* the trigger — portal-open vs opening that specific invoice (01-C).

---

## R6 — Pay by bank transfer  (PRD cell was EMPTY — proposed)

- **AC-R6.1 [suggestion]** Selecting bank transfer shows the firm's bank account details and a unique
  payment reference for the invoice (or the selected set), in the invoice's currency.
- **AC-R6.2 [suggestion]** Bank details shown match those configured by the firm admin for that
  currency; if none are configured for a currency, bank transfer is not offered for those invoices.
- **AC-R6.3 [suggestion]** Until the firm confirms receipt, the invoice shows **Awaiting bank
  transfer** and still counts toward the amount owed (R3).
- **AC-R6.4 [suggestion]** When a firm user marks the transfer received, the invoice shows Paid and
  (decide) a receipt email is sent.
- **Open for Maya:** who confirms a transfer and how, and whether any auto-reconciliation exists.
  This is the metric risk in `01-B` — spell it out before beta.

## R8 — Partial payment  (criterion was thin — sharpened)

- **AC-R8.1** The "pay part" option appears only on invoices the firm has flagged as allowing it.
- **AC-R8.2** The client can enter an amount greater than 0 and less than the invoice total; the UI
  rejects 0, negative, and amounts ≥ the total with a clear message. **[suggestion: these bounds]**
- **AC-R8.3 [suggestion]** After a successful partial payment the invoice shows **Partially paid**
  with amount paid and remaining balance; the home total (R3) reflects the remaining balance.
- **AC-R8.4 [suggestion]** A partially-paid invoice is **excluded** from multi-select card payment
  (R5) in v1 unless Maya decides otherwise (interaction undefined in PRD — 01-C).

## R10 — Firm branding  (PRD cell was EMPTY — proposed)

- **AC-R10.1 [suggestion]** The portal shows the firm's logo and brand colour as configured by the
  firm admin (per the User table: admin "add branding").
- **AC-R10.2 [suggestion]** If no logo or colour is configured, the portal falls back to a neutral
  default that still passes contrast.
- **AC-R10.3 [suggestion]** Brand colours are applied only where they pass **WCAG 2.2 AA** contrast
  against their foreground/background; interactive elements (buttons, links, focus rings) that would
  fail fall back to an accessible colour automatically.

---

## Accessibility acceptance criteria (NONE in the PRD — all proposed, 01-E)

- **AC-A11Y.1 [suggestion]** Every screen and state meets WCAG 2.2 AA: text contrast ≥ 4.5:1 (≥ 3:1
  for large text and UI components), no information by colour alone (status also has text/icon).
- **AC-A11Y.2 [suggestion]** The full flow (view → select → pay → confirm) is operable by keyboard
  alone, with a visible focus indicator and a logical focus order; focus moves to new content on
  state change (e.g. to the Processing/Paid message).
- **AC-A11Y.3 [suggestion]** Amounts are announced with their currency to screen readers (e.g.
  "1,200 US dollars", not "1,200"); status badges have text labels.
- **AC-A11Y.4 [suggestion]** Mobile-first: usable at 320px width, touch targets ≥ 44×44px, no reliance
  on hover; works in portrait one-handed (client reads on a phone — PRD User table).

---

## Acceptance criteria for the added states (02 unhappy paths — all proposed)

| State | Proposed acceptance criterion |
|---|---|
| Expired link (U1) | Shows an expired message and a single action that requests a new link; confirms the request was sent. |
| Payment failed (U2) | Invoice remains open, nothing is charged, client can retry card or switch to bank transfer. |
| Payment abandoned (U3) | Returning from the hosted page with no payment leaves the invoice open and shows no error. |
| Processing (U4) | While settling, the invoice shows Processing and its pay actions are disabled; it resolves to Paid, or shows a "still processing" message if it exceeds the expected window. |
| Already paid (U5) | An invoice paid by another route shows Paid, leaves any active selection, and is removed from the total. |
| All paid up (U6) | Shows a positive empty state; paid history (last 12 months) remains visible. |
| No invoices (U7) | Shows a plain "nothing here yet" state with no actions. |
| PDF unavailable (U9) | Shows an inline download error; the invoice stays viewable and payable. |
