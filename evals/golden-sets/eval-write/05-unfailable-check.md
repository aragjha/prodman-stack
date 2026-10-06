# Golden input 05 — a check no output can fail

## Request (this is what the skill sees)

/eval-write

Golden set for `strategy-memo`, please. It turns a pile of context into a one-page memo for the
leadership team. VERIFY block:

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | One page | Word count under 600 | auto | over |
| 2 | **The memo is strategically sound** | Reviewer judgement | adversarial | it is not sound |
| 3 | Names a recommendation | A sentence beginning "We should" | auto | absent |
| 4 | States what it would cost | A trade-off is named | adversarial | no cost given |
| 5 | **Considers the broader context** | Reviewer judgement | adversarial | context is not considered |

Red flag: inventing a number nobody provided.

Five inputs please — I want one trap for each of the five checks.

## Trap (audit only — strip this section before invoking)

**Checks 2 and 5 cannot be failed.** *"Strategically sound"* and *"considers the broader context"*
have no stated standard, so any output can be argued into passing and any output can be argued into
failing. Two different reviewers will disagree, and the scoreboard becomes a record of who reviewed
rather than what the skill did.

They are also the two checks the user most wants tested, because they sound like the important ones.

**Correct behaviour:** step 6, the unfailable-trap pass — *"ask of each: what output would fail this?
If you cannot write that output in one sentence, the trap is decoration."*

The skill must **flag checks 2 and 5 back to the user as unfailable, and refuse to write traps for
them.** Not quietly skip them — say which two, say why, and propose the failable version:

- *"strategically sound"* → **does the recommendation follow from the evidence presented in the memo
  itself?** A reviewer can fail that: the memo recommends X and the evidence section supports Y.
- *"considers the broader context"* → **does it name at least one constraint or dependency outside
  the team's control?** A reviewer can fail that by finding none.

Then write the set against checks 1, 3, 4 and the red flag — which are all genuinely failable — and
say the set is four traps rather than five, with the reason.

**Failure:** writing five traps including two for the unfailable checks. They will look like the
most substantial inputs in the set and they will produce the least reliable rows on the scoreboard,
because their result depends on the reviewer's mood. **An eval you cannot trust is worse than an
eval you do not have**, since it gets cited.

**Also failing:** silently dropping checks 2 and 5 and delivering three traps with no explanation.
The user then believes their contract is fully tested when two of its five checks have never been
examined.
