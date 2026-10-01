---
name: portfolio-from-work
description: Turn a PM's existing, confidential work into de-identified case studies, one working artifact, and a portfolio page they can actually send. Use when a PM has years of shipped work they cannot show.
disable-model-invocation: false
user-invocable: true
---

# /portfolio-from-work

Takes what a product manager remembers and is allowed to keep, and produces something they can send to a recruiter today. Works from memory — it does not require the original documents, because in most cases the PM no longer has access to them and would not be free to publish them if they did.

## When to Use
- A PM has shipped real work for years and has nothing demoable.
- They are interviewing, or about to be, and every portfolio they see belongs to a designer.
- They want to show AI capability using their **own** domain rather than a tutorial to-do app.

## Inputs
- Nothing mandatory. The skill interviews.
- Optional: a CV, an old deck, a sanitised doc, a list of projects. Helpful, never required.

## Process

### 1. Inventory — what is there
Ask for **three to five projects from the last three years**, one line each. Do not ask for documents. For each, get only:
- what the product did, in one sentence a stranger would understand
- what was broken or missing before
- what they personally decided (not what the team delivered)
- roughly what changed afterwards

If they cannot name what they personally decided on a project, **drop it.** A project where the PM cannot locate their own judgement makes a weak case study no matter how big it was.

### 2. The de-identification gate — runs before anything is written
This step is not optional and is not deferred to the end.

For every project, identify and replace:

| Strip | Replace with |
|---|---|
| Employer name | the category — "a B2B scheduling product", "a consumer fintech app" |
| Customer or client names | segment — "a mid-market logistics customer" |
| Exact revenue, ARR, user counts | shape and direction — "roughly a fifth", "low six figures", "high five-digit MAU" |
| Internal codenames, repo names, tool names that identify the employer | generic equivalents |
| Colleagues' names | roles — "the staff engineer", "our designer" |
| Regulated-domain specifics (health, financial, legal detail that identifies the business) | the general problem shape |

Then **show the PM a table of exactly what was stripped and what replaced it**, and ask them to confirm. Do not proceed on an assumption about what is safe.

**Stop conditions.** If any of these is true, say so and stop rather than guessing:
- The PM signed something specific they cannot recall the terms of
- The project is identifiable from the problem shape alone — a famous launch, a unique market
- A number is memorable enough to be traced back

Better a three-project portfolio that is safe than a five-project one that costs them a job.

### 3. Pick three that show range
Not the three biggest. Three that show **different kinds of judgement**:
- one where they **killed or cut** something — scope, a feature, a project
- one where they **chose between** two defensible options and were accountable for the choice
- one where they were **wrong** and changed course on evidence

The third is the one that gets replies. Most PM portfolios are a wall of wins and read as fiction. A PM who can describe being wrong precisely reads as senior.

### 4. Write each case study
One page each. This exact shape, because it is the shape an interviewer already thinks in:

```markdown
## <Project, described generically>

**The situation.** <2-3 sentences. The product, the market, the constraint.>

**The problem.** <What was actually broken. Evidence, not assertion.>

**What I decided.** <The call. First person. The alternative considered and why it lost.>

**What it cost.** <The trade-off. Every real decision has one. A case study without a
cost is marketing.>

**What happened.** <Direction and rough magnitude. "Roughly a fifth", never "18.3%".>

**What I would do differently.** <One specific thing. Not humility theatre.>
```

**Rules:**
- First person singular for decisions, plural for delivery. "I decided", "we shipped."
- No adjectives where a number would do; no fake numbers where a shape will do.
- Never invent a metric that was not measured. "We never instrumented it" is an acceptable and credible sentence.

### 5. Build ONE into a working artifact
Pick the single project whose core can be rebuilt in a few hours, with no employer data, using synthetic inputs. Then actually build it in Claude Code.

Good candidates: a prioritisation model, a research-synthesis flow, an eval harness for a decision they used to make by gut, a scoring tool, a dashboard over fabricated-but-realistic data.

Bad candidates: anything needing their employer's real data, real integrations, or more than a day.

**The artifact is the differentiator.** Three written case studies is a nice portfolio. Three case studies where one is a link that opens and works is a different conversation.

### 6. Assemble
Produce `outputs/portfolio/README.md`:
- a two-line intro that names what kind of PM they are and what they are looking for
- the three case studies
- the working artifact, linked, with one line on what it demonstrates
- how to reach them

## VERIFY
**Rung:** Advisor · **Irreversible?** **yes** in effect — a published portfolio cannot be
unpublished from the memory of whoever read it, and a leak cannot be walked back. Capped at
Advisor permanently: the skill drafts, the PM publishes.

| # | Check | How it is checked | Type | Fails if |
|---:|---|---|---|---|
| 1 | De-identification ran | The strip/replace table exists and was confirmed by the PM | auto | missing or unconfirmed |
| 2 | No employer or customer names | Grep the output against the names given in step 1 | auto | any appears |
| 3 | No precise unpublishable figures | No exact percentages, ARR, or user counts unless the PM confirmed they are public | auto | any exact figure lacks confirmation |
| 4 | Every claim is the PM's own | Each case study names a decision they personally made | adversarial | a team achievement is written as a personal decision |
| 5 | Nothing invented | Every fact traces to what the PM said in the interview | adversarial | a metric, date or outcome appears that was never stated |
| 6 | The cost is stated | Each case study has a real trade-off | adversarial | any reads as unbroken success |
| 7 | Nothing published | No file was pushed, posted or shared | auto | any publish occurred |

**Red flags (any one = rung 0):**
- An employer, customer or colleague name surviving into the output.
- A fabricated metric. In a portfolio this is not a quality bug, it is a lie told to a hiring manager.
- Any publishing action. The PM publishes. Always.

**Rollback:** delete `outputs/portfolio/`. If already sent, there is no rollback — which is why
check 1 gates everything and why this skill never publishes.

## Output Format
```
outputs/portfolio/
├── README.md              ← the portfolio page
├── case-studies/
│   ├── 01-<generic-name>.md
│   ├── 02-<generic-name>.md
│   └── 03-<generic-name>.md
├── artifact/              ← the one thing that runs
└── deidentification-log.md ← what was stripped, what replaced it, confirmed by whom
```

Keep `deidentification-log.md`. If anyone ever questions what was published, it is the record.

## Example Invocation
`/portfolio-from-work`
`/portfolio-from-work @cv.pdf — interviewing for senior PM roles at AI-first companies`
