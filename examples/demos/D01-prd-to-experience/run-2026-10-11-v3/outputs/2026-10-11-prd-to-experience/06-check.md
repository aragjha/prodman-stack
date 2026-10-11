DRAFT, not reviewed by a person

# 06 · Independent check

Run by a subagent (Agent tool, general-purpose) that saw only: the PRD input file, the artifacts
(01–04 + prototype/index.html), and the handback draft (05). It did not see 00-frame or any notes.
Checker brief given word for word from the pm skill.

**Totals reported by the checker:** 39 rows checked (30 handback + 9 prototype) · 2 failed · 2 corrections.

## Failed rows and how they were resolved

| Row | Claim | Checker verdict | Resolution |
|---|---|---|---|
| 4 | ROUTE: "design + engineering start Monday" | NO — the PRD states no start date; "start Monday" is not in the PRD | The Monday start comes from the **user's request** ("Design and engineering start on Monday"), not the PRD. Reworded in the final handback to attribute it to the request, and to note the weekday is computed (Monday = 2026-10-12, confirmed). |
| 5 | ROUTE: "Skills run: pm only ... No fallbacks used" | NONE — no source in the PRD for this process claim | Not a PRD fact; it is sourced from `workflows/INDEX.md` D01 ("Skills. [pm]"), which the checker was not given. Kept as a process note; accurate. |

## What the checker confirmed holds
- All PRD-source claims matched exactly: requirement numbers; line citations (28, 34–43, 46, 47,
  58, 59); the "R6 and R10 acceptance cells are empty" claim (PRD lines 39, 43); the metric
  figures (34 days, August 2026 → 25 days, end of March 2027, line 46); the currency list order.
- All counts accurate, each counted item stating its own thing: 17 gaps (G1–G17), flows A–E,
  unhappy U1–U5, requirements R1–R10, 9 screens + state matrix.
- Prototype arithmetic internally consistent (synthetic data, no PRD source, as instructed):
  USD $2,130.00 = 1,200 + 480 + 450; EUR €300.00; INV-1070 remaining $450.00 = 650 − 200;
  selected total $1,680.00 = 1,200 + 480. Prototype's PRD-derived labels (30-day expiry, paid
  within 1 minute + receipt, PDF identical to email, last-12-months) all match the PRD.
- Weekday: Monday = 2026-10-12, confirmed by the checker with python3.

## Rubric (PM.md section 7), graded on the final artifact
| Criterion | Pass/fail | Evidence |
|---|---|---|
| Clarity | pass | Flows, criteria and spec each stand alone; gaps cross-referenced by Gn |
| Visual | pass | State-coverage matrix (04) + the clickable prototype make the key points visible fast |
| Concise | pass | One file per step; blockers surfaced up front in the judgment list |
| Decision | pass | Names the six blockers and what each one changes; prototype shows them, not hides them |
| Honesty | pass | Proposed behaviours marked as suggestions; synthetic data labelled; confidence medium with the limiting reason |
| Accuracy | pass | 39 rows, 2 soft failures both resolved; no misquote or miscount of the PRD |
| Artifact checks | pass | Every requirement ends with a testable criterion; error/empty/edge states covered; accessibility addressed; added scope marked (suggestion) |
