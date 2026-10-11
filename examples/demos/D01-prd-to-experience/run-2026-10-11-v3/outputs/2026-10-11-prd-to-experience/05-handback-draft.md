DRAFT, not reviewed by a person

# 05 · Hand back (draft, pre-check)

```
RESULT   The client payment portal PRD is turned into a product experience: a gap review, end-to-end
         flows with unhappy paths, acceptance criteria for all 10 requirements, a screen/state spec,
         and a clickable prototype. Six blockers must be decided before Monday.
         Files: outputs/2026-10-11-prd-to-experience/ (01 gap review, 02 flows, 03 acceptance
         criteria, 04 screen & state spec, prototype/index.html).

ROUTE    D01, PRD to product experience, because a PRD exists and (per your request) design +
         engineering start Monday 2026-10-12 and need the flows, states and a walkthrough. The
         Monday start is from your request, not the PRD; the weekday is computed (today Sunday
         2026-10-11). Skills run: pm only (workflows/INDEX.md lists D01 as pm only). No fallbacks used.

STEPS    (the five D01 steps)
         1. Review the PRD for gaps        — done, 01-prd-gap-review.md (17 gaps, G1–G17)
         2. Write the user flows incl.
            unhappy paths                  — done, 02-user-flows.md (flows A–E, unhappy U1–U5)
         3. Acceptance criteria for every
            requirement lacking one        — done, 03-acceptance-criteria.md (R1–R10; R6 and R10
                                             had empty cells in the PRD and are now written)
         4. Prototype-ready screen/state
            specification                  — done, 04-screen-state-spec.md (9 screens + state matrix)
         5. Questions only the owner can
            answer                         — done, "Needs your judgment" below
         Plus the requested clickable prototype — done, prototype/index.html (synthetic, DRAFT).

CHECKS   39 rows, 2 corrected, 0 removed · checked by a subagent that saw only the PRD, the
         artifacts and this draft · 06-check.md. Both corrections were in this ROUTE block (the
         "Monday start" now attributed to your request; the "pm only" note sourced to the workflow
         index). All PRD quotes, line citations, counts and metric figures matched the source; the
         prototype's synthetic totals are internally consistent. Rubric: all five criteria pass,
         accuracy pass — table in 06-check.md.

NEEDS YOUR JUDGMENT (what design + engineering need from you before Monday 2026-10-12)
These are the blockers. Each is a decision only you (Maya) can make; design can start on the
non-blocked screens in parallel.
1. **Multi-currency [G1, blocks R3 + R5].** A client's open invoices can be in USD, CAD, EUR, GBP
   (PRD line 28). Confirm: show the total owed per currency, and limit one card payment to one
   currency? The prototype assumes yes — the top of the portal and the whole multi-select flow
   depend on your answer.
2. **Bank transfer [G2, blocks R6].** The PRD's acceptance cell for R6 is empty and never says who
   marks a bank-transfer invoice paid, or when. This drives the primary metric (days to paid,
   line 46). Define what the client sees and how/when the invoice is marked paid.
3. **Status taxonomy [G3].** Confirm the full set of statuses a row can show. The PRD names only
   Open and Paid (line 35), but due dates imply Overdue and R8 implies Partially paid. Proposed:
   Open, Overdue, Partially paid, Paid, Processing.
4. **Partial payment rules [G4, R8].** Minimum amount? repeat partials? partial by bank transfer?
   does the remaining balance count in the total owed (R3) and can a partial invoice join a
   multi-select payment (R5)? And how is "the firm allows it" surfaced to the client?
5. **Expired-link recovery [G5, R1].** Is the new link automatic or sent by a person, how fast, to
   which email, and what if the email changed?
6. **Accessibility [G6].** The PRD is silent. Approve a mobile-first, WCAG 2.1 AA baseline (incl.
   brand colours never dropping below contrast minimums), and confirm the partner's hosted payment
   page meets accessibility needs — we don't control it.
Also decide (smaller, from the PRD's own open questions): show other firms' invoices? (Open Q1,
line 58, proposed no) · notify the accountant on payment? (Open Q2, line 59) · what "Viewed" means
in Ledgerly (G12, R9) · guardrail metric has no baseline (line 47, G17).

NEXT ACTIONS
1. Maya: answer the six blockers above (and ideally the four smaller ones) before Monday — owner: Maya.
2. Maya + Lena (design): walk the prototype (prototype/index.html) with the team on Monday using
   this spec; start design on the non-blocked screens (home, invoice detail, card success/fail,
   PDF, empty states) — owner: Lena.
3. Eng: confirm two dependencies before building — the payments partner's hosted-page return
   behaviour (success/decline/abandon/webhook timing) and its accessibility — owner: Squad A.

ASSUMPTIONS
- Working from the PRD alone; no context/PRODUCT.md, DECISIONS.md or CORRECTIONS.md exist (templates
  only), so product context beyond the PRD is unknown.
- The prototype is a low-fidelity structure/flow walkthrough, not visual design (D01 produces a spec,
  not designs). All its data is synthetic.
- Proposed behaviours for undefined paths (errors, empty states, statuses) are suggestions, marked as
  such; they are not in the PRD.

CONFIDENCE  medium — the flows and states are solid, but six PRD gaps (esp. multi-currency and bank
            transfer) are genuine unknowns that only your decisions can close, and this is the first
            run of the D01 workflow (untested).
```
