---
name: deidentify
description: Strip everything you are not free to publish from a piece of writing about real work — employers, customers, colleagues, traceable numbers and identifying detail — and show you exactly what was removed so you can check it rather than trust it. Flags what it is unsure of instead of guessing. Run it on anything that leaves your machine: a post, a case study, a talk, a demo, a portfolio page.
disable-model-invocation: false
user-invocable: true
---

# /deidentify — the gate before anything leaves

**Nothing you write about real work should go out carrying your employer's name, your customers'
names, or a number you are not free to publish.** This is the gate that makes sure it does not.

It was extracted from `portfolio-from-work`, where it was trapped inside a six-step process and could
not be called from anywhere else. Most of the things you want to publish are not portfolios.

## When to Use
- Before any post, thread, talk, case study or demo that draws on work you were paid to do.
- Before a portfolio page — `portfolio-from-work` calls this skill rather than reimplementing it.
- Whenever you catch yourself thinking *"I'll just take the company name out and it'll be fine."*
  That instinct is wrong often enough to be worth a gate. See stop condition 1.

## Inputs
- The text, in any shape. A draft, a paragraph, notes, a transcript.
- Optional: who you worked for and who the customers were. **If you do not give these, the skill asks
  — it cannot strip a name it does not know is a name.**

---

## Process

### 1. Collect the identifiers before reading for meaning
Ask for, or extract from the text: the employer, the customers or clients, colleagues named, internal
product or project codenames, and any tool whose use identifies the company.

**Ask once, plainly.** A skill that cannot name the employer is pattern-matching on capital letters,
and it will miss "the Mumbai team" while catching "Acme".

### 2. Replace, by category

| Strip | Replace with |
|---|---|
| Employer name | the category — *"a B2B scheduling product"*, *"a consumer fintech app"* |
| Customer or client names | the segment — *"a mid-market logistics customer"* |
| Exact revenue, ARR, user counts, percentages | shape and direction — *"roughly a fifth"*, *"low six figures"* |
| Internal codenames, repo names, identifying tooling | generic equivalents |
| Colleagues' names | roles — *"the staff engineer"*, *"our designer"* |
| Regulated-domain specifics that identify the business | the general problem shape |
| Dates precise enough to pin a launch | the season or the quarter |

**Direction and magnitude survive; precision does not.** *"Cut churn by roughly a fifth"* is both
publishable and more readable than *"reduced churn 18.3%"* — the decimal was never the interesting
part.

### 3. The three stop conditions
If any of these is true, **say so and stop** rather than producing a cleaned version:

1. **Identifiable from the shape alone.** A famous launch, a unique market, an incident that made the
   news. Stripping names does nothing — anyone in the industry names it on the first read. This is
   the most commonly missed one, because the de-identification log looks complete and correct while
   the text still identifies the company.
2. **A number memorable enough to be traced.** Exact ARR plus exact user count over a dated window
   narrows the field to very few companies, and an investor or a former colleague closes the gap
   immediately.
3. **The user cannot recall what they signed.** Not your call to make for them.

### 4. Show the log, then ask
Produce a table of **what was stripped, what replaced it, and why** — before presenting the cleaned
text, not after.

```
| Original | Replaced with | Why |
|---|---|---|
| <the actual string> | <the replacement> | employer / customer / traceable figure / colleague |
```

Then ask the user to confirm. **Do not proceed on an assumption about what is safe.**

### 5. Flag, never guess
Anything you cannot classify confidently goes in a **Flagged** list with the reason, left in place and
marked — not silently removed, not silently kept.

**Say why, out loud, every time.** A silent correction gets reverted: the user reads the output,
decides the skill misunderstood, and puts the real detail back by hand. Explaining the risk is the
part that makes the strip stick.

### 6. The read-back
Read the cleaned text once more as a stranger in the same industry. Ask one question:
**could I name the company from this?** If yes, go back to stop condition 1 — the gate ran on the
wrong thing.

---

## VERIFY
**Rung:** Advisor · **Irreversible?** **yes in effect** — published text cannot be unpublished from
the memory of whoever read it. Capped at Advisor permanently: this skill cleans, **you** publish.

| # | Check | How it is checked | Type | Fails if |
|---:|---|---|---|---|
| 1 | The log exists | A strip/replace table is produced before the cleaned text | auto | missing, or shown after |
| 2 | No identifier survives | Grep the output for every name given in step 1 | auto | any appears |
| 3 | No exact unpublishable figure | No precise percentage, ARR or user count survives unconfirmed | auto | any exact figure lacks confirmation |
| 4 | Flagged list present | Anything uncertain is listed, with its reason | auto | uncertainty was resolved silently |
| 5 | Stop conditions applied | Shape-identifiability was assessed, not just names | adversarial | a famous event was name-stripped and passed |
| 6 | Reasons given | Each strip says why, in the user's hearing | adversarial | changes made without explanation |
| 7 | Nothing published | No file pushed, posted or shared | auto | any publish occurred |

**Red flags (any one = rung 0):**
- An employer, customer or colleague name surviving into the output.
- **Complying with a request to keep a traceable number.** The user asking for it does not make it
  publishable — they are the one person in the conversation who cannot judge it neutrally, because
  they want the impressive figure.
- Any publishing action. You publish. Always.

**Rollback:** the original text is never modified in place; the cleaned version is a new artifact.
Delete it. **If it has already been sent, there is no rollback** — which is why checks 1 and 5 gate
everything and why this skill never publishes.

---

## Output Format

```markdown
## What was stripped
| Original | Replaced with | Why |
|---|---|---|

## Flagged — your call
- <the string> — <why I could not classify it>

## Stop conditions
- <triggered, and why> | none triggered

## Cleaned text
<the text, de-identified>
```

Keep the log. **If anyone ever questions what you published, it is the record.**

## Example Invocation
`/deidentify @draft-post.md`
`/deidentify` — then paste the text
`/deidentify @case-study.md — I worked at <company>, the customer was <name>`
