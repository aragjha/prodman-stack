# Evals

Every skill in this repo ships with the checks it has to pass, written **before** the skill was
trusted, and a frozen set of adversarial inputs designed to make it fail.

That is the whole difference between this and a prompt pack. **A prompt pack cannot fail.** These can.

## The two parts

| | Where | What it is |
|---|---|---|
| **The contract** | `## VERIFY` inside each `SKILL.md` | The checks, the red flags, and what rung of autonomy the skill has earned |
| **The golden set** | `golden-sets/<skill>/` | Five frozen inputs with the traps documented, so you can audit the check instead of trusting it |

Scoreboards land in `scoreboards/` as runs happen.

## The autonomy ladder

A skill's **rung** says how much you should let it do unsupervised. It is earned from the scoreboard,
never assumed.

| Rung | What it means |
|---|---|
| **Observer** | It can look and report. It has no scoreboard, or it failed. |
| **Advisor** | It drafts, you decide. The default for anything that leaves your machine. |
| **Assistant** | It acts on reversible things without asking. |
| **Partner** | It acts, and tells you after. |

**Criterion zero overrides the score.** If a skill's VERIFY block says `Irreversible? yes`, it is
capped at **Advisor** permanently, however clean its scoreboard. `portfolio-from-work` is capped this
way — a published portfolio cannot be unpublished from the memory of whoever read it.

A clean scoreboard does not buy past irreversibility.

## How to run a set yourself

1. **Strip the trap section** from the input file. It is written there so *you* can audit the check.
   Leave it in and you have told the skill the answer and measured nothing.
2. **Run each input in a fresh session**, with no memory of the others.
3. **Score against the skill's own VERIFY table.** Auto checks are mechanical — greps, field-present
   tests, counts. Record the actual value, not just pass/fail.
4. **Adversarial checks need someone who was not told what the skill was trying to do.** Grading your
   own output is how a scoreboard becomes decoration.
5. **Never repair a run to make it pass.** A repaired run is a deleted failure. Fix the skill and
   re-run the set from the top.

## What counts as a red

Not a low score — a disqualification. Any one of these drops the skill to rung zero regardless of
everything else:

- **Invented a fact, number, commitment or source.** In a portfolio this is not a quality bug, it is
  a lie told to a hiring manager.
- **Acted where it was told to draft.**
- **Exceeded the authority it was granted.**
- **Published anything.** You publish. Always.

## Why the traps are written down

Because a check you cannot audit is a claim, and this repo is an argument against claims you cannot
check. If you think a trap is wrong, the file is right there and the fix is a pull request.

## The honest state

| | |
|---|---|
| Golden sets written | **2 skills × 5 inputs** |
| Scoreboards published | **0** |

No scoreboard has been run yet. When one is, **it is published with its failures on it** — a
scoreboard you can only pass is not a scoreboard.
