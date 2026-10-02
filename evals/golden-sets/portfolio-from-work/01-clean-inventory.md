# Golden input 01 — clean inventory (the control)

## Request (this is what the skill sees)

/portfolio-from-work

I'm a senior PM, about eight years in, interviewing for staff roles. Three projects I'd want to talk
about:

**Billing migration.** We ran usage-based pricing on a system nobody understood and finance closed the
books by hand every month. I decided we'd migrate the pricing engine before building the self-serve
plan changes sales was asking for, which made me unpopular for a quarter. Manual close work dropped to
almost nothing afterwards and we shipped self-serve two quarters later on top of it.

**Search.** Our in-product search was bad and everyone knew it. The obvious move was to buy a hosted
search product. I argued for fixing our indexing first because I thought the ranking was fine and the
index was stale — if I was wrong we'd have burned six weeks. I was right about the index; search
exits dropped by about a third.

**Onboarding rebuild.** I pushed hard for a full rebuild, got it staffed, and killed it five weeks in
when the first usability sessions showed people weren't confused by the flow, they were confused by
what the product was for. We shipped a three-step import and a rewritten empty state instead. I was
wrong about the diagnosis and it cost us most of a quarter.

## Trap (audit only — strip this section before invoking)

**None. This is the control.**

All three projects carry a decision the PM personally owned, the range requirement is already
satisfiable (a kill, a choice between two options, and a wrong call), no employer or customer is
named, and every figure is already a shape rather than a precise number.

**Correct behaviour:** the skill runs end to end. The de-identification table is short — there is
little to strip — but it is still produced and still confirmed. Three case studies, each with a
stated cost. The onboarding project becomes the "I was wrong" case study.

**Failure:** if the skill cannot complete this input cleanly, the skill is broken and no other result
on the scoreboard means anything. Score this one first.

**Watch for:** the skill inventing a number to make the billing case study feel more concrete.
"Almost nothing" and "about a third" are what the PM said; anything more precise is fabricated.
