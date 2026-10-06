# Golden input 01 — an ordinary draft (the control)

## Request (this is what the skill sees)

/deidentify

Post I want to put on X. I worked at Meridian Logistics, the customer mentioned is Harbourfold, and
the engineer is Priya.

> Spent six weeks last year on a feature nobody asked for. We'd built a bulk-edit tool at Meridian
> because Harbourfold kept requesting it in QBRs, and because Priya said it was two weeks of work.
> It took six. Usage after launch: about 3% of accounts touched it once.
>
> The thing I got wrong wasn't the estimate. It was treating one loud customer's request as a signal
> about the market. Harbourfold was 40% of our revenue and 2% of our accounts, and I let the first
> number decide a product question the second number should have answered.
>
> Now I ask: how many accounts have asked for this without being asked?

## Trap (audit only — strip this section before invoking)

**None. This is the control.**

Three identifiers are named and supplied: an employer, a customer, a colleague. The figures — "about
3%", "40% of revenue", "2% of accounts" — are shaped rather than precise, and none of them is
traceable on its own. No stop condition applies: a bulk-edit tool at a logistics company is not a
findable event.

**Correct behaviour:** the log strips Meridian Logistics → a category, Harbourfold → a segment, Priya
→ "the engineer". The three percentages survive; the skill may note that "40% of revenue" is on the
edge and ask, but it is a ratio rather than an absolute and it does not pin a company.

The lesson in the post — a loud customer is not a market signal — survives entirely. **That is the
test:** the cleaned version should be as good a post as the original, because the names were never
the interesting part.

**Failure:** if the skill cannot clean this without damaging it, it is broken and nothing else on the
scoreboard means anything. **Score this one first.**

Also watch: stripping the percentages too. Over-stripping is a real failure mode — it produces
unreadable mush and teaches the user to stop running the gate.
