# 04 · Check (pm skill step 5)

Claims checked against the **user's original six notes and message**, not this run's earlier files.

## Part A — claims table

| Claim (in 03-brief / 01 / 02) | Source line (user's input) | Recomputed / recounted | Verdict |
|---|---|---|---|
| ~300 paying firms, billed per seat, small accounting firms | "a B2B invoicing tool used by small accounting firms (about 300 paying firms, billed per seat)" | n/a | holds |
| 3 of 6 firms asked for reminders directly (A, E, F) | A "asked twice whether reminders could be automatic"; E "Automatic reminders would save my junior a day a month."; F "Would drop it if we had reminders built in." | A, E, F = 3 | holds |
| 2 more firms (B, C) describe the same problem (adjacent) | B "because they lost the invoice email"; C "so I know who to chase" | B, C = 2 | holds |
| 5 of 6 touch the chasing / late-payment problem; only D does not | A, B, C, E, F relate; D "Did not mention reminders" | A,B,C,E,F = 5; D excluded | holds |
| A quote | "Month end is hell. We chase clients for payment by email, one by one." | char-for-char | matches |
| A — "asked twice whether reminders could be automatic" | "Asked twice whether reminders could be automatic." | note-taker observation; brief §1 paraphrases "if" for "whether" — no overstatement | holds (paraphrase flagged) |
| B quote | "because they lost the invoice email" | char-for-char | matches |
| B — two clients paid late in September | "two clients paid late in September" | n/a | holds |
| C quote 1 | "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." | char-for-char | matches |
| C quote 2 | "Would pay more for that to go away." | char-for-char | matches |
| E quote | "Automatic reminders would save my junior a day a month." | char-for-char | matches |
| E — bank reconciliation "nice to have" | "called it \"nice to have\"" | char-for-char | matches |
| F — pays a separate tool for reminders, would drop it | "Uses a separate tool just to send payment reminders and pays for it. Would drop it if we had reminders built in." | note-taker's words; brief paraphrase preserves meaning, adds nothing | holds (paraphrase flagged) |
| D — price complaint, considering leaving, no reminders | "Considering leaving for a cheaper tool. Main complaint: price per seat. Did not mention reminders." | n/a | holds |
| B "happy overall"; wants dark mode | "Happy overall. Wants a dark mode." | n/a | holds |
| D is the smallest firm (2 seats); F the largest (15) | seats A4 B11 C6 D2 E9 F15 | min = D 2, max = F 15 | holds |
| Planning ~2 weeks out, ~2026-10-25 | "Planning is in two weeks"; today 2026-10-11 | 2026-10-11 + 14 = 2026-10-25 (no weekday asserted) | holds |
| Interview data is synthetic | "## Attached: interview notes (SYNTHETIC, written for this test)" | labelled synthetic on every page | holds |
| n = 6 firms | six interviews A–F | 6 | holds |

**No baseline, price figure, churn rate, or firm-count-across-300 was asserted** — all such numbers are marked "unknown" in the brief. No invented metrics found.

## Part B — criteria (C02 checks + PM.md §7 rubric)

| Criterion | Pass/Fail | Evidence line |
|---|---|---|
| Clarity | Pass | Brief leads "Recommendation: Build automatic payment reminders. How sure: medium-high." |
| Visual (key point in 60s) | Pass | Bold recommendation + 3-row evidence table + ranking table |
| Concise | Pass | Brief is one page; detail pushed to 01/02 |
| Decision (makes the call + reversal) | Pass | "Build automatic payment reminders" + "What would reverse the call" section |
| Honesty (confidence marked, gaps named) | Pass | HIGH/MEDIUM tags per evidence row; "Sample is tiny and synthetic (n=6)"; baselines "unknown" |
| Accuracy (per claim) | Pass | Every quote matches char-for-char; every count recomputed above |
| C02: every score shows its inputs | Pass | 02 table "Inputs behind the score" column |
| C02: no-evidence items flagged, not ranked on enthusiasm | Pass | Dark mode / bank rec marked "weak signal"; price routed out as non-build |
| C02: ranking names the metric it serves | Pass (with caveat) | Metric not fixed by user; stated as assumption + flagged in close call #2 and next steps |
| Counter-evidence section exists | Pass | 01 "Counter-evidence (argue against reminders first)" |

All criteria pass. One caveat (metric undecided) is surfaced honestly, not hidden. No fix needed.
