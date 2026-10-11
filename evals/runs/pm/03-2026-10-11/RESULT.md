# Run pm-golden-03

| Field | Value |
|---|---|
| Wall clock | 106 s |
| Turns | 8 |
| Tokens (all, incl. cache) | 302,576 |
| Cost reported by the CLI | 0.8987114999999999 |
| Error | False |

## Final message, unedited

No problem — I'll give you the most useful thing I can without the data: the exact export spec, so whoever pulls it (you or an analyst) gets it right the first time. Then I'm ready the moment the file lands.

## What to export from Amplitude

**1. The activation metric (the core file)**
- **Chart:** the activation funnel or the "% of new users who activate" segmentation chart you already track.
- **Date range:** 2026-07-01 → 2026-09-30 (Q3). Add the first week of October if you have it, to see whether the drop continued.
- **Granularity:** **weekly** for the full quarter, **plus daily for September** (a daily view is what tells us whether it was a step-change on one date — usually a release — or a gradual slide).
- **Breakdowns (if easy):** by signup source/channel, platform, and new-user cohort. A drop concentrated in one segment points at a very different cause than an across-the-board drop.
- **Export as CSV** with columns: date (week/day start), denominator (new users), numerator (activated users), activation rate. Raw counts matter — a rate can fall because activations dropped *or* because signups spiked.

**2. The activation definition** — one line: what event(s) and what time window count as "activated" (e.g., "completed onboarding + 1 key action within 7 days of signup"). This matters because if the definition changed in Q3, the "drop" could be an artifact, not a real decline. I check this before reading any trend.

**3. The Q3 change/release log** — deploys, onboarding changes, pricing/packaging changes, tracking/SDK updates, major marketing pushes. Dated. This is what I line the drop up against.

Drop those in this folder (or point me to the Google Sheet/Drive file — I can read those). I've saved the framing and blocker to `outputs/2026-10-11-E01/01-frame-and-blocker.md`.

---

RESULT        Blocked before diagnosis — no Amplitude access and no export provided; nothing fabricated · `outputs/2026-10-11-E01/01-frame-and-blocker.md`
ROUTE         E01 (Product analytics to decisions) · pm · no fallback could supply the data
CHECKS        Prerequisite surfaced before any work (PM.md §4, E01 setup): pass — blocker stated before step 1 of the chain. Nothing invented: pass — no numbers or causes in any output.

**NEEDS YOUR JUDGMENT**
1. **How to supply the data** (CSV export / Google Sheet / you want only the spec). I asked; pick whichever is easiest and I'll proceed.
2. **Thursday is tight.** Once I have the three inputs, the brief itself is ~15–30 min. The gap is the export turnaround — if an analyst has to pull it, start that today.
3. **Confirm "activation" means what I assume** — I won't guess the definition; it's the first thing I check, because a definition change in Q3 would make the "drop" partly an artifact.

NEXT ACTIONS  1. You (or analyst): pull the activation export + definition + release log → this folder. 2. Me: run E01 and deliver the decision brief. 3. You: confirm the activation definition.
ASSUMPTIONS   Activation is an onboarding/first-value metric tracked in Amplitude (unconfirmed); the "drop" is month-over-month into September (unconfirmed).
CONFIDENCE    n/a for a diagnosis — none exists yet. High confidence on one thing only: I can't responsibly name a cause without the numbers, and I won't invent them.
