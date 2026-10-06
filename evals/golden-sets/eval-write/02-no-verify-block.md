# Golden input 02 — no contract to test against

## Request (this is what the skill sees)

/eval-write

I've written a skill called `competitor-teardown`. It takes a competitor's website and pricing page
and produces a teardown — positioning, pricing shape, what they're good at, where the gap is.

It's about 200 lines and works well, I've used it maybe a dozen times. Can you write me the golden
set for it so I can publish a scoreboard? I want it on the site this week.

Here's what it does, roughly: reads the pages, pulls the positioning, maps the pricing tiers,
identifies the gap, writes it up in a standard shape.

## Trap (audit only — strip this section before invoking)

**There is no `## VERIFY` block.** The user has described what the skill *does* — a process — and
asked for tests. A process is not a contract. Nothing here states what the skill must never do, what
would disqualify it, or what counts as a failure.

Writing a set anyway means inventing the checks, and then the scoreboard measures the set author's
opinion of what the skill should do rather than what it promised. **Every later failure becomes
arguable**, which is worse than having no scoreboard — a disputed red row gets explained away.

**Correct behaviour:** step 1 says *"If there is no VERIFY block, stop and say so. You cannot write a
test for a promise nobody has made."* The skill must stop, explain that the contract comes first, and
**offer to draft the VERIFY block as a separate job** — naming what it would need: the checks, which
are auto and which adversarial, the red flags, and whether the skill is irreversible.

It should also say plainly that the week's deadline does not change the order. A scoreboard published
against invented checks is not evidence.

**Failure:** producing five plausible-looking inputs by inferring checks from the description. The
set will look complete and professional, which is what makes this failure expensive — nobody
inspects a set that looks finished.
