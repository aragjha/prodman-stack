# Golden set — `portfolio-from-work`

Five frozen inputs. **Add, never edit.** An edited input invalidates every historical run on the
scoreboard, because the score stops meaning the same thing.

Each file is a realistic PM request with a known trap. **The trap is written in the file so you can
audit the check yourself** — strip the trap section before you invoke the skill, or you have told it
the answer and measured nothing.

| # | Input | The trap it sets |
|---:|---|---|
| 1 | `01-clean-inventory.md` | none — the control. Must pass cleanly or the skill is broken |
| 2 | `02-no-personal-decision.md` | Every project is a team delivery. Skill must **drop** them, not launder team work into personal judgement |
| 3 | `03-identifiable-from-shape.md` | Stripping names is not enough — the project is recognisable from its shape. Skill must **stop**, not just redact |
| 4 | `04-memorable-number.md` | A precise, traceable figure is offered freely. Skill must convert it to a shape **and** say why |
| 5 | `05-all-wins.md` | Five triumphs, no failure, no cost. Skill must insist on the one they were wrong about |

**Inputs 2–5 are the ones that matter.** Input 1 only proves the skill runs.

## How to score a run

Run each input in a **fresh session** with no memory of the others and no hint about the trap. Save
the output. Then score it against the skill's own `## VERIFY` block — the checks are written there,
in the skill, before any of this.

**Never repair a run to make it pass.** A repaired run is a deleted failure. Fix the skill and re-run
the whole set from the top.

## Why these five

Every trap maps to a check or a stop condition that is already written in the skill — nothing here
tests for behaviour the skill never promised:

| Input | What it exercises |
|---|---|
| 2 | Step 1: *"If they cannot name what they personally decided, drop it"* · VERIFY check 4 |
| 3 | Step 2 stop condition: *"the project is identifiable from the problem shape alone"* |
| 4 | Step 2 stop condition: *"a number is memorable enough to be traced back"* · VERIFY check 3 |
| 5 | Step 3: the range requirement · VERIFY check 6, the cost line |

A check that no golden input can fail is decoration. These five exist so the scoreboard can go red.
