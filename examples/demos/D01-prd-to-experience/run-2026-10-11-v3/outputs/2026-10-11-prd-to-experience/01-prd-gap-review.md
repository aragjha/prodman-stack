DRAFT, not reviewed by a person

# 01 · PRD gap review — client payment portal

Source: `examples/demos/D01-prd-to-experience/input/prd-client-portal.md` (draft v0.2, SYNTHETIC),
read 2026-10-11. Each gap cites the PRD line it comes from. Nothing here is added to scope; items
marked **[suggestion]** are proposals for Maya to accept or decline.

## A. The blocker: multi-currency breaks two requirements

This is the one gap that should be settled before design opens a file, because it changes core screens.

> Context: "Firms can issue invoices in USD, CAD, EUR and GBP, and a client's invoices can be in any of these."

> R3 acceptance: "The total equals the sum of all open invoices."

> R5 acceptance: "The total of the selected invoices is shown before payment. One payment marks every selected invoice paid."

**Conflict.** A client can hold invoices in several currencies, but R3 asks for a single total and
R5 asks for one card payment across selected invoices. You cannot add USD to EUR into one number,
and a card charge is in one currency. As written, R3 and R5 are undefined for the mixed-currency
client — which the Context says is possible.

**Shown both ways (a person decides — see judgment list):**
- **Plan A — group by currency.** The total (R3) is shown per currency ("You owe $1,200 USD and
  €800 EUR"). Multi-select (R5) is allowed only within one currency; selecting across currencies is
  blocked with a message. Simplest to reason about; more screens.
- **Plan B — single-currency portal per link.** Each invoice email/link covers one currency, so the
  portal only ever shows one. Simplest UI; needs the email/link logic to split by currency, and a
  client with two currencies gets two links.

The prototype (`prototype/`) is built on **Plan A** so the team can see the harder case; it is
labelled as an assumption, not a decision.

## B. Requirements with no acceptance criteria (PRD leaves these blank)

| # | Requirement (quoted) | What's missing |
|---|---|---|
| R6 | "The client can pay by bank transfer" — acceptance cell is **empty** | No definition of what the client sees (bank details? a reference?), and — critically — **how the invoice gets marked paid.** Bank transfers don't auto-reconcile, so the invoice stays open until a human confirms it. The PRD's own Problem says "accountants mark invoices paid by hand." If that persists for transfers, those invoices may never hit "paid" promptly, which drags the **primary metric** (days to paid). Draft criteria proposed in `03-acceptance-criteria.md`. |
| R10 | "The portal shows the firm's logo and brand colours" — acceptance cell is **empty** | No source for logo/colours (firm admin uploads per User table?), no fallback when unset, no size limits, and no contrast rule — arbitrary brand colours can fail accessibility (see section E). Draft criteria in `03`. |

## C. Thin or ambiguous acceptance criteria

| # | Line (quoted) | Ambiguity |
|---|---|---|
| R1 | "On an expired link, the client can request a new one by email" | By what mechanism? A button on the expired-link page, or they reply to the original email? Who receives the request and how fast is the new link sent? The expired-link page needs its own designed state. |
| R4 | "the invoice is marked paid within 1 minute" | What does the client see during that minute? A pending/processing state is implied but not specified. Also undefined: card payment **failure** and **abandonment** on the partner's hosted page. |
| R5 | "One payment marks every selected invoice paid" | Partial failure is undefined. A single hosted-page charge is all-or-nothing, so this is probably fine — but it should be stated. Also: can a **partially-paid** invoice (R8) be included in a multi-select? Undefined. |
| R8 | "The client can enter an amount lower than the invoice total" | No minimum, no rule against overpaying, no defined status after a partial payment ("partially paid"?), and no statement of whether R3's total then shows the **remaining balance**. Interaction of R8 with R5 (multi-select) is undefined. |
| R9 | "the invoice list in Ledgerly shows 'Viewed' with the date and time" | "Viewed" = opened the portal, or opened **that specific** invoice? First view or most recent? Lives in Ledgerly (the firm app), so it is out of the portal UI but still needs a trigger defined. |

## D. Missing states and edge cases (no PRD line — these are gaps, flagged as such)

The PRD describes happy paths only. Design needs these states or they surface in review/production:

1. **Empty — no invoices at all** (new client). R2 lists invoices; says nothing about zero.
2. **Empty — nothing owed** (all paid). R3 shows a total; says nothing about a zero total ("You're
   all paid up").
3. **Payment failed / card declined** on the hosted page (R4). No defined return state.
4. **Payment abandoned** — client closes the hosted page and returns (R4/R5).
5. **Payment pending/processing** — the gap during the "within 1 minute" (R4).
6. **Already paid elsewhere** — an invoice is paid (or chased by phone, per Risks) while the client
   has the page open. Concurrency / stale list.
7. **Expired link page** (R1) — its own screen, with the "request a new one" action.
8. **Firm without card payments** — Risks says these firms "can only offer bank transfer." The
   portal must render a bank-transfer-only variant. Context: "Fewer than 50 firms have card payments
   turned on," so most firms are in this variant.
9. **Receipt coverage** — R4 emails a receipt for a single card payment. Undefined: receipt for a
   **multi-invoice** payment (R5), a **partial** payment (R8), and a **bank transfer** (R6).
10. **PDF unavailable** — R7 assumes the PDF exists; no fallback state.

## E. Accessibility — absent from the PRD entirely

The PRD has no accessibility section, yet the User table says the client "Often reads the invoice
email on a phone," and this is a **payment** flow (high stakes, must be operable by everyone).
**[suggestion]** Treat these as requirements, not nice-to-haves:
- Target **WCAG 2.2 AA**. Full notes and per-screen criteria in `03-acceptance-criteria.md` and `04-screen-state-spec.md`.
- **R10 brand colours must pass contrast.** Arbitrary firm colours can fail AA against text/buttons;
  need an enforced minimum contrast or an automatic accessible fallback for interactive elements.
- **Mobile-first**: the client reads on a phone; the whole flow must work one-handed, with targets
  ≥ 44px and no reliance on hover.
- The payment and selection controls must be fully **keyboard and screen-reader** operable; money
  amounts and currency must be announced, not conveyed by colour alone (status badges).

## F. Scope and metric notes (not blockers, but flag before Monday)

- **Guardrail baseline is unknown.** PRD: "Guardrail: support tickets about payments, per 100 firms
  per month. Baseline: unknown." Can't tell if the portal makes support better or worse without it.
  Cheapest fix: pull the last 1–2 months of payment-related ticket counts before beta.
- **Two open questions in the PRD are still open** (other-firm invoices; notify accountant on pay).
  Both touch the UI; carried into `05-open-questions`.
- **Bank-transfer-only is the common case** (see D8); the "less value" Risk is really the default
  experience for most firms, not an edge. Worth deciding how much to invest in that variant now.
