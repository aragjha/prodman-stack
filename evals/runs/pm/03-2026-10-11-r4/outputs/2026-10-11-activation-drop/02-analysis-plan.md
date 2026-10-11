DRAFT, not reviewed by a person

# 02 · The E01 diagnosis plan, ready to run the moment the export lands

This is the method, not the answer. It contains no activation numbers because none were provided; every
value below is a placeholder to fill from your export. Following E01's six steps:

**What to export from Amplitude (three files, drop them in this run folder):**
1. Weekly (or daily) activation rate for Q3 2026 — Jul, Aug, Sep — ideally with the two weeks either
   side, and the numerator and denominator, not just the percentage. New-account cohort by week is best.
2. The activation metric + event definition: what event marks "activated", over what window, with what
   threshold — and whether any of that changed in Q3.
3. The Q3 release / change log: product releases, pricing/packaging changes, onboarding changes,
   acquisition-channel or campaign changes, and any tracking/instrumentation changes.

**Step 1 — Restate as a decision.** What will the VP do differently depending on the answer? (e.g. roll
back a release, fund an onboarding fix, or accept it as seasonal and move on.)

**Step 2 — Check definitions first.** Did "activated" change meaning in Q3 (event, window, threshold)?
Did any instrumentation/SDK change drop or double-count the activation event? A definition or tracking
change is the single most common way a "drop" is an artifact, not a real decline — rule it in or out
before reading the curve as a trend.

**Step 3 — Date the movement and separate seasonality.** Find the exact week activation turned down.
Compare September against the same weeks in prior quarters/years to tell a real drop from a normal
late-summer / back-to-school dip. Flag small weekly numbers rather than over-reading them.

**Step 4 — Line the drop up against changes.** Put the dated drop next to the release log. For each
candidate cause (a specific release, a pricing change, a channel-mix shift bringing lower-intent signups,
a tracking change), state the evidence and a confidence tag (HIGH/MEDIUM/ZERO per PM.md §3).
Correlation with a release is a lead, not proof.

**Step 5 — Design the cheapest test** that confirms or kills the leading cause (e.g. segment activation
by signup source or by exposure to the suspected release; or a holdback/rollback on the suspected
change). Name a primary metric, a guardrail metric, and a stopping rule.

**Step 6 — Write the one-page decision brief** (PM.md §5 shape): the dated drop · recommendation ·
three strongest pieces of evidence with confidence tags · what would reverse the call · risks · next
step, owner and date.

**Timeline:** with the three files in hand, this is a 15–30 minute run — comfortably before Thursday
2026-10-15.
