DRAFT, not reviewed by a person

# 01 · Route and prerequisite check

**Routing to E01 (Product analytics to decisions),** because the decision is "a metric moved, someone
senior wants to know why by Thursday" — an exact match to this workflow's problem statement. Skills
run: pm (this repo) only.

## Prerequisites E01 requires (INDEX.md "You need")
1. The metrics as a table or export (weekly or daily).
2. The event and metric definitions.
3. The release log / list of changes in the period.

E01 Setup note, quoted: "without an analytics connector it works only from what you export."
E01 Limits, quoted: "it cannot query your analytics tool unless you connect it."

## What is missing, what it blocks, the fallback
| Required input | Status | Blocks | Fallback |
|---|---|---|---|
| Amplitude connector | **Not configured** in this workspace | Pulling "last quarter's activation numbers" directly, as the request asks | Work only from a file you export; I cannot connect to Amplitude for you |
| Weekly/daily activation export (Q3: Jul–Sep 2026) | **Not provided** | The entire diagnosis — there are no numbers to date the drop or size it | You export from Amplitude and drop the file in this run folder |
| Metric + event definition ("what counts as activated") | **Not provided** | Step 2: ruling out a definition change being read as a trend | You paste the activation definition and any change to it in Q3 |
| Release log / change list for Q3 | **Not provided** | Step 4: lining the drop up against releases to name candidate causes | You export or paste the Q3 release/change log |

**Conclusion: the run is blocked on its core inputs before step 2.** The request assumes I can pull from Amplitude; I cannot — no connector exists here, and nothing was attached. Per PM.md principle 6 ("Unknown is a valid answer. Invented is not.") I will not fill these with plausible numbers, and I will not use
the repo's synthetic demo data (examples/demos/E01-...) as if it were your real Amplitude figures.

The smallest action that unblocks this: export the three files above from Amplitude and point me at the
folder. With them, E01 is a 15–30 minute run and well inside the Thursday deadline.
