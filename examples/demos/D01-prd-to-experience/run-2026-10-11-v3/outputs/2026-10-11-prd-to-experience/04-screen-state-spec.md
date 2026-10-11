DRAFT, not reviewed by a person

# 04 · Prototype-ready screen & state specification

A designer or engineer can prototype from this. Each screen lists its purpose, the default state, and
every empty / error / edge state. Traces to PRD requirements (Rn, line) and gaps (Gn). This is
structure and behaviour, not visual design. All content in the prototype is **synthetic**.

Design frame: **mobile-first, password-less web** (non-goals, lines 15–18; client on a phone,
line 23). Every screen carries the firm logo + brand colours (R10) and a plain statement of what the
page is (trust response to Risk line 54 / U4).

---

## Screen 1 · Expired link (R1, line 34)
- **Purpose:** re-entry when a link is older than 30 days.
- **Default:** message that the link has expired, one action: "Send me a new link."
- **State 1b — request sent:** "Check your email" confirmation naming the email the invoice was sent
  to. **[G5 — automatic vs. manual, timing, changed-email case all undefined; shown as proposed.]**
- **Error:** request could not be sent → retry / contact firm.

## Screen 2 · Portal home — invoice list (R2 line 35, R3 line 36, R10 line 43)
- **Purpose:** the client sees what they owe and everything about this firm.
- **Header:** firm logo + brand colours (R10); "Invoices from {Firm}"; one line of what-this-is copy.
- **Total owed (R3):** sum of open invoices. **Multi-currency variant [G1]:** one total per currency.
- **List (R2):** open invoices first by due date, each row = number, issue date, due date, amount,
  status; paid invoices (last 12 months) below.
- **Statuses shown [G3]:** Open, Overdue, Partially paid, Paid, Processing (proposed set).
- **State 2b — all paid (U3/G8):** no open invoices → "You're all paid up" + paid history.
- **State 2c — empty (U3/G8):** no invoices at all → "Nothing is outstanding" + reassurance the link
  is valid.
- **State 2d — multi-currency (U5/G1):** totals grouped per currency; a note that each currency is
  paid separately.
- **State 2e — loading / long history:** paid history capped at 12 months (R2); confirm older access.
- **Select mode (R5):** toggles checkboxes on open rows; running selected-total appears; selecting
  across currencies is blocked **[G1]**.

## Screen 3 · Invoice detail
- **Purpose:** one invoice, its actions.
- **Default:** number, issue/due dates, amount, status; actions: **Pay by card** (R4), **Pay by bank
  transfer** (R6), **Download PDF** (R7), and **Pay part** (R8) *only if the firm allows it* **[G4]**.
- **State 3b — overdue:** due date in the past flagged (not by colour alone — A11y).
- **State 3c — partially paid [G3/G4]:** shows amount paid and remaining balance; Pay actions apply
  to the remaining balance.
- **State 3d — already paid:** shows Paid, receipt download (R4/R7); Pay actions hidden.

## Screen 4 · Pay by card hand-off and return (R4 line 37, R5 line 38)
- **Hand-off:** "Taking you to our secure payments page" → partner hosted page (line 29). We do not
  render card fields (non-goal: no saved cards, line 16; hosted page, line 29).
- **State 4a — success:** success screen; invoice(s) marked paid within 1 minute (R4); receipt
  emailed (R4); for multi-select, one payment marked all selected paid (R5).
- **State 4b — processing (U2/G9):** result not yet confirmed → "We're confirming your payment"; not
  success, not failure.
- **State 4c — failed / declined (U2/G9):** invoice stays Open; retry or choose another method.
- **State 4d — abandoned (U2/G9):** returned without paying; invoice Open; no receipt.
- **State 4e — already paid (U2/G9):** invoice paid elsewhere; no second charge.

## Screen 5 · Pay selected (multi-invoice) (R5, line 38)
- **Purpose:** confirm the set before paying.
- **Default:** list of selected invoices + **total before payment** (R5); "Pay by card."
- **State 5b — single currency enforced [G1]:** cannot proceed with mixed currencies; UI prevents it.
- **State 5c — selection changed (G9):** an invoice became paid → removed from set, client told
  before paying.

## Screen 6 · Pay by bank transfer (R6, line 39) — **DRAFT, blocked by G2**
- **Default (proposed):** firm bank details + a payment reference to quote; the invoice stays Open /
  "Awaiting transfer" until reconciled.
- **Blocked:** who/what marks it paid and when is undefined in the PRD (G2); this screen cannot be
  finalised until Maya decides. Affects the primary metric (line 46).

## Screen 7 · Pay part of an invoice (R8, line 41)
- **Default:** input for an amount **lower than the invoice total** (R8); shows resulting remaining
  balance; "Pay by card."
- **State 7b — invalid amount:** amount ≥ total, or ≤ 0, or below any firm minimum → blocked with a
  clear message. **[G4 — minimum and repeat-partial rules undefined.]**
- **Visibility:** only where the firm allows partial payment **[G4]**.

## Screen 8 · Download PDF (R7, line 40)
- **Default:** downloads a file identical to the email attachment (R7).
- **State 8b — unavailable (G11):** clear retry / contact-firm message, not a broken download.

## Screen 9 · Receipt / paid confirmation (R4, line 37)
- **Purpose:** the client keeps a copy (client need, line 23).
- **Default:** confirmation + receipt emailed; receipt re-downloadable from the paid invoice
  **[G10 — contents to confirm]**.

---

## State coverage matrix

| Screen | Default | Empty | Error / failure | Edge |
|---|---|---|---|---|
| 1 Expired link | expired + resend | — | send failed | changed email [G5] |
| 2 Home | open+paid list | all-paid (2b), none (2c) | load error | multi-currency (2d), 12-mo cap (2e) |
| 3 Invoice detail | actions | — | — | overdue (3b), partial (3c), paid (3d) |
| 4 Card return | success (4a) | — | failed (4c), abandoned (4d) | processing (4b), already-paid (4e) |
| 5 Pay selected | total+pay | — | selection changed (5c) | single-currency enforced (5b) [G1] |
| 6 Bank transfer | details+ref [DRAFT] | — | — | mark-paid undefined (6) [G2] |
| 7 Pay part | amount entry | — | invalid amount (7b) | firm-allowed only [G4] |
| 8 Download PDF | file | — | unavailable (8b) | paid invoices too [G11] |
| 9 Receipt | confirm+email | — | — | re-download [G10] |

## What the prototype covers vs. leaves as spec-only
The clickable prototype (`prototype/index.html`) walks Screens 1–9 and the key states above so the
team can step through the experience. Blocked screens (6 bank transfer) and blocked states
(multi-currency total, partial-paid status) are shown **marked as draft / decision-needed** so the
gaps are visible in the walkthrough rather than hidden.
