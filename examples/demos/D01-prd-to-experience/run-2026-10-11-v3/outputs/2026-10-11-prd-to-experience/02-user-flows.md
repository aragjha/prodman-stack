DRAFT, not reviewed by a person

# 02 · User flows — invoice email to paid invoice

Primary actor: the **Client** (owner or bookkeeper of a small business, no Ledgerly login, often on
a phone — PRD line 23). Each flow lists the happy path and the unhappy paths. Steps trace to PRD
requirements (R1–R10) and to the gaps in `01-prd-gap-review.md` (Gn). Where a gap blocks a path, the
step is marked **[BLOCKED: Gn]** and shown as the proposed behaviour pending Maya's decision.

## Flow A · The main path: email → portal → pay by card → paid

1. Client receives the invoice email (R1, line 34). Email contains the invoice PDF attachment
   (R7, line 40) and a link to the portal.
2. Client taps the link on their phone. Portal opens with **no password** (R1; non-goal line 15).
3. Portal loads: firm logo and brand colours at top (R10, line 43), total owed (R3, line 36), open
   invoices first by due date, then paid invoices from the last 12 months (R2, line 35).
   - This view is what the accountant sees as "Viewed" in Ledgerly (R9, line 42) — **[G12]** exact
     trigger (portal-open vs invoice-open) to confirm.
4. Client taps an open invoice to see its detail, or selects it from the list.
5. Client taps **Pay by card**.
6. Client is taken to the payments partner's **hosted page** (R4, line 37; Context line 29).
7. Client enters card details on the hosted page and confirms.
8. On success, client returns to the portal to a **payment success** state; the invoice is marked
   paid within 1 minute (R4) and a **receipt email** is sent (R4).
9. The paid invoice moves to the paid section; the total owed decreases (R3).

## Flow B · Pay several invoices in one card payment (R5, line 38)

1–3. As Flow A, steps 1–3.
4. Client taps **Select** and ticks several open invoices.
   - **[BLOCKED: G1]** If the selected invoices are in different currencies, a single card payment
     cannot cover them. Proposed: selection is limited to one currency at a time; the total shown is
     per currency. Confirm with Maya.
5. Portal shows the **total of the selected invoices before payment** (R5).
6. Client taps **Pay selected by card** → partner hosted page (R4/R5).
7. On success, **one payment marks every selected invoice paid** (R5); one receipt email covering
   all selected invoices — **[G10]** receipt contents to confirm.

## Flow C · Pay by bank transfer (R6, line 39) — DRAFT, see G2

1–4. As Flow A.
5. Client taps **Pay by bank transfer**.
6. **[BLOCKED: G2]** Proposed: portal shows the firm's bank details and a **payment reference** to
   quote. The invoice stays **Open** (or a new "Awaiting transfer" state — see G3) until the payment
   is reconciled. Who marks it paid, and when, is undefined in the PRD and must be decided before
   this flow can be built.
7. Client makes the transfer in their own bank; returns later to see status update once reconciled.

## Flow D · Pay part of an invoice (R8, line 41) — where the firm allows it

1–4. As Flow A; the invoice detail shows a **Pay part** option only if the firm allows partial
   payment for it — **[G4]** how "the firm allows it" is surfaced to confirm.
5. Client enters an amount **lower than the invoice total** (R8).
6. Pays that amount by card (R4) — **[G4]** confirm whether partial by bank transfer is allowed.
7. Invoice becomes **Partially paid** with a remaining balance — **[BLOCKED: G3/G4]** this status
   and how it affects the total owed (R3) and multi-select (R5) are not defined in the PRD.

## Flow E · Download an invoice as a PDF (R7, line 40)

1–4. As Flow A.
5. Client taps **Download PDF** on any invoice; the file is **identical to the PDF attached to the
   invoice email** (R7).
   - **[G11]** confirm available for paid invoices too, and the behaviour if the PDF is missing.

## Unhappy paths

### U1 · Expired link (R1, line 34)
- Link older than 30 days → **expired-link** screen. Client can **request a new one by email** (R1).
- **[G5]** Proposed: a "Send me a new link" action confirms the email the invoice was sent to and
  shows a "check your email" state. Whether the new link is automatic or needs a person, how fast,
  and what happens if the email changed, are undefined and need Maya's decision.

### U2 · Card payment fails or is abandoned (R4, line 37) — **[G9]**
- **Declined:** client returns from the hosted page to a **payment-failed** state; the invoice stays
  Open; client can retry or choose another method.
- **Abandoned:** client closes the hosted page without paying → returns to the portal with the
  invoice still Open; no receipt.
- **Result not yet confirmed:** client returns before the "paid within 1 minute" confirmation lands
  → a **processing** state, not a success or a failure, until confirmed.
- **Already paid / double payment:** invoice was paid in another tab or by another person at the firm
  → client sees it is already paid and is not charged again.
- All four are proposed behaviours; the PRD specifies only the success path, so these need sign-off.

### U3 · Nothing to pay / empty states (R2, line 35) — **[G8]**
- Client has **no open invoices** (all paid): portal shows an "all paid" state and the paid history.
- Client has **nothing at all** at this firm: portal shows an empty state explaining the link is
  valid but there is nothing outstanding.
- Client has **more than 12 months** of paid invoices: history is limited to 12 months (R2) — confirm
  whether older ones are reachable.

### U4 · Trust hesitation (Risk, line 54)
- "Clients may not trust a link in an email and phone the firm instead." Design response
  **(suggestion):** show the firm's name and branding (R10) prominently, state plainly what the page
  is and that no login is needed, and show the firm's contact so the client can verify by phone and
  still return to pay.

### U5 · Mixed currencies in one view (Context line 28) — **[BLOCKED: G1]**
- A client with open invoices in more than one currency: the total owed (R3) is shown **per currency**
  (proposed), and multi-select (R5) is limited to one currency per payment. Needs Maya's decision.

## Flow map (text)

```
Invoice email ──tap link──▶ [Link valid?] ──no──▶ Expired-link screen ──request──▶ "Check email" (U1/G5)
                                 │ yes
                                 ▼
                          Portal home (R2,R3,R10) ──▶ accountant sees "Viewed" (R9/G12)
                                 │
         ┌───────────────┬───────┴───────┬──────────────┬─────────────┐
         ▼               ▼               ▼              ▼             ▼
  Invoice detail   Select several    Download PDF   (empty/all-paid)  Bank transfer
   │   │   │        (R5, one ccy)      (R7/G11)        states (U3)     (R6, DRAFT G2)
   │   │   └─Pay part (R8/G4)                                            │
   │   └─────Pay by card (R4)                                     show bank details+ref
   ▼                                                               invoice stays Open
 Partner hosted page ──success──▶ Success + receipt (R4) ──▶ invoice Paid, total drops
         │
         ├─declined──▶ Payment-failed (retry / other method)   ┐
         ├─abandoned─▶ back to portal, still Open               ├ U2 / G9
         └─no result─▶ Processing state                         ┘
```
