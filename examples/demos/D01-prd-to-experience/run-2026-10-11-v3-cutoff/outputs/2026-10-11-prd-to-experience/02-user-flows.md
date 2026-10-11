DRAFT, not reviewed by a person

# 02 · User flows — invoice email → paid invoice

Primary actor: the **Client** (no Ledgerly login; often on a phone — PRD User table). Secondary
touchpoints for **Accountant** (R9) and **Firm admin** (R10) are noted where they appear.
Each flow traces to PRD requirements. Unhappy paths are included per the D01 workflow.

Legend: `→` next step · `⤷` branch · **[gap]** not in the PRD, added here · **[assumption]** a
choice the prototype makes that Maya must confirm.

---

## Flow 0 — The spine (happy path, card, single invoice)

1. Firm sends invoice. Email includes the PDF **and** a portal link (R1). Client is often on a phone.
2. Client taps the link → portal opens **without a password** (R1).
3. **Portal home** shows the total owed (R3) and the invoice list: open first by due date, then paid
   from the last 12 months (R2). Opening the portal records a "Viewed" event for the accountant
   (R9) — **[gap: trigger is portal-open vs invoice-open; see 01-C]**.
4. Client taps an invoice → **invoice detail** (number, dates, amount, status; download PDF — R7).
5. Client taps **Pay** → **review** screen shows the amount and currency to be paid (R4/R5 pattern).
6. Client taps **Pay by card** → redirected to the **partner's hosted page** (R4).
7. Client enters card details on the hosted page and confirms.
8. Client is returned to the portal → **Processing** state (the "within 1 minute" window — R4) **[gap: this state is implied, not specified]**.
9. Invoice flips to **Paid** → **confirmation** screen. A **receipt email** is sent (R4).
10. Accountant sees the invoice as paid in Ledgerly. **[open question: do we also notify the accountant on pay? PRD open Q2]**

**Outcome:** invoice paid; the primary metric (days sent→paid) is served.

---

## Flow 1 — Pay several invoices in one card payment (R5)

From **Portal home**:
1. Client taps **Select** → each open row gets a checkbox.
2. Client selects 2+ open invoices **in the same currency** **[assumption: cross-currency selection is blocked — see 01-A]**.
   ⤷ If the client taps an invoice in a different currency → it is disabled/blocked with a message
   ("You can pay invoices in one currency at a time"). **[gap]**
3. A sticky bar shows the **running total of the selected invoices** (R5).
4. Client taps **Pay selected** → review shows the total → **Pay by card** → hosted page (R4/R5).
5. On success, **every selected invoice is marked paid** by the one payment (R5) → confirmation lists
   all paid invoices → one receipt email covering all of them **[gap: R4 specifies a receipt for the single-invoice case only]**.

---

## Flow 2 — Pay by bank transfer (R6)

From **invoice detail** or **review**:
1. Client taps **Pay by bank transfer**.
2. Portal shows the firm's **bank details and a payment reference** for the invoice(s) **[gap: R6 has no acceptance criteria — these details are proposed in 03]**.
3. Client makes the transfer in their own bank (outside the portal).
4. Invoice stays **Awaiting bank transfer** (still counts as owed) until a human at the firm confirms
   receipt and marks it paid — PRD Problem: "accountants mark invoices paid by hand." **[gap: who/how/when is undefined; this is a metric risk — see 01-B]**
5. When marked paid, the row flips to **Paid**. **[gap: is a receipt emailed for transfers? undefined]**

**Firm without card payments (the common case — 01-D8):** the portal renders **bank-transfer-only** —
no "Pay by card" button anywhere. Everything else is the same.

---

## Flow 3 — Pay part of an invoice (R8)

Only when **the firm allows partial payment on that invoice** (R8: "when the firm allows it"):
1. On invoice detail, a **Pay part** option appears.
2. Client enters an amount **lower than the invoice total** (R8). **[gap: no minimum defined; overpay/equal not addressed]**
3. Pays by card (hosted page) or bank transfer.
4. On success, the invoice becomes **Partially paid**, showing **amount paid** and **remaining balance**;
   the home total (R3) reflects the remaining balance. **[gap: status name and whether R3 nets partials are undefined]**
5. **[gap: can a partially-paid invoice join a multi-select (R5)? undefined — prototype excludes it, flagged]**

---

## Flow 4 — Download a copy (R7)

From invoice detail (or any row), client taps **Download PDF** → gets a PDF **identical to the one
attached to the invoice email** (R7). Available regardless of paid/unpaid status. This directly serves
PRD Goal 2 (fewer "please resend the invoice" requests).

---

## Unhappy paths (each a designed state — see 04)

| # | Trigger (PRD line or gap) | What the client sees | Recovery |
|---|---|---|---|
| U1 | Link older than 30 days (R1) | **Expired-link page**: "This link has expired." | Button: **Email me a new link** (R1: "request a new one by email") → confirmation that a new link is on the way. **[gap: mechanism undefined]** |
| U2 | Card declined / fails on hosted page (R4) | Returned to portal → **Payment failed**: invoice still open, nothing charged. | **Try again** (card) or **Pay by bank transfer**. |
| U3 | Client abandons the hosted page (R4/R5) | Returns to portal → invoice **still open**, no charge, no error shouted. | Resume from the invoice/selection. |
| U4 | Within the "1 minute" settle window (R4) | **Processing** state on the invoice; actions disabled to avoid double pay. | Auto-updates to Paid; if it stalls, a "still processing" message. **[gap]** |
| U5 | Invoice already paid (e.g. phoned the firm — Risks) while page open | **Already paid** notice; row shows Paid; it drops out of any selection/total. | Nothing owed on it; total recalculates. **[gap: concurrency not in PRD]** |
| U6 | No open invoices (all paid) | **All paid up** empty state; paid history still listed (R2). | Nothing to do. **[gap]** |
| U7 | No invoices at all (new client) | **Nothing here yet** empty state. | — **[gap]** |
| U8 | Cross-currency multi-select attempt (01-A) | Blocked with "one currency at a time." | Deselect the other currency. **[assumption]** |
| U9 | PDF unavailable (R7) | Inline error on download; invoice still viewable/payable. | Retry / contact firm. **[gap]** |

---

## Trust risk from the PRD (Risks section)

> "Clients may not trust a link in an email and phone the firm instead."

Design implication carried into the spec: the portal must look unmistakably like the firm (R10
branding), state what it is in plain words at the top, and show the same invoice number and amount as
the email/PDF so the client can match them. This is a **[suggestion]**, tied to a stated PRD risk.
