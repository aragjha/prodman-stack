# Worked example — one case study, start to finish

A real run of `/portfolio-from-work`, showing what goes in and what comes out. The project below
is fictional, written to demonstrate the shape. Your own will read like this.

---

## What the PM said in the interview

> "At [company] we had this onboarding flow for the admin console. Activation was bad — something
> like 30% of signups never got to the point of inviting a teammate. I pushed hard for a guided
> setup wizard. Took us a quarter. It barely moved. Turned out the problem was people signing up
> who had no team to invite yet. We killed the wizard, changed who we let in at the top of the
> funnel instead, and activation went up more in six weeks than the wizard did in a quarter."

That is the whole input. No documents. Four sentences from memory.

---

## What the de-identification pass stripped

| Found | Replaced with | Why |
|---|---|---|
| `[company]` | "a B2B workflow product" | Employer identifiable |
| "30% of signups" | "roughly a third" | Exact figure not confirmed public |
| "admin console" | kept | Generic across hundreds of products |
| "a quarter" / "six weeks" | kept | Durations are not identifying |

Confirmed by the PM before anything was written. Logged in `deidentification-log.md`.

---

## The case study it produced

### Onboarding activation on a B2B workflow product

**The situation.** A B2B workflow product sold to teams, where the core value only appears once
a second person joins the workspace. Self-serve signup, no sales touch below a certain size.

**The problem.** Roughly a third of signups never invited anyone. The working assumption
across the team was that setup was too hard — the console asked for a lot before it gave
anything back.

**What I decided.** I argued for a guided setup wizard and I won the argument. The alternative
on the table was tightening who we let in at the top of the funnel, which I rejected as
"shrinking the number to fix the ratio." We spent a quarter building the wizard.

**What it cost.** A quarter of two engineers and a designer, and the top-of-funnel work we
deferred to do it.

**What happened.** The wizard barely moved activation. Digging into the accounts that stalled,
most of them had no second person to invite yet — solo signups evaluating the product, not
teams adopting it. The friction was never the problem. **I had diagnosed the ratio and ignored
who was in the denominator.** We cut the wizard, changed qualification at signup, and activation
improved more in six weeks than the wizard achieved in a quarter.

**What I would do differently.** Before building, I would have looked at the stalled accounts
one at a time rather than in aggregate. Twenty minutes of reading individual signups would have
shown me the pattern, and I would have got the quarter back. I now treat an aggregate metric as
a prompt to go and read the rows, not as a finding.

---

## Why this one gets replies

It is the **"I was wrong"** case study, and it is doing four things a wall of wins cannot:

1. **It names a decision, not a delivery.** "I argued for it and I won the argument" is
   accountability. "We shipped a wizard" is a changelog.
2. **It names the alternative that lost** — and it was the one that turned out to be right.
   That is uncomfortable, which is exactly why it reads as true.
3. **It states the cost in the currency that matters.** A quarter of three people, plus the
   deferred work. Not "we invested heavily."
4. **The lesson is specific enough to be useful to the reader.** "Read the rows, not the
   aggregate" is a transferable rule. "Always validate assumptions" is a fortune cookie.

An interviewer who reads this has a question ready, and it is the question the PM most wants:
*"tell me about how you found that."*

---

## And then the artifact

The natural build from this case study is a **stall-diagnosis tool**: point it at signup data,
segment the accounts that never activated, and surface the *shape* of who is stalling rather
than the rate at which they stall. Synthetic data, a few hours in Claude Code, no employer
information anywhere near it.

That turns the last paragraph of the case study from a lesson learned into a **link that opens
and works** — which is the entire difference between a portfolio and a résumé in prose.
