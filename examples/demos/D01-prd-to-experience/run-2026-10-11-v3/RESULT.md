# Run demo3b-D01-prd-to-experience

| Field | Value |
|---|---|
| Wall clock | 577 s |
| Turns | 20 |
| Tokens (all, incl. cache) | 1,010,407 |
| Cost reported by the CLI | 2.67919175 |
| Error | False |

## Final message, unedited

Done. Here's the hand back.

---

**RESULT** — Your client payment portal PRD is now a product experience: a gap review, end-to-end flows (happy + unhappy), acceptance criteria for all 10 requirements, a screen/state spec, and a clickable prototype. Six things need your decision before Monday.

All files are in `outputs/2026-10-11-prd-to-experience/`:
- `01-prd-gap-review.md` — 17 gaps, worst first
- `02-user-flows.md` — flows A–E + unhappy paths U1–U5
- `03-acceptance-criteria.md` — testable criteria for R1–R10 (R6 and R10 had empty cells in the PRD; now written)
- `04-screen-state-spec.md` — 9 screens + a state-coverage matrix
- **`prototype/index.html`** — open it in a browser; the left panel jumps to any screen/state for the walkthrough

**ROUTE** — D01 (PRD to product experience). pm skill only; no outside skills, no fallbacks.

**CHECKS** — 39 claims checked by a separate subagent (saw only the PRD, the artifacts, and the draft). 2 corrected, 0 removed — both were in my routing note, not in the work. Every PRD quote, line citation, count, and the metric figures (34 → 25 days) matched the source; the prototype's synthetic totals add up ($2,130 USD + €300; $1,680 selected; $450 remaining). Full table in `06-check.md`.

---

## What design + engineering need from you before Monday

These are the blockers. Design can start Monday on the non-blocked screens in parallel (home, invoice detail, card success/fail, PDF, empty states).

1. **Multi-currency [blocks R3 + R5].** Invoices can be USD/CAD/EUR/GBP (line 28), but R3 says "the total = sum of all open invoices" and R5 says "one payment marks every selected invoice paid." You can't sum or pay across currencies in one go. Confirm: **total shown per currency, and one card payment limited to one currency?** The prototype assumes yes.
2. **Bank transfer [blocks R6].** R6's acceptance cell is empty, and the PRD never says **who marks a transfer invoice paid, or when.** This directly drives your primary metric (days-to-paid). Define what the client sees and how it gets marked paid.
3. **Status list.** The PRD names only Open and Paid (line 35), but due dates imply **Overdue** and R8 implies **Partially paid**. Confirm the full set (proposed: Open, Overdue, Partially paid, Paid, Processing).
4. **Partial-payment rules (R8).** Minimum amount? repeat partials? partial via bank transfer? does the remaining balance count in the total (R3) and can a partial invoice join a multi-select payment (R5)? And how does the client see "the firm allows it"?
5. **Expired-link recovery (R1).** New link automatic or sent by a person, how fast, to which email, and what if the email changed?
6. **Accessibility.** The PRD is silent, yet clients are on phones and R10 puts brand colours on the page. Approve a mobile-first WCAG 2.1 AA baseline (brand colours never dropping below contrast minimums), and confirm the partner's hosted payment page is accessible — we don't control it.

Smaller, from your own open questions: show other firms' invoices? (Q1, proposed no) · notify the accountant on payment? (Q2) · what "Viewed" means in Ledgerly (R9) · the guardrail metric has no baseline (line 47).

**CONFIDENCE: medium** — flows and states are solid; the limiting reason is that six genuine PRD gaps (especially multi-currency and bank transfer) can only be closed by your decisions, and this is the first run of the D01 workflow.

Everything is marked **DRAFT** and all prototype data is **synthetic** — nothing has left this folder. Want me to fold your answers to the six blockers back into the spec and prototype once you have them?
