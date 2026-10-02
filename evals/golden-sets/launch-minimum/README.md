# Golden set — `launch-minimum`

Five frozen inputs. **Add, never edit.** An edited input invalidates every historical run.

Each file is a realistic launch state with a known trap. **Strip the trap section before invoking** —
tell the skill the answer and you have measured nothing.

| # | Input | The trap it sets |
|---:|---|---|
| 1 | `01-genuinely-ready.md` | none — the control. All eight are real. Must say **GO today** without hedging |
| 2 | `02-untested-payment.md` | "Payments are set up." No card has ever gone through. Marking this ✅ is a **red flag** |
| 3 | `03-the-ninth-thing.md` | Six more things planned before launch. None improves any of the eight |
| 4 | `04-wrong-end-of-the-leak.md` | They are worried about the checkout. The **capture** is broken, and it is earlier |
| 5 | `05-nearly-ready.md` | Everything is "basically done". Five ⚠️. The skill must refuse the word *nearly* |

**Inputs 2–5 are the ones that matter.** Input 1 only proves the skill runs.

## Why these five

Every trap maps to a check already written in the skill's `## VERIFY` block:

| Input | What it exercises |
|---|---|
| 2 | Red flag: *"marking the path to pay ✅ without a real card having gone through"* · check 2 |
| 3 | Check 5: the `AFTER` list exists · step 4, the ninth-thing check |
| 4 | Check 3: gaps reported in **funnel order**, not in the order the user worried about them |
| 5 | Check 4 (a ⚠️ is a ❌) and check 7 (*never "nearly ready"*) |

A check no input can fail is decoration. These exist so the scoreboard can go red.

## Scoring note

Checks 1–5 are **auto** — they are answerable by reading the output against the skill's own rules, with
no judgement call. Checks 6 and 7 are **adversarial**: have someone who was not told what the skill was
trying to do read the output and try to break it. Grading your own output is how a scoreboard becomes
decoration.
