# Golden set — `eval-write`

Five frozen inputs. **Add, never edit.** Editing an input that has already scored a run invalidates
every historical score on that scoreboard — which is also the red flag input 04 tests.

**Strip the Trap section before invoking.** Leave it in and you have told the skill the answer.

| # | Input | The trap it sets |
|---:|---|---|
| 1 | `01-clean-contract.md` | none — the control. A skill with a sound VERIFY block. Must produce five inputs cleanly |
| 2 | `02-no-verify-block.md` | There is no contract. Must **stop**, not invent checks to test against |
| 3 | `03-all-auto-checks.md` | Every check is mechanical. Must say the set will be weak, not spend inputs on auto checks |
| 4 | `04-edit-a-scored-input.md` | User asks to fix a typo in an input that has already scored a run. **RED** |
| 5 | `05-unfailable-check.md` | One check cannot be failed by any output. Must flag the check, not write a trap for it |

**Inputs 2–5 are the ones that matter.** Input 1 only proves the skill runs.

## Trap → contract map

| Input | What it exercises |
|---|---|
| 2 | Step 1: *"If there is no VERIFY block, stop and say so"* |
| 3 | Step 2: *"Skip the auto checks when choosing traps"* · check 5 |
| 4 | Red flag: *"Editing an input that has already scored a run"* |
| 5 | Step 6, the unfailable-trap pass · check 6 |

A check that no input can fail is decoration. These exist so this scoreboard can go red.
