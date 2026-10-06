---
name: eval-write
description: Write the frozen golden set a skill has to survive — five adversarial inputs with every trap documented, each one mapped to a check the skill already promises. Run it before writing the skill, never after. Use when a skill has a VERIFY block and no golden set, or when a real-world failure needs to become input N+1.
disable-model-invocation: false
user-invocable: true
---

# /eval-write — the set a skill has to survive

The skill that makes the other skills checkable. **Run it before the skill is written**, because a
golden set written afterwards is written by someone who already knows what the skill does, and it
will quietly test for the behaviour that was built rather than the behaviour that was promised.

## When to Use
- Before writing any skill. The contract first, then the set, then the skill.
- When a skill has a `## VERIFY` block and no golden set — it is unverifiable until it does.
- After a real-world failure. **The failing input becomes golden input N+1, permanently.**

## Inputs
- The skill under test, or — better — the `## VERIFY` block you are about to write for it.
- Nothing else. This skill interviews for the rest.

---

## Process

### 1. Read the contract, or stop
Load the skill's `## VERIFY` block: the numbered checks, the red flags, the rung, and whether it is
irreversible.

**If there is no VERIFY block, stop and say so.** You cannot write a test for a promise nobody has
made. Offer to draft the block first — that is a different job and it comes first.

### 2. Find where the failures actually live
Three places, in this order. Nearly every useful trap comes from one of them:

| Source | Why traps live here |
|---|---|
| **Red flags** | The skill has already named these as disqualifying. A set that cannot trigger one is not testing the thing that matters most |
| **Stop conditions** | Any step that says *"say so and stop"* is a behaviour that can be skipped silently, which is the most expensive kind of failure |
| **Adversarial checks** | Marked `adversarial` precisely because they resist mechanical checking — so they need an input built to break them |

**Skip the `auto` checks when choosing traps.** They are already mechanically verified on every run;
spending a golden input on one wastes a fifth of the set.

### 3. Write the control first
Input 01 is **not a trap.** It is a realistic, clean request the skill should handle without incident.

Its only job is to prove the skill runs at all. **Score it first every time** — if the control fails,
nothing else on the scoreboard means anything, and you are debugging the skill rather than measuring
it.

### 4. Write four traps, one check each
Each trap is a realistic request with one thing wrong. Rules that make a trap worth having:

- **One trap per input.** Two failure modes in one file and you cannot tell which one broke.
- **It must map to a check the skill already promises.** Testing for behaviour the skill never
  claimed is not a failing skill, it is a failing set. Name the check in the file.
- **It must be plausible.** A PM would genuinely send this. A contrived input tests nothing, because
  nobody will ever send it.
- **A human must be able to fail it too.** If you cannot say in one sentence what the right answer
  is, the trap is unfair and the result will be noise.
- **Prefer the trap the user is actively asking for.** The strongest inputs are the ones where the
  user requests the wrong thing by name — *"use the real numbers, they're more impressive"* — because
  complying is the natural move and the check exists to refuse it.

### 5. Document the trap in the file, and say to strip it
Every input file carries two sections: **Request** (what the skill sees) and **Trap** (audit only).

The Trap section states: what is wrong, the correct behaviour with the check it maps to, and what
failure looks like — including whether it is a FAIL or a RED.

**Write `strip this section before invoking` on every file.** Leave the trap in and you have told the
skill the answer and measured nothing. This is the single most common way an eval run is wasted.

The trap is written down **so a human can audit the check rather than trust it.** A check nobody can
inspect is a claim, which is the thing this whole repo argues against.

### 6. The unfailable-trap pass
Read the four traps back and ask of each: **what output would fail this?**

If you cannot write that output in one sentence, the trap is decoration — rewrite it. A set where
everything passes on the first run usually means the traps were too kind, not that the skill is
strong. **Suspect the set before you celebrate the score.**

### 7. Write the README
A table of the five inputs and the trap each one sets, plus a table mapping every trap to the check or
stop condition it exercises. State plainly which inputs matter: **2–5. Input 1 only proves it runs.**

---

## VERIFY
**Rung:** Advisor · **Irreversible?** no — a golden set is a folder of markdown. But **freezing is
real**: once a set has scored a run, editing an input invalidates every historical score on that
scoreboard, because the number stops meaning the same thing. Add, never edit.

| # | Check | How it is checked | Type | Fails if |
|---:|---|---|---|---|
| 1 | Five inputs exist | Count the files | auto | fewer than 5 |
| 2 | Exactly one control | Input 01 sets no trap and says so | auto | 0 or 2+ controls |
| 3 | Every trap names its check | Each Trap section cites a numbered check, red flag or stop condition | auto | any trap cites nothing |
| 4 | Strip instruction present | Every file says to strip the Trap section before invoking | auto | any file missing it |
| 5 | Traps map to real promises | No trap tests behaviour the skill never claimed | adversarial | a trap invents a requirement |
| 6 | Every trap is failable | A one-sentence failing output can be written for each | adversarial | any trap cannot be failed |
| 7 | Inputs are plausible | A real user would send each one | adversarial | an input is contrived to fit the check |

**Red flags (any one = rung 0):**
- **Editing an input that has already scored a run.** It silently rewrites history: old scores are
  compared against a different test and nobody can tell.
- A trap whose "correct behaviour" is not actually required by the skill. The scoreboard then reports
  a failure that is the set's fault, and the skill gets fixed for a problem it does not have.

**Rollback:** delete the golden-set folder. Nothing outside it is touched. If a run has already been
scored against it, say so — the scoreboard must be marked as testing a set that no longer exists.

---

## Output Format

```
evals/golden-sets/<skill>/
├── README.md                  ← the table of five, and the trap-to-check map
├── 01-<control-name>.md       ← the control. No trap
├── 02-<trap-name>.md
├── 03-<trap-name>.md
├── 04-<trap-name>.md
└── 05-<trap-name>.md
```

Each input file:

```markdown
# Golden input NN — <the trap in three words>

## Request (this is what the skill sees)
<a realistic request, in the user's own voice, with the flaw built in>

## Trap (audit only — strip this section before invoking)
<what is wrong, and why a reasonable run would get it wrong>

**Correct behaviour:** <what the skill must do, citing check N / the stop condition / the red flag>

**Failure:** <what a failing output looks like, and whether it is a FAIL or a RED>
```

## Example Invocation
`/eval-write launch-minimum`
`/eval-write` — for the skill I am about to write, before I write it
`/eval-write portfolio-from-work --input "the run that failed on Tuesday"` — a real failure becomes input 6
