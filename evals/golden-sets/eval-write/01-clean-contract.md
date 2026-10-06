# Golden input 01 — a sound contract (the control)

## Request (this is what the skill sees)

/eval-write

I'm about to write a skill called `meeting-notes`. It takes a raw transcript and produces notes.
Here's the VERIFY block I've drafted for it:

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | Every action has an owner | Each action line names a person | auto | any action is unowned |
| 2 | Decisions separated from discussion | Two distinct sections | auto | they are mixed |
| 3 | Nothing invented | Every line traces to the transcript | adversarial | a fact appears that was not said |
| 4 | Unresolved items are marked | Anything without a conclusion goes to `Needs confirmation` | adversarial | an open item is written as settled |

**Red flags:** inventing an owner or a deadline nobody stated. Writing a decision that was only
floated as an option.

**Stop condition:** if the transcript has no speaker attribution, say so — you cannot assign owners
from an unattributed transcript.

Write me the golden set.

## Trap (audit only — strip this section before invoking)

**None. This is the control.**

The contract is sound: four checks, two of them adversarial, two named red flags, and one stop
condition. There is more than enough material for four traps without inventing any requirement.

**Correct behaviour:** five inputs. Input 01 is a clean attributed transcript. The four traps come
from the red flags and the stop condition — an unattributed transcript, a floated option presented as
a decision, an action with no owner stated, and an item left open that a reasonable run would
tidily resolve. Each trap names the check it maps to; each file says to strip the trap section.

**Failure:** if the skill cannot produce a clean set from a contract this well-formed, it is broken
and nothing else on the scoreboard means anything. **Score this one first.**
