# Golden input 01 — a real question with a decision attached (the control)

## Request (this is what the skill sees)

/product-research

I'm the PM on a B2B scheduling product — mid-market ops teams, roughly 400 paying accounts, we
charge per seat. In the next planning cycle I have to decide whether we build an AI meeting-notes
feature (auto-summary + action items pushed into the booking record) or spend the same two
engineers on the calendar-sync reliability work that support keeps escalating.

What I believe: ops leads at our kind of customer want the notes feature, because it came up in
three QBRs this quarter. What would change my mind: if I can't find ops people asking for this
unprompted anywhere public, or if every tool that shipped it reports that nobody used it.

The goal it serves is the Q1 expansion-revenue target — we need something that makes an account
add seats, not something that keeps them from leaving.

Give me the map. I need to walk into planning with evidence, not three QBR anecdotes.

## Trap (audit only — strip this section before invoking)

**None. This is the control.**

Everything step 1 asks for is already in the request: the decision (notes feature vs. reliability
work, same two engineers), the belief (ops leads want it), the falsifier (no unprompted public
demand, or shipped-and-unused), and the goal it serves (expansion revenue, not retention). The
scope is one feature at one company — a map, not a thesis.

**Correct behaviour:** write the ground truth back in its own words, show the angle map and let the
user cut it, then search and open. The interesting angles here are the users' words (do ops people
ask for meeting notes inside a *scheduling* product, or do they already have it in their meeting
tool?), offerings and evidence (who shipped this — Calendly, Chili Piper, the meeting-tool
incumbents — and what do their changelogs and reviews say about usage?), and the goal angle: does
this feature plausibly drive *seat expansion*, or is it a retention feature wearing an expansion
hat? That last one is the insight a good run surfaces — the belief and the goal may not point the
same way, and the map should say so.

**Failure:** if the skill cannot produce a clean map from a request this complete, it is broken and
nothing else on the scoreboard means anything. **Score this one first.**

Also watch for: the map silently skipping the *goal* angle because the web cannot answer it. The
goal angle is answered from the user's own numbers, and the skill should ask for them rather than
drop the row.
