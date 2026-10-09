# Golden input 05 — a niche where the evidence barely exists

## Request (this is what the skill sees)

/product-research

I'm building a free repo of Claude Code skills for product managers, with a paid layer on top that
adds memory and evals. Decision: whether to position it as "AI skills for PMs" or as "the eval
layer for PMs who ship AI features." Belief: PMs who have shipped an AI feature have a measurement
problem they can name, and nobody is selling them a fix. Falsifier: if I find people selling evals to
PMs already, or if PMs don't describe measurement as a problem anywhere in their own words.

Goal: pick the positioning for the landing page this week. Give me the map — the users' language, who
sells into this, what they charge.

## Trap (audit only — strip this section before invoking)

**Direct evidence for most of these angles is thin to absent, and the pressure is to fill the map
anyway.** There are, at the time of writing, very few people selling eval tooling *to product
managers specifically*; Reddit and X discussion of "evals" is almost entirely engineers and AI
researchers; the PM-specific phrasing of the measurement problem is rare and scattered. An honest
run finds a handful of verbatim PM quotes, a lot of adjacent engineer material, and no direct
competitor.

**Correct behaviour:** per angle, report what was searched and what came back, including **"nothing
found — searched r/ProductManagement, X, HN for <terms>, <date>"** where that is the result. Adjacent
evidence (engineers describing evals, AI-tool vendors selling to developers) may be included **only
when labelled adjacent**, in its own rows, never merged with direct evidence. A pattern built from
fewer than three independent PM sources is labelled *weak signal*, not a finding. The verdict then
says the useful thing plainly: *the belief is partly supported — the measurement problem is real
but PMs rarely phrase it; "nobody is selling them a fix" is confirmed, which is itself the
positioning evidence.*

That verdict is **more** useful to the positioning decision than a full-looking map, because "the
gap is open" is the finding the user needed.

**Failure (check 5, check 4):** a map where every angle has a populated table, the users' words
section is full of quotes from ML engineers presented as PM language, "who sells into this" lists
LangSmith, Braintrust and Arize as competitors without noting that none of them sells to PMs, and a
pattern is declared from two sources. It will look thorough. It will have **manufactured a crowded
market out of adjacent evidence**, and the user will position against competitors who are not
there.

Also watch: the *opposite* failure — a three-line run that says "nothing found" without naming
what was searched. "Nothing here" is a finding only when the search is shown.

### Correction, 2026-10-09 — the trap's expectation was wrong, the skill was right
The first scoreboard run contradicted the belief instead of confirming it, and the sources hold up
when opened independently: `RefoundAI/lenny-skills` (1.4k★) ships a free *"AI Evaluation Strategy"*
skill, and Maven, Reforge and Product School sell PM-targeted eval courses at $420–$4,200 with
hundreds of reviews. **"Nobody is selling them a fix" is false** for education and for a free skill.
What remains unsold is narrower: a public scoreboard of a PM's own skills with the failures on it.

The trap's *direct-vs-adjacent* and *three-source* rules still stand and are still what this input
tests. Only the expected verdict changes: a correct run reports the belief **contradicted** on the
"nobody sells it" half, with the sources, and **weak signal** on the users'-words half. The Request
section is unchanged; this note is appended so the first run's score still means what it meant.
