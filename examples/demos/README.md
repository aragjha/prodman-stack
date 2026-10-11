# Flagship demos

Five real runs of the `pm` skill on five product management problems, each in a fresh Claude Code
session with no access to anything but its own inputs. Every output is saved unedited, and each run
was graded by a separate reviewer who did not write the skill or the inputs and who had an answer key
the run never saw.

**The inputs are synthetic.** They describe Ledgerly, a made up invoicing tool for small accounting
firms, and every input file says so on its first line. The problems planted in them (contradictions,
stale documents, a misleading metric, a breaking change) are listed in answer keys kept outside this
repo until the runs were graded.

## Results, versions 2 and 3 of the skill, 2026-10-11
"Key" is how many of the answer key's criteria the run met: the planted problems found and handled.
"Checks" are the skill's own eight checks. Every run failed overall; the table says how.

| Demo | What the PM asked | Version 2 | Version 3 | What changed |
|---|---|---|---|---|
| [A01 document chaos](A01-document-chaos/) | 15 messy documents: what did we agree, what conflicts, what to build first | Key 9 of 10, checks 6 of 8 | Key 8 of 10, checks 5 of 8, 1 red flag | Checked far more quotes (67 of 74, against 13 of 35), but turned a spoken promise into "a written commitment" and called the CEO's date reachable by cutting scope |
| [C01 idea to roadmap](C01-idea-to-roadmap/) | A rough idea into a roadmap two squads can deliver, with competitor research | Key 7 of 10, checks 6 of 8, 1 red flag; 13 of 16 web claims on their pages | Key 7 of 10, checks 6 of 8, 1 red flag; 7 of 14 web claims on their pages | Worse on the web: claims from search summaries, and "nobody prices this per seat" against its own source |
| [D01 PRD to experience](D01-prd-to-experience/) | A PRD into flows, states and a clickable prototype | Key 8 of 9 (clears the key's bar), checks 6 of 8 | **Key 9 of 9**, checks 6 of 8 | Fixed the wrong total and the missing DRAFT marks; the prototype's multi invoice screen is still static |
| [E01 analytics to decisions](E01-analytics-to-decisions/) | Why did activation drop, and is a release driving seats | Key 7 of 10, checks 6 of 8, 1 red flag | **Key 9 of 10**, checks 6 of 8, no red flag | Fixed "halved" (about a third) and "6 weeks" (8); the follow up experiment's length is still wrong |
| [G01 release comms](G01-release-comms/) | Release notes for three audiences from a ticket list | Key 6 of 9, checks 6 of 8 | Key 6 of 9, checks 6 of 8 | The invented API fallback left the changelog but stayed in the partner email |

## What these runs show
The skill finds what a careful PM would find: the contradictions, the stale documents, the misleading
metric, the date that cannot be met. What it does not yet do is check its own writing as strictly as
it checks the inputs.

Version 3 handed that check to a separate reader, and in every run the separate reader really ran. It
caught real errors ("halved", an invented release note clause). But the author kept steering it: it
added its own expected answers to the checker's brief, chose which files it saw, summarised its
table, and edited the message after the check. Version 4, written from these grades and not yet run,
takes the steering away: a fixed checker prompt, the checker's own table as the check file, and no
edits after the check. See the [pm scoreboard](../../evals/scoreboards/pm.md).

The folders ending `-v3-cutoff` hold three version 3 runs that were stopped by a spend limit and rerun.

## How to run one yourself
```text
/prodman:pm I've put every document about our recurring invoices project in
examples/demos/A01-document-chaos/input/. What did we agree, where do they contradict each other,
which can I stop reading, and what should we build first?
```

Each demo folder holds `REQUEST.md` (the exact request), `input/` (the synthetic files), and
`run-2026-10-11/` (the unedited outputs, the final message in `RESULT.md`, and the grade in
`GRADE.md`).
