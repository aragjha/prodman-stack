DRAFT, not reviewed by a person

RESULT        Blocked, not diagnosed: there is no Amplitude connector in this session and no data
              was provided, so I cannot pull September's activation numbers or explain the drop
              without inventing them. I've framed the decision and listed the exact export that
              unblocks a same-day diagnosis · outputs/2026-10-11-activation-drop/01-prerequisites.md

ROUTE         E01 · Product analytics to decisions, because it matches E01's stated problem — which
              reads, exactly: "A metric moved, someone senior wants to know why by Thursday, and the
              dashboard shows what happened but not why or what to do." · skills run: pm (routing
              and framing only; the E01 chain did not run for lack of inputs) · fallbacks: none

STEPS         E01 lists six steps; none could run without the data:
              1. Restate as a decision — done (00-frame.md)
              2. Check definitions for a change in the period — blocked (no definitions provided)
              3. Find when the drop started, separate from seasonality — blocked (no metrics export)
              4. Line the drop up against releases, rank causes — blocked (no metrics, no release log)
              5. Design the cheapest confirming test — blocked (depends on a leading cause from step 4)
              6. Write the decision brief with success + guardrail metric — blocked (depends on 2–5)

CHECKS        27 rows, 2 corrected, 0 removed · independent pass (subagent, saw only inputs + artifacts) · 03-check.md
              Decision first | pass | 00-frame.md written before any artifact
              Route named | pass | E01, an ID in workflows/INDEX.md
              Prerequisites surfaced | pass | 01-prerequisites.md names every missing input and connector before the chain
              Nothing invented | pass | no activation number, cause or date is asserted

NEEDS YOUR JUDGMENT
              1. The deadline is tight and the diagnosis cannot start until data lands. "By Thursday"
                 named no date; I read it as Thu 2026-10-15 (today is Sun 2026-10-11). Confirm, and
                 note that the brief needs the export in hand with a day or two to spare.
              2. "Activation" is undefined here. Its meaning (which event, what window, what
                 denominator) decides the whole analysis — send the definition, not just the chart.
              3. If you have an Amplitude connector/MCP you expect me to use, it is not present in
                 this session. If one exists, connect it; otherwise the export route is the only path.

NEXT ACTIONS  1. You: export the three items in 01-prerequisites.md (weekly activation Jul–Sep + a
                 baseline, the activation definition, a Jul–Sep release log) into this folder — owner: you.
              2. Me: on receipt, run the full E01 chain and return the one-page decision brief — owner: me.
              3. You: confirm the Thursday date and who the VP is, so the brief is addressed right — owner: you.

ASSUMPTIONS   "By Thursday" = 2026-10-15. "Last quarter" = Q3 2026 (Jul–Sep). The VP wants a causal
              explanation plus a recommendation, not just the chart. The activation metric lives in
              Amplitude as stated.

CONFIDENCE    high — not in any diagnosis (there is none yet), but in the call to stop: with no
              connector and no data, the only honest output is the exact ask that unblocks it.
