DRAFT, not reviewed by a person

RESULT Blocked before analysis: I cannot answer why activation dropped in September because there is no Amplitude connector here and no data was attached — so there are no numbers to
              diagnose. I will not invent them. What's needed to unblock, plus a ready-to-run plan, is in
              outputs/2026-10-11-activation-drop/ (01-route.md, 02-analysis-plan.md).

ROUTE E01 (Product analytics to decisions), because the decision is "a metric moved, someone
              senior wants to know why by Thursday" — an exact match. · Skills run: pm · Fallbacks: none
              reached; the run stops at the missing-input checkpoint before the chain runs.

STEPS E01 step 1 (restate as a decision): done · 00-frame.md
              E01 step 2 (check definitions first): skipped — no metric definition provided
              E01 step 3 (date the drop, separate seasonality): skipped — no metrics export provided
              E01 step 4 (line up against releases): skipped — no release log provided
              E01 step 5 (design the test): skipped — depends on a leading cause from steps 2–4
              E01 step 6 (decision brief): skipped — no evidence to brief on
              (The method for all six is laid out ready-to-run in 02-analysis-plan.md.)

CHECKS {{CHECKS}}

NEEDS YOUR JUDGMENT
              1. Data source (BLOCKING). There is no Amplitude connector in this workspace and I cannot
                 configure or authenticate one for you. To proceed I need three files exported and dropped
                 in this folder: the weekly/daily activation table for Q3, the activation metric/event
                 definition, and the Q3 release log. (See 01-route.md and 02-analysis-plan.md.)
              2. Definition change — rule it out first. Before any number is read as a real drop, confirm
                 whether "activated" changed meaning in Q3 (event, window, threshold) or whether any
                 tracking/instrumentation change affected the event. This is the most common false "drop".
              3. Scope of "last quarter". I've assumed Q3 2026 (Jul–Sep). Confirm, especially if your
                 fiscal quarters don't follow the calendar.
              4. What the VP will act on. Knowing whether the answer feeds a rollback, an onboarding
                 investment, or an "it's seasonal, move on" call will sharpen step 1 and the eventual test.

NEXT ACTIONS 1. You (or someone with Amplitude access): export the three files above and drop them in
                 outputs/2026-10-11-activation-drop/, then tell me to run E01. — owner: you
              2. Me, on receiving the files: run E01 steps 2–6 and produce the one-page decision brief
                 (15–30 min, before Thursday 2026-10-15). — owner: me
              3. You: confirm the activation definition and whether it changed in Q3. — owner: you

ASSUMPTIONS - "Last quarter" = Q3 2026 (Jul–Sep 2026); "Thursday" = 2026-10-15.
              - "Our Amplitude" implies a live analytics source I should query; I have no connector to it
                and none was provided, so I treated the run as export-only per E01's setup note.

CONFIDENCE high — that the run is correctly blocked on inputs. The limiting reason: zero activation
              data of any kind was available, and inventing it (or substituting the repo's synthetic demo numbers) would be a defect under PM.md principle 6, not an answer.
