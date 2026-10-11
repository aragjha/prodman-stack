DRAFT, not reviewed by a person

# 01 · PRD gap review

Source: `examples/demos/D01-prd-to-experience/input/prd-client-portal.md` (draft v0.2), read
2026-10-11. Line numbers below refer to that file. Nothing here adds scope; new ideas are marked
**(suggestion)**.

## The gaps that block design, worst first

### G1 · Multi-currency breaks "the total owed" and "pay several in one payment" — BLOCKER
- Context line 28: "Firms can issue invoices in USD, CAD, EUR and GBP, and a client's invoices can
  be in any of these."
- R3 (line 36): "The total equals the sum of all open invoices." A single sum is undefined when the
  open invoices are in different currencies — you cannot add 100 USD and 100 EUR into one number.
- R5 (line 38): "One payment marks every selected invoice paid" and "The total of the selected
  invoices is shown before payment." A single card payment runs in one currency, so a client cannot
  pay a USD and a EUR invoice in one payment.
- **Decision needed from Maya:** when a client's open invoices span currencies, does R3 show one
  total per currency, and does R5 restrict a single payment to one currency? This changes the top of
  the portal and the whole multi-select flow. See `03-acceptance-criteria.md` R3/R5 and the
  judgment list.

### G2 · R6 "pay by bank transfer" has no acceptance criteria and no "mark paid" path — BLOCKER
- R6 (line 39): "The client can pay by bank transfer" — the acceptance-criteria cell is empty.
- R4 (line 37) marks a card invoice paid "within 1 minute" automatically. Bank transfer has no such
  mechanism: the money arrives later and someone has to match it. The PRD never says who marks a
  bank-transfer invoice paid, how, or when.
- This directly affects the **primary metric** (line 46, "median days from invoice sent to paid"):
  a bank transfer that is reconciled by hand days later counts very differently from a card payment.
- **Decision needed:** what does a client see after choosing bank transfer (firm bank details? a
  payment reference?), and who/what marks the invoice paid, and when. Until this is answered the
  bank-transfer screens are specified as a draft (see `04-screen-state-spec.md`, Screen 6).

### G3 · Status taxonomy is incomplete — overdue and partially-paid are implied but never named
- R2 (line 35) says each row shows a "status" and lists only two: "Open invoices first, by due
  date. Paid invoices from the last 12 months below."
- A due date (line 35) implies invoices can be **overdue**, but no overdue status is defined.
- R8 (line 41) lets a client "pay part of an invoice," which implies a **partially-paid** status and
  a remaining balance, neither of which R2, R3 or R5 account for.
- **Decision needed:** the full list of statuses a row can show (proposed: Open, Overdue,
  Partially paid, Paid, Processing) and how each affects the total owed (R3) and selectability (R5).

### G4 · Partial payment (R8) is under-specified and collides with R3, R5 and status
- R8 (line 41): "The client can enter an amount lower than the invoice total." Unspecified: is there
  a minimum? can a partial be paid by bank transfer as well as card? after a partial, does the total
  owed (R3) show the remaining balance or the full amount? can a partially-paid invoice be included
  in a multi-select payment (R5)? can a client pay several partials over time?
- "when the firm allows it" (line 41): the client needs to see *which* invoices allow partial
  payment; the PRD does not say how that is surfaced.

### G5 · Expired-link recovery (R1) is named but not designed
- R1 (line 34): "On an expired link, the client can request a new one by email." Unspecified: is the
  new link sent automatically or by a person? to which email? how long does it take? what does the
  client see in the meantime? what if the client's email changed? This is the client's re-entry
  point, so it needs a screen and a state.

### G6 · Accessibility is not mentioned anywhere in the PRD
- There is no accessibility requirement in the PRD, yet the Users table (line 23) says the client
  "Often reads the invoice email on a phone," and R10 (line 43) puts firm **brand colours** on the
  page — brand colours routinely fail colour-contrast minimums.
- **(suggestion)** Treat this as mobile-first and add baseline accessibility acceptance criteria
  (contrast, keyboard, screen-reader labels for amounts/currencies/statuses, focus order), plus a
  rule that brand colours never override the contrast minimum for text and controls. The payment
  step itself runs on the partner's hosted page (line 29), which we do not control — its
  accessibility is a dependency to confirm, not something we can specify. See `03` A11y section.

## Smaller gaps and ambiguities

| # | PRD line | Gap / ambiguity | Why it matters |
|---|---|---|---|
| G7 | R1, line 34 | "link to the client's portal" — one link per client per firm? per invoice? how is the token secured/guessed-against? | Determines what the link opens and the security model |
| G8 | R2, line 35 | No empty states: client with no open invoices; client with nothing at all; >12 months of paid history (pagination) | Empty and overflow states are unspecified |
| G9 | R4, line 37 | No card-failure paths: declined, abandoned on hosted page, return-without-result, webhook later than 1 minute, double-payment / already-paid | Error states are the bulk of a payment UI |
| G10 | R4, line 37 | "emailed a receipt" — contents, and whether a receipt can be re-downloaded in the portal, undefined | Clients "keep a copy" (line 23) |
| G11 | R7, line 40 | PDF "Identical to the PDF attached to the invoice email" — available for paid invoices too? what if the PDF is missing? | Download state coverage |
| G12 | R9, line 42 | "Viewed" — does it mean opening the portal, or opening a specific invoice? first view only or every view? | Changes what the accountant sees; it is in Ledgerly, not the client portal |
| G13 | R10, line 43 | No fallback when a firm has set no logo/colours; no format/size rules; contrast not addressed | Default branding state and a11y |
| G14 | Risks, line 54 | "Clients may not trust a link in an email" is a stated risk with no design response | Trust cues (firm name, branding, what-this-is copy) should be designed in |
| G15 | Open Q1, line 58 | "Should the portal show invoices from other Ledgerly firms? Proposed: no." | If no, a client with invoices at two firms gets two links; the UI must make the single-firm scope obvious |
| G16 | Open Q2, line 59 | "Do we notify the accountant when a client pays?" | Affects R9-adjacent accountant experience; not on the client's path but part of the full experience |
| G17 | Guardrail, line 47 | Guardrail metric baseline is "unknown" | Can't tell if the portal makes payment-support tickets worse without a baseline |

## What the PRD already specifies well (so design can start on these Monday)
- R1 expiry window: "Expires after 30 days" (line 34).
- R2 ordering and row fields: open first by due date, paid below for 12 months; row shows number,
  issue date, due date, amount, status (line 35).
- R4 card behaviour: partner hosted page, paid within 1 minute, emailed receipt (line 37).
- R5 pre-payment total and one-payment-marks-all (line 38) — within a single currency (see G1).
- Non-goals are explicit: no passwords, no saved cards/autopay, no reminders, no mobile app
  (lines 15-18) — so this is a password-less, mobile-responsive web portal.
- Primary metric with baseline and target: 34 days (August 2026) → 25 days by end of March 2027
  (line 46).
