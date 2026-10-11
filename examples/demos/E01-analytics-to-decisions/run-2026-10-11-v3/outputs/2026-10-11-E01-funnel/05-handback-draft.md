DRAFT, not reviewed by a person

# 05 · Hand back (draft, pre-check)

RESULT  Activation fell by about a third (~62%→~42%) from the week of 27 Jul, lining up with release 4.0's
invoice-editor rebuild; the seat "doubling" is mostly the 24 Aug definition change, so bulk invite
can't yet be credited for seat growth. · outputs/2026-10-11-E01-funnel/04-decision-brief.md

ROUTE  E01 (Product analytics to decisions), because you have weekly metrics, definitions and a
release log and need to know what changed, why, and what to do before Tuesday. · Skills run: pm ·
Fallbacks: none (no analytics connector needed; worked only from the exported files, as E01 specifies).

STEPS (all six E01 steps)
1. Restate as a decision — 00-frame.md
2. Check definitions first — 01-definitions-check.md (caught the 24 Aug seats redefinition)
3. Find when movement started vs seasonal — 02-movement-and-causes.md §A, §C (ruled out 29 Jun holiday dip)
4. Line movements up against releases, each cause with evidence + confidence — 02-movement-and-causes.md §D
5. Design the cheapest confirming/killing test — 03-experiment.md (primary + guardrail + stopping rule)
6. Decision brief with success + guardrail metric for the fix — 04-decision-brief.md
No steps skipped.

CHECKS  45 rows / 6 corrected / 0 removed · independent subagent (saw only inputs + brief + handback) · 06-check.md
Corrections: "halved"→"fell by about a third" (×2); "62–66"→"61–66" signups; 13/20 Jul rate shown as 61.9%/62.5%; seats prior range noted as 25–29 with 17 holiday week. All applied.

NEEDS YOUR JUDGMENT
1. Bulk invite ↔ seats is confounded with the 24 Aug definition change; the only clean read is a
   paying-vs-trial seat split for 31 Aug–14 Sep. Confirm you want that pulled before Tuesday.
2. The activation cause (release 4.0) is MEDIUM confidence — a release correlation, not proof.
   Confirm you're comfortable presenting it as a leading hypothesis, with the free cohort read as the test.
3. No context/PRODUCT.md exists, so the "metric leadership watches" and the seat-growth target are
   assumed from your question, not from a stated goal. Confirm which metric the review is actually judged on.

NEXT ACTIONS
1. PM + Felix: run the free pre/post-4.0 cohort read and pull the paying-vs-trial seat split — before Tue 13 Oct.
2. PM: take the decision brief into the review with both answers framed as evidence + confidence.
3. Eng (after cohort read confirms): A/B a one-click default template (03-experiment.md).

ASSUMPTIONS
- The export is complete and final through the week of 14 Sep (stated export date 28 Sep supports this).
- "Within 7 days" activation windows for all shown weeks have closed (they have, given the export date).
- Release dates in release-log.md are the actual ship dates.

CONFIDENCE  Medium — the activation cause is a release correlation, not a proven mechanism; the
definitional read on seats (the other headline) is high confidence.
