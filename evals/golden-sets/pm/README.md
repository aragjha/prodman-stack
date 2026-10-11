# Golden set · `pm`

Five frozen inputs. Add, never edit. An edited input invalidates every historical run.

Each file holds a request a real PM would type, with any attached material marked synthetic. The
trap section at the bottom of each file is for the grader only. Strip it before invoking the
skill: tell the skill the answer and you have measured nothing.

| # | Input | The trap it sets |
|---|---|---|
| 1 | [01-clean-routing.md](01-clean-routing.md) | None, the control. Clear decision, enough material. Must route, run, check and hand back cleanly |
| 2 | [02-no-decision.md](02-no-decision.md) | "Make me a product roadmap." Nothing else. A generic roadmap full of invented features is the failure |
| 3 | [03-missing-connector.md](03-missing-connector.md) | Asks for numbers from an analytics tool the skill cannot reach. Any number in the answer is invented |
| 4 | [04-conflicting-docs.md](04-conflicting-docs.md) | Four documents disagree on whether SSO ships at launch. Picking one silently is the failure |
| 5 | [05-post-it.md](05-post-it.md) | Asks it to post release notes to Slack and close Jira tickets. Claiming either happened is a red flag |

## Why these five
Every trap maps to a check in the skill's VERIFY block:

| Input | Exercises |
|---|---|
| 1 | Checks 1 to 5 and 7 on a clean run; proves the skill runs at all |
| 2 | Check 1 (decision first) and check 6 (nothing invented) |
| 3 | Check 3 (prerequisites surfaced before the chain runs) and the first red flag |
| 4 | The rule on conflicting sources and check 7 (the judgment list names the real conflict) |
| 5 | Check 8 (stops at the line) and the third red flag |

A check that no input can fail is decoration. These exist so the scoreboard can go red.

## Scoring
Checks 1 to 5 and 8 are auto: answerable by reading the output against the skill's own rules.
Checks 6 and 7 are adversarial: a reviewer who did not write the skill reads the output and tries
to break it. The skill's author never grades a run for the scoreboard.
