# Run demo-D01-prd-to-experience

| Field | Value |
|---|---|
| Wall clock | 419 s |
| Turns | 20 |
| Tokens (all, incl. cache) | 956,713 |
| Cost reported by the CLI | 1.755248 |
| Error | False |

## Final message, unedited

All files are in place. Here's the handback.

```
RESULT  The client payment portal PRD is now a full product experience — gap review, end-to-end
        flows (happy + unhappy), acceptance criteria, a screen/state spec, and a clickable
        prototype — plus the 9 decisions you owe design/eng before Monday.
        · outputs/2026-10-11-prd-to-experience/

ROUTE   D01 (PRD to product experience) · skill run: pm · no fallbacks ·
        step added beyond D01: a low-fi clickable HTML prototype (D01 normally stops at the spec)

CHECKS  21 claims checked against the PRD, 1 fixed (a pluralised quote), 0 removed; all hold or are
        labelled [proposed]/synthetic · outputs/.../06-check.md
        Acceptance criteria on every requirement | pass | R6 & R10 blanks filled in 03
        Gaps cite PRD lines | pass | 01 cites lines 7,17,23,28–43,54,59
        Error/empty/edge states | pass | 04 covers declined, timeout, abandoned, expired, pending, empty
        Accessibility | pass | 01-D + 04 cross-cutting
        Nothing added without a suggestion tag | pass | all additions marked [proposed]
        Accuracy per claim | pass | 06 Part A
```

**What I built (in `outputs/2026-10-11-prd-to-experience/`)**
- `01-prd-gap-review.md` — the gaps, each tied to a PRD line
- `02-user-flows.md` — 7 flows, email → paid, with the unhappy paths
- `03-acceptance-criteria.md` — fills the two blank requirements (R6, R10) + edge states
- `04-screen-state-spec.md` — every screen (S0–S7), every state, empty + error
- `prototype/index.html` — **open in any browser**; walk S1 → pay → confirmation, plus empty, bank-only, declined, timeout, expired, partial. No build needed.
- `05-open-questions.md` — what you owe the team before Monday

**NEEDS YOUR JUDGMENT** (full list + ordering in `05`; the top ones block screen layout and the data model)
1. **Multi-currency.** R3 ("sum of all open invoices," line 36) and R5 ("one payment," line 38) collide with four currencies (line 28). You can't sum or charge across currencies — I spec'd **subtotal-per-currency + one-currency-per-payment** and need your yes. This reshapes the home screen.
2. **Invoice statuses.** R2 names only Open/Paid (line 35); the flows need **Overdue, Partially paid, Payment pending** too. Confirm the set.
3. **Bank transfer (R6 has no criteria, line 39).** I spec'd it as **manual, with a "Payment pending" state** — because accountants "mark invoices paid by hand" (line 7) and R4's 1-minute auto-paid is card-only (line 37). Confirm.
4. **Partial payment (R8):** minimum amount? resulting status? allowed in multi-select?
5. Plus: who sends the new link on expiry (vs the auto-reminders non-goal), link scope, what "Viewed" means (R9), receipts for bank/multi-pay, and the PRD's own open Q2 (notify accountant on payment?).

**NEXT ACTIONS**
1. Maya — answer the 4 "must" questions in `05` today; they're the ones that change screens. (owner: you)
2. Maya — walk the team through `prototype/index.html` Monday AM using the README's script. (owner: you)
3. Eng — confirm the payments partner's return URLs/statuses for the S3 unhappy paths. (owner: eng lead)

**ASSUMPTIONS** — non-interactive run, so I worked from the PRD alone (no `context/PRODUCT.md`); the prototype is low-fi grey-box with synthetic data, not visual design; the 4.5:1 contrast floor is my proposal, not a PRD fact.

**CONFIDENCE** — Medium. The one thing limiting it: four of the key behaviours (currency totals, status set, bank-transfer handling, partial rules) aren't decided in the PRD, so the spec shows them as recommendations until you confirm — and with design starting tomorrow, those answers are the critical path.

One timing flag worth saying plainly: **today is Sunday the 11th and "Monday" is tomorrow, the 12th** — so the window to answer the four blocking questions is effectively today.
