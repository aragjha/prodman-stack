# Flagship demos

Five real runs of the `pm` skill on five product management problems, each in a fresh Claude Code
session with no access to anything but its own inputs. Every output is saved unedited, and each run
was graded by a separate reviewer who did not write the skill or the inputs and who had an answer key
the run never saw.

**The inputs are synthetic.** They describe Ledgerly, a made up invoicing tool for small accounting
firms, and every input file says so on its first line. The problems planted in them (contradictions,
stale documents, a misleading metric, a breaking change) are listed in answer keys kept outside this
repo until the runs were graded.

## Results, version 2 of the skill, 2026-10-11
| Demo | What the PM asked | Planted problems found | Result | The single worst problem |
|---|---|---|---|---|
| [A01 document chaos](A01-document-chaos/) | 15 messy documents: what did we agree, what conflicts, what to build first | 9 of 10 answer key criteria: all five contradictions with both sources, both stale documents, five duplicate groups, the theme in five sources, and that the CEO's date cannot be met | FAIL | Shortened customer quotes inside quotation marks with no ellipsis, and the self check covered 13 of 35 quotes |
| [C01 idea to roadmap](C01-idea-to-roadmap/) | Turn a rough idea into a roadmap two squads can deliver, with competitor research | 7 of 10; 13 of 16 outside claims were on their pages | FAIL | The seat growth assumption can only be tested after both squads are committed; one quote came from a search summary, not the page |
| [D01 PRD to experience](D01-prd-to-experience/) | Turn a PRD into flows, states and a clickable prototype | 8 of 9, which clears the key's bar: all five planted gaps found | FAIL | The 12 screen prototype it built shows wrong totals and a static multi invoice flow; it was never read back |
| [E01 analytics to decisions](E01-analytics-to-decisions/) | Why did activation drop, and is the bulk invite release driving seats | 7 of 10: dated the drop to the right release, ruled out both decoys, caught the definition change behind the fake seat jump | FAIL | Called a fall of about a third "halved", and its check saw "6 weeks" against 8 and passed it |
| [G01 release comms](G01-release-comms/) | Release notes for three audiences from a ticket list | 6 of 9: kept unmerged tickets out, flagged the breaking change, caught a missed notice period | FAIL | Offered the partner an old API version as a fallback the scope never mentions |

## What these runs show
The skill finds what a careful PM would find: the contradictions, the stale documents, the
misleading metric, the date that cannot be met. What it does not yet do is check its own writing as
strictly as it checks the inputs. Every run failed the same two checks: claims that said slightly more
than their source, and a self check that let them through.

Version 3 hands that check to a separate reader. Its demo runs are in the folders ending `-v3`: E01 and
G01 finished; A01, C01 and D01 were cut off when the test account hit its monthly spend limit. None of
them is graded yet, so no result is claimed for version 3.

## How to run one yourself
```text
/prodman:pm I've put every document about our recurring invoices project in
examples/demos/A01-document-chaos/input/. What did we agree, where do they contradict each other,
which can I stop reading, and what should we build first?
```

Each demo folder holds `REQUEST.md` (the exact request), `input/` (the synthetic files), and
`run-2026-10-11/` (the unedited outputs, the final message in `RESULT.md`, and the grade in
`GRADE.md`).
