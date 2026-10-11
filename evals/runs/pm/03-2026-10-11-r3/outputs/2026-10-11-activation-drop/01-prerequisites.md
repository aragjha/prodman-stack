DRAFT, not reviewed by a person

# 01 · Prerequisites — what blocks the run, and what unblocks it

**Route:** E01 · Product analytics to decisions (workflows/INDEX.md). Picked because the decision
is "why did a metric move, and what do we do," with a senior deadline — E01's exact problem.

## What E01 requires vs. what is in hand

| E01 needs | In hand? | What it blocks |
|---|---|---|
| The metrics as a table/export (weekly or daily) | **No** | The whole diagnosis. I cannot find when the drop started or size it without the numbers. |
| The event and metric definitions | **No** | Step 2 — ruling out a definition change that only *looks* like a drop. |
| The release log / list of changes for the period | **No** | Step 4 — lining the drop up against releases to name candidate causes. |

## Why I cannot "pull from Amplitude" myself

There is no Amplitude connector in this session (I checked the available tools). I have no login,
no API access, and no export. PM.md §4 and the pm skill both say: a missing connector means I work
only from data you provide, and I say so before starting rather than fill the gap. So I am stopping
here instead of producing activation numbers — any September figure I wrote would be invented, and
an invented number that looks right is the exact failure this repo's standards are built to prevent
(PM.md §3, §6).

## The smallest export that unblocks the full E01 diagnosis

From Amplitude, export and drop into this folder (CSV or pasted table):

1. **Activation, weekly, last quarter + a baseline run-up.** Jul–Sep 2026 at minimum; ideally back
   to ~Apr 2026 so September has something to compare against and seasonality is visible. One row
   per week: week-start date, numerator (activated users), denominator (eligible/new users), rate.
   Daily for September too, if easy — it pins the day the drop started.
2. **The activation definition.** What event(s) count as "activated," within what window, over what
   denominator — and whether that definition changed at any point in the quarter (a redefinition can
   masquerade as a drop).
3. **A release / change log for Jul–Sep 2026.** Shipped features, experiments turned on, pricing or
   onboarding changes, tracking/SDK changes, known outages. Dates matter most.

Optional but sharpens it: activation split by signup source, platform, or new-vs-returning;
`context/PRODUCT.md` filled in (product, users, the metric's owner).

## Fallback if you cannot export cleanly

Paste whatever you have — even a screenshot of the weekly chart with the axis values, or the raw
weekly numbers in chat. I will work only from that and label any gap "unknown" rather than fill it.
