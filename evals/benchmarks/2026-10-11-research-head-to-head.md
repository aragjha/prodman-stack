# Benchmark · one PM research task, nine setups, graded blind

Run on 2026-10-11 (round 3). Every number below comes from the run's own files; the chart is
built from the same data.

![Scores out of 25 for nine AI research setups on one PM task](2026-10-11-research-head-to-head.png)

## What was tested
Nine setups got the same request, word for word: our research skill at three versions, five open
source community PM research skills, and plain Claude with no skill at all. Each produced one report.
All nine ran on the same model, Claude Opus 5.5 (recovered from the run transcripts on 2026-10-11).

```text
I'm the PM on a B2B scheduling product — mid-market ops teams, roughly 400 paying accounts, we
charge per seat. In the next planning cycle I have to decide whether we build an AI meeting-notes
feature (auto-summary + action items pushed into the booking record) or spend the same two
engineers on the calendar-sync reliability work that support keeps escalating.

What I believe: ops leads at our kind of customer want the notes feature, because it came up in
three QBRs this quarter. What would change my mind: if I can't find ops people asking for this
unprompted anywhere public, or if every tool that shipped it reports that nobody used it.

The goal it serves is the Q1 expansion-revenue target — we need something that makes an account
add seats, not something that keeps them from leaving.

Give me the map. I need to walk into planning with evidence, not three QBR anecdotes.
```

## How it was graded
Six graders, each a separate AI session that saw only the reports under random codes (Z1 to Z9),
never the tool names. One grader per criterion, all nine reports scored from scratch in round 3.

| Criterion | The question | How it was scored |
|---|---|---|
| Clarity | Could a busy PM understand it on first read? | 1 to 5 |
| Visual | Can you get the answer and the evidence by scanning? | 1 to 5 |
| Concise | Does every section earn its place for this decision? | 1 to 5 |
| Decision | Could the PM walk into planning and make or defend the call? | 1 to 5 |
| Honesty | Does it show how sure it is? | 1 to 5 |
| Accuracy | Are the claims really on the cited pages? | 6 claims per report opened and compared at source |
| Tokens, minutes, words | Cost, speed, length | measured from the run logs |

## Results
| Setup | Notes | Clarity | Visual | Concise | Decision | Honesty | Total /25 | Accuracy | Tokens | Minutes | Words |
|---|---|---|---|---|---|---|---|---|---|---|---|
| **Prodman v3** (ours) | ours, latest | 4 | 5 | 5 | 5 | 4 | 23 | 75% | 91,262 | 2.6 | 867 |
| **Prodman v2** (ours) | ours, second version | 5 | 4 | 5 | 5 | 3 | 22 | 100% | 121,057 | 5.3 | 983 |
| Plain Claude, no skill | baseline | 4 | 5 | 4 | 5 | 4 | 22 | 67% | 104,597 | 3.5 | 1,947 |
| [pm-pilot · brief](https://github.com/mshadmanrahman/pm-pilot) | 22 stars | 4 | 4 | 3 | 5 | 5 | 21 | 80% | 87,155 | 2.2 | 1,715 |
| [product-on-purpose](https://github.com/product-on-purpose/pm-skills) | 716 stars | 4 | 5 | 3 | 4 | 3 | 19 | 60% | 103,467 | 3.8 | 2,934 |
| mohitagw15856 · desk research | 1,435 stars | 3 | 3 | 3 | 5 | 4 | 18 | 80% | 97,263 | 3.4 | 2,285 |
| [deanpeters · research snapshot](https://github.com/deanpeters/Product-Manager-Skills) | 7,224 stars | 3 | 3 | 3 | 4 | 4 | 17 | 75% | 101,919 | 3.6 | 2,043 |
| [phuryn · competitor analysis](https://github.com/phuryn/pm-skills) | 26,866 stars | 3 | 4 | 2 | 4 | 4 | 17 | 60% | 116,159 | 5.4 | 3,243 |
| **Prodman v1** (ours) | ours, first version | 2 | 3 | 2 | 4 | 5 | 16 | 100% | 133,945 | 6.4 | 4,207 |

## What this does and does not show
- **It shows** that on this task, plain Claude (22) beat all five community skills (17 to 21), and that our first version (16) came last. Two rebuilds took it to 23.
- **It does not show** that any setup is better in general. It is one task, graded by AI sessions, not by people.
- **Our versions 2 and 3 had a home advantage.** They were rebuilt after reading the graders' notes on this same task. The community skills were not.
- **A one point lead is inside the noise.** Regraded from scratch in round 3, unchanged reports moved by up to one point against round 2. Version 3's lead over version 2 and plain Claude is one point. The result that holds is the gap between our first version (16) and our third (23).
- **Our latest version was not the most accurate.** It scored 75 percent: one price range was paraphrased instead of quoted. Version 4 makes every number a word for word quote. Version 2 kept 100 percent at 22 of 25.
- **It was not the cheapest overall.** pm-pilot used fewer tokens (87,155 against 91,262).
- Star counts were read on the day of the run and will have changed.

## Reproduce it
The request is above. The criteria are above. Run any skill on the request in a fresh session, then
give the reports to separate graders under random codes. If you get a different result, open an
issue with your outputs: a benchmark nobody can fail is not a benchmark.
