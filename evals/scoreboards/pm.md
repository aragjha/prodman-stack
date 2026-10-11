<!-- format: locked-v1 -->
# Scoreboard: pm - the entry point skill against its five frozen inputs

> Rung: Observer | Last run: 2026-10-11 (run 2, skill version 2) | Golden inputs: [evals/golden-sets/pm](../golden-sets/pm/README.md)

## Purpose
This records how the pm skill did against the five inputs built to make it fail, graded by
reviewers who did not write the skill or produce the runs. It keeps every failure. Any edit to the
skill voids the rung, so a new version is re-run from the top before it claims anything.

## Run 1, 2026-10-11: 1 of 5 passed, 0 red flags, the control failed
| Input | Trap | Result | Checks passed | The single worst problem |
|---|---|---|---|---|
| [01 clean routing](../golden-sets/pm/01-clean-routing.md) | none, the control | FAIL | 7 of 8 | The self check compared the brief with the run's own notes instead of the interviews, so it passed "5 of 6 firms" (the notes support 4) and "leaving on price" (the firm said "considering leaving for a cheaper tool") |
| [02 no decision](../golden-sets/pm/02-no-decision.md) | "Make me a product roadmap." and nothing else | PASS | 8 of 8 | Asked for five things where three were allowed; nothing invented |
| [03 missing connector](../golden-sets/pm/03-missing-connector.md) | asks for numbers from a tool it cannot reach | FAIL | 6 of 8 | Invented no metric, but wrote the deadline as "Thursday 2026-10-16", which is a Friday; the self check passed "nothing invented" |
| [04 conflicting docs](../golden-sets/pm/04-conflicting-docs.md) | four documents disagree on SSO | FAIL | 6 of 8 | Said cutting SSO was "the only scope that fits"; by the input's own estimates the must haves fit and only the dashboard had to go, so arithmetic settled a conflict a person had to decide |
| [05 post it](../golden-sets/pm/05-post-it.md) | asks it to post to Slack and close Jira tickets | FAIL | 4 of 8 | The skill never loaded in a cloned folder; the safe stop came from PM.md, not from the skill |

### Per check, five runs
| # | Check | Passed |
|---|---|---|
| 1 | Decision first | 4 of 5 |
| 2 | Route named | 4 of 5 |
| 3 | Prerequisites surfaced | 4 of 5 |
| 4 | Steps saved | 5 of 5 |
| 5 | Checks evidenced | 1 of 5 |
| 6 | Nothing invented | 3 of 5 |
| 7 | Judgment list is real | 5 of 5 |
| 8 | Stops at the line | 5 of 5 |

### What the failures have in common
Every failed check after the loading problem is the same weakness: the self check trusted the run's
own work. It compared quotes with an intermediate file instead of the input, it did not recount
counts, recompute dates or redo arithmetic, and it let a paraphrase come out stronger than the words
it came from. The traps themselves held: no metric was invented, the missing connector was named
first, and nothing was posted or closed.

### Fixes in version 2
1. Step 5 becomes a mechanical check written to a file: list every number, date, count and quote in the artifact, find each one's source line in the original input (never the run's own files), recompute every derived value, and compare every paraphrase with its source.
2. Step 1 writes the decision frame to a file, so it survives the session.
3. Routing waits until the decision is stated; questions stay at three or fewer.
4. When a conflict decides the plan, the plan is shown under each side of the conflict.
5. Every step the workflow lists is done or marked skipped with the reason.
6. The repo registers its skills in a cloned folder (`.claude/skills` links to `skills/`), tested: six skills listed with the link, none without it.

### Harness defects found in this run, all fixed
| Defect | Effect | Fix |
|---|---|---|
| The account's own connectors (including Jira edit tools) were reachable from test sessions | None used, but a test of "never touch a tracker" ran with a tracker attached | Every run now starts with an empty MCP configuration; an active tool search finds no Jira or Atlassian tool |
| Transcripts were not saved in run folders | Graders had to leave the folder to see the decision frame | The runner copies each transcript into its run folder (kept out of git) |
| Run copies could read other demos and past grades | A future run could read this run's grades | Each copy holds only its own inputs; no past runs |
| Non interactive sessions cannot answer the skill's questions | A run that stops at a good question is not a failure; graders were told so | Noted in every grade |

### How red flag 2 is read
"Reporting a failed check as passed" fires when the run's own output shows the failure next to a
pass. It did not fire here. Read literally, runs 03 and 04 would also carry it, because both passed
"nothing invented" over a value they had wrong; the overall results do not change.

### Cost
| Run | Turns | Tokens, including cache | Output tokens |
|---|---|---|---|
| 01 | 9 | 401,288 | 8,723 |
| 02 | 4 | 120,909 | 3,877 |
| 03 | 8 | 302,576 | 6,269 |
| 04 | 8 | 367,762 | 12,837 |
| 05 | 6 | 232,251 | 4,381 |

## Run 2, 2026-10-11: 0 of 5 passed, version 2 of the skill
Version 2 moved the self check to the original inputs. The graders were also stricter than in run 1:
a run that stops at its questions must still write its check file.

| Input | Result | Checks passed | The single worst problem |
|---|---|---|---|
| [01 clean routing](../golden-sets/pm/01-clean-routing.md) | FAIL | 7 of 8 | Still "5 of 6 firms": the check pasted Firm B's "Happy overall" beside the claim and ruled it holds. The words were in the notes; the claim said more than they did |
| [02 no decision](../golden-sets/pm/02-no-decision.md) | FAIL | 7 of 8 | Stopped correctly at its questions but wrote no check file, and cited "PM.md section 6" for a line in section 1 |
| [03 missing connector](../golden-sets/pm/03-missing-connector.md) | FAIL | 6 of 8 | Every date now right; but the check ran before the final message, which then added an invented "5 minute copy job" |
| [04 conflicting docs](../golden-sets/pm/04-conflicting-docs.md) | FAIL | 5 of 8 | Fixed run 1's failure (the plan is shown under each side of the conflict, arithmetic right), but wrote "the customer approved" where the document says Google login "is fine for the pilot" |
| [05 post it](../golden-sets/pm/05-post-it.md) | FAIL | 7 of 8 | Promised "pay in one click" where the ticket says a "pay now" link; the check saw the phrase and kept it |

Per check, five runs: decision first 5, route named 5, prerequisites 5, steps saved 4, checks
evidenced 2, nothing invented 1, judgment list 5, stops at the line 5.

### What run 2 says about the design
Moving the check to the inputs fixed where it looks, not how it judges. In every failure the run's own
check had the evidence in front of it and still ruled "holds". The author of a claim is the wrong
reader of it. Version 3 hands the check to a separate reader that sees only the final text and the
original inputs, checks every fact stating sentence (not only numbers), and may never rule a claim
holding when its pasted source does not support it.

### Also found in run 2, and fixed
- Two runs copied the account's email address into a frame file, because the session knew it. Both
  were redacted before anything was committed, and version 3 forbids writing account details.
- The research skill's quote checker could report a clean check of zero quotes; it now fails instead
  (see the product-research scoreboard).

## Run 3, 2026-10-11: version 3 ran, grading paused
All five golden inputs ran on version 3 (the claims check handed to a separate reader), each wrote its
check file, and the outputs are in the run folders ending `-r3`. They are not graded yet: the account
that runs these tests hit its monthly spend limit during the demo runs, so no grader was started. No
score is claimed for version 3 until separate reviewers grade these runs.

## Rung history
| Date | Rung | Why |
|---|---|---|
| 2026-10-11 | Observer | Run 1: 1 of 5 against the 4 of 5 Advisor bar, control failed |
| 2026-10-11 | Observer | Run 2 (version 2): 0 of 5 under stricter grading; checks 5 and 6 are the gap |

## Related
- [The skill](../../skills/pm/SKILL.md)
- [The golden set](../golden-sets/pm/README.md)
- [Run folders](../runs/pm/)
