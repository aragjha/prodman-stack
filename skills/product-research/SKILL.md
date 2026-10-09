---
name: product-research
description: Turn a product question into an evidenced research map a decision can be made from. Writes your ground truth first — the decision, the belief, what would change your mind — then looks at the question from eight angles, opens the sources instead of quoting snippets, marks every claim by how it was verified, and ends in a verdict on the belief and one next step. Run it before a feature, a roadmap bet, a positioning call or a build-vs-buy. Refuses to research with no decision attached.
disable-model-invocation: false
user-invocable: true
---

# /product-research — the research that argues against you

**Most AI research agrees with you.** Tell a model what you believe before it searches and it is
measurably more likely to confirm it (Wang et al., *When Truth Is Overridden*, arXiv 2508.02087:
"first-person prompts ('I believe...') consistently induce higher sycophancy rates than
third-person"). This skill is built to do the opposite: it writes down what would prove you wrong,
goes looking for that first, and ends in a verdict on your belief.

Most product research fails before it starts. Nobody wrote down what decision it was for, so it
cannot be wrong — and a document that cannot be wrong changes nothing. It gets filed under
*interesting*, the decision gets made on the three anecdotes everyone already had, and the research
is cited afterwards as support.

This skill does the opposite, in a fixed order. **Ground truth first. Then angles. Then sources —
opened, not quoted. Then a verdict on the belief you started with.** If there is no decision, it
stops and asks.

## When to Use
- Before a feature, a roadmap bet, a positioning choice, a pricing call, a build-vs-buy.
- When you have three anecdotes and a planning meeting.
- When a deep-research tool gave you 4,000 words and you still do not know what to do.

## Inputs
- The question, in a sentence.
- The decision it feeds, the belief you hold, and what would change your mind. **If you do not give
  the decision, the skill asks once — it will not search without one.** A missing belief or
  falsifier it drafts itself, marks *unconfirmed* in section 0, and proceeds. Only the absence of a
  decision stops the run.
- Optional: your goal or OKR doc, what you already know, sources you already trust or distrust.

---

## Process

### 1. Ground truth, before the first search
Write it back in under a page and get it confirmed:

| Field | What it must say |
|---|---|
| **Decision** | What will be chosen differently depending on what is found. Build · buy · position · price · enter · kill |
| **Goal it serves** | The number that is supposed to move, from your own strategy — never the web's |
| **Belief** | What the user currently thinks is true, **written in the third person** (*"The PM believes ops leads want…"*, never *"I believe"*), in one sentence a stranger could disagree with. Split a compound belief into **B1 / B2** here |
| **Falsifier** | What finding would make you drop the belief. **A belief that cannot lose is not a belief; it is a conclusion waiting for footnotes** |
| **Already known** | What you have already seen, so the run does not re-find it |

**Stop condition.** If the user cannot say what decision this feeds, **stop and ask once.** Research
with no decision attached produces a document that agrees with whoever reads it. If they still
cannot say, offer the angle map (step 2) and nothing below it.

**The "prove it" request.** If the decision is already made and the user wants supporting evidence
only, say plainly that the map will contain what contradicts the belief, in its own section, so they
can choose what goes on a slide. The map is complete; the deck is theirs. **Then run.** Draft the
missing belief and falsifier yourself and mark them *unconfirmed*; do not send the user a form.

**One question, at most, in the whole run.** The skill asks when the decision is missing. Every
other gap is drafted, marked *unconfirmed*, and confirmed in the map rather than by asking.

### 2. The angle map — show it, then let them cut
Eight angles. Each is a question the map must answer or explicitly report empty. Write the search
keys before searching: **problem phrase + platform + company + angle word.**

| # | Angle | The question it answers | Where the honest answer lives |
|---:|---|---|---|
| 1 | **Goal** | Which number moves, and by how much would it have to move to matter? | Your own numbers. Ask for them; never substitute the web's |
| 2 | **Lay of the land** | Who is in this space, what shape is it, where is it moving? | Company sites, pricing pages, changelogs, launch posts, funding announcements |
| 3 | **The users' words** | How do they phrase the pain, unprompted? | Reddit, Hacker News, community forums, app-store reviews, support forums, X — verbatim only |
| 4 | **Offerings, and evidence of use** | What exists — paid, free, open source — and is it actually used? | GitHub stars *and* last commit, review counts, changelog cadence, a pricing tier that exists because someone pays for it |
| 5 | **Method — the PM canon** *(never cut)* | Which PM frameworks, books and strategies apply to this decision, and what do they predict? | The book and the chapter, named and applied: *Continuous Discovery Habits* (opportunity solution tree), *The Mom Test*, *Inspired* / *Empowered*, JTBD (*Competing Against Luck*), Kano, *Obviously Awesome* (positioning), *Crossing the Chasm*, RICE / ICE, North Star, *Escaping the Build Trap*, Shreyas's LNO, Lenny's benchmarks — cited, not vibed |
| 6 | **Cases — good, bad, ugly** | Who did this before, and what happened? | Post-mortems, teardowns, conference talks, case studies with numbers, *"we shut it down"* posts |
| 7 | **Constraints** | What limits the options — regulation, platform rules, data, cost? | Official docs, regulator pages, platform policies |
| 8 | **Distribution** | Where would we reach these people? | The same rooms as angle 3, newsletters, events, the repos they star |

**Show the map and the keys before searching.** The user cuts angles that do not bear on the
decision. Eight full angles for a decision that needed three is not thorough; it is expensive.

**Read `FRAMEWORKS.md` (this skill's folder) before writing angle 5.** It says what each framework
predicts and the misuse to avoid — Kano is measured from customers, never from competitor counts; the
Mom Test is an interview method, not a theory. Each angle-5 row: *framework · what it predicts here ·
what the evidence says · agrees / disagrees*.

**The canon is the spine, not an angle you can cut.** A PM trusts a map that speaks their language.
Angle 5 is never cut, and every other angle's **Insight** names the framework it is read through —
*"through JTBD, the job here is…"*, *"Kano: this is a basic, so its absence costs, its presence
earns nothing"*. Name the framework, say what it predicts, then say whether the evidence agrees. A
framework name with no prediction is decoration.

### 3. Search, and open
The one rule: **a search snippet is not a source.** Open the page. If it cannot be opened, say so.

**Search against the belief first.** Write the contradicting search keys before the confirming ones
(*"<feature> nobody used"*, *"<feature> shut down"*, *"<claim> wrong"*, *"why we stopped <X>"*)
and run them first. Read the belief out of your working notes while you collect; look at it again
only in step 5.

Every claim carries a mark:

| Mark | Means |
|---|---|
| **HIGH** | You opened the page and read the thing itself. URL and date read are recorded |
| **MEDIUM** | A credible secondary source, named and linked — the press release of a paywalled report, a reputable roundup |
| **ZERO** | Could not verify. Say so and move on. **Never round up because the claim is convenient** |
| **NONE** | Searched, nothing found. The search string is the source; no URL; the date read is still recorded. Never mark an empty search HIGH |
| **ASK** | From the user, not the web — angle 1's numbers, anything only they hold. No URL; the row says what was asked for |

Rungs that work, so you do not re-climb dead ones:

| Lane | Use | Avoid |
|---|---|---|
| Reddit | A public archive API — search by subreddit, term and date | `reddit.com` and `old.reddit.com` directly; usually blocked |
| Hacker News | The Algolia search API, no key needed | — |
| Quora | `site:quora.com` search — the question titles are the asker's own words | Fetching page bodies; they return 403 |
| GitHub | The repo page: stars, last commit, open issues, README | Star counts alone. A 20k-star repo with no commit in a year is a museum |
| Reviews | App stores and public review pages, opened and read | Anything behind a login |
| Reports | The press release, marked MEDIUM — plus your own arithmetic from open data where you can | Quoting a paywalled headline number as HIGH |
| YouTube · Medium · talks | Search for the case, then open the write-up or the public transcript and quote it | Summarising from the title and the thumbnail. A talk you did not open is a snippet |

Capture **verbatim** to `SOURCES.md`: angle · quote · URL · date read · engagement · mark. A
paraphrase is not evidence. A quote is.

**Then prove the quotes are verbatim.** A page-reading tool returns a model's version of the page,
not the page; three scoreboard rounds failed on quotes that were almost exact. Before step 4, run
`python3 verify_quotes.py SOURCES.md` (in this skill's folder). It fetches each raw page and string-
matches every quote. For each line it reports: **MISMATCH** → fix the quote from the raw text, or
downgrade the row to MEDIUM and drop the quotation marks · **CUT** → add the "…" where the quote starts
or ends mid-sentence · **UNREACHABLE** (JavaScript-built page) → MEDIUM, unless you read the text from
an API or JSON endpoint the row names. The output goes in section 4. Then run `python3 verify_quotes.py --crosscheck MAP.md SOURCES.md` and the same for
RESPONSE.md: every quote in the map or the message must appear, character for character, in SOURCES.md. Never
re-cut a quote while writing the map; an ellipsis may only stand where whole sentences or list items were left out.

**Patterns need three.** A claim that something is *common*, *a trend* or *what most people do*
needs three independent sources. Fewer is a *weak signal*, labelled as such. **Adjacent evidence** —
engineers describing a problem you are researching for PMs, a US market standing in for an Indian
one — is allowed only in its own rows, labelled *adjacent*, never merged with direct evidence.

**Nothing here is a finding.** An angle that returns nothing is reported as *"nothing found —
searched X, Y, Z on <date>."* That sentence is often the most valuable one in the map — and it is
only a finding when the search is shown.

### 4. Build the map
One document, `MAP.md`. Section 1 is the overview — everything found around the question, on one
screen. Below it, one section per angle: the approach, why it was taken, the index of what was
found, what can be extracted, and the insight — each with its impact on the belief.

**Every finding answers two questions, in two columns.** First, **Belief:** exactly one word —
`confirms` · `contradicts` · `unknown` — against the belief from step 1, every row, no dashes, no
other word. *Weak*, *adjacent*, *trust*, *counter-signal* are qualities of the evidence: they go in
**Mark** or **Also changes**. A finding that does not bear on the belief is `unknown`. A compound
belief is split into B1 / B2 in section 0, and each row names which one it judges. Second, **Also
changes:** the decision, the build, the method, the next step — or nothing. A consequence for the
build written where the belief status should be is the most common way a map stops being a map.
An insight with no stated impact is a fact with nowhere to go, and it does not go in the map.

### 5. Close against the ground truth
**Sweep by text, not by label — and leave the table.** Write `### Sweep` at the top of section 3 with one
line per section-2 row: `<id> · weakens? yes / no · cited in verdict? yes / dropped because …`. A verdict with
no Sweep table fails.  Re-read every section-2 row's *Finding* and *Also changes* text and ask:
does this weaken, limit or complicate the belief, whatever its label says? Relabel any that do — the
labels were written while the belief was in your head, which is when agreement bias lands.

**List first, then judge.** Before writing a word of the verdict, list by id every section-2 row whose
**Belief** column says *contradicts* (including weak or adjacent ones, which say so in **Mark** or
**Also changes**, never in Belief). The *Contradicting evidence* line must cite every id on that list, or say which one
was dropped and why. **The verdict may never cite fewer contradicting rows than section 2 labelled.**
A verdict built from memory of the map is the failure this skill exists to prevent; it happened on
the first scoreboard's control, with every fact in the map correct. Write **Dropped:** with the ids
you left out and why — *"Dropped: none"* is allowed only after that explicit line.

The verdict, in this order:

1. **The belief:** confirmed · contradicted · still unknown — and the three findings that decided it.
2. **The falsifier:** did it fire? One line.
3. **Contradicting evidence**, listed, not buried. If there is none, say *none found* and name what was searched.
4. **Top three insights** ranked by impact on the goal — not by how interesting they were.
5. **Next step** — one sentence, no "and", no "plus". Exactly one of: *decide* (the decision can be made now) · *spec* (the question is
   answered; write it) · *one named gap* (precisely what is still unknown, and where to look).
   Never *"more research needed."* **If the decision would reverse on a number the map does not
   have, the step is *one named gap* — that number — not a *decide* with a caveat. Never both.**
**RESPONSE.md repeats the verdict's next step word for word and adds no new ask.** The user message is the
verdict in plain words, never a second verdict.

6. **Other gaps — not needed for this decision:** everything else still unknown goes here, on its
   own line, so the next step can stay one sentence.

Then the self-check: the auto checks from the VERIFY block, with actual values. **It is not a
scoreboard** — a run grading itself is a claim, not a check — but it makes the claim auditable.

---

## VERIFY
**Rung:** Observer — target Advisor, earned when the golden set scores ≥ 4/5, never declared ·
**Irreversible?** no — a map is a document. The decision it feeds may not be, which is why check 7
exists.

| # | Check | How it is checked | Type | Fails if |
|---:|---|---|---|---|
| 1 | Ground truth before search | Decision, belief and falsifier are written and timestamped earlier than the first `SOURCES` row | auto | missing, or written after |
| 2 | Every claim is sourced and marked | Each `MAP` finding cites a `SOURCES` row carrying HIGH / MEDIUM / ZERO / NONE / ASK | auto | any finding without both |
| 3 | No snippet-sourced HIGH | Every HIGH has a URL and a date read | auto | a HIGH without them |
| 4 | Patterns need three | Any *common / trend / most* claim cites ≥ 3 independent sources, or is labelled weak signal | auto | a pattern on fewer than 3, unlabelled |
| 5 | Empty angles reported | Every angle on the map has findings or *"nothing found — searched …"* | auto | an angle silently dropped |
| 6 | Every insight states its impact | confirms / contradicts / unknown, against the belief | adversarial | an insight with no consequence; *"interesting"* with nowhere to go |
| 7 | The verdict is honest | Every row section 2 labelled *contradicts / weak confirm / trust / counter-signal* is cited in section 3, or its dropping is explained | adversarial | the belief is rounded up; a labelled row exists and section 3 omits it |
| 8 | Ends in a step a decision can take | decide · spec · one named gap | adversarial | ends in *"more research needed"* |
| 9 | Grounded in the PM canon | Angle 5 is present and not cut; ≥ 3 named frameworks or books, each with what it predicts and whether the evidence agrees | adversarial | angle 5 cut; frameworks name-dropped with no prediction; a map a PM would not recognise as PM work |

**Red flags (any one = rung 0):**
- **An invented source, quote or number.** Over-claiming counts: a snippet reported as an opened
  page is an invented read.
- **Searching before the ground truth is written.** It is the default behaviour of every
  deep-research tool, and the one this skill exists to refuse.
- **Rounding ZERO up** because the claim is convenient or the user is presenting it on Thursday.
- Getting behind a login or past an anti-bot wall for the *"actual"* data. Public pages, official
  APIs, RSS and permitted scraping only. The user wanting the quotes does not change this.

**Rollback:** delete the research folder. Nothing outside it is written.

---

## Output Format

```
research/<YYYY-MM-DD>-<slug>/
├── MAP.md          ← the map
└── SOURCES.md      ← every quote, verbatim · URL · date read · engagement · mark
```

`MAP.md`:

```markdown
# Research map — <question> — <date>

## 0 · Ground truth (written <timestamp>, before the first search)
**Decision:** … · **Goal it serves:** … · **Belief:** … · **Falsifier:** … · **Already known:** …

## 1 · The map
<everything found around the question, on one screen>
| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |

**Cases to follow:** the three worth copying — what they did · good · bad · ugly · source

## 2 · Angles
### <angle> — <approach · why this angle · what was searched>
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
**Insight:** <one sentence> · **Belief:** confirms · contradicts · unknown · **Also changes:** …
<or: nothing found — searched …, on <date> (a NONE row in SOURCES)>

## 3 · Verdict
**Belief:** confirmed · contradicted · unknown — because …
**Falsifier:** fired · did not fire
**Contradicting evidence:** … | none found — searched …
**Top three, by impact on the goal:** 1 … 2 … 3 …
**Dropped:** <ids and why> | none
**Next step:** decide · spec · one named gap — <one sentence>
**Other gaps — not needed for this decision:** …

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
```

`SOURCES.md` — this header, every row, no other layout:

```markdown
| S# | Angle | Verbatim | URL | Date read | Engagement | Mark |
|---|---|---|---|---|---|:--:|
| S1 | 3 | "<the quote, untouched; cuts shown with …>" | https://… | 2026-10-09 | 35 pts · 14 comments | HIGH |
| S2 | 2 | searched: "<the exact search string>" | — | 2026-10-09 | — | NONE |
| S3 | 1 | asked the user for: <what> | — | 2026-10-09 | — | ASK |
```

**Quotation marks are for source text only.** Beliefs, labels, your own phrasing go in *italics*, never in quotes.

**Verbatim means verbatim.** Inside quotation marks, nothing is cut without an ellipsis, and never
mid-clause. The first scoreboard's one red flag was nine words silently removed from a quote.

**Size:** a map a PM can read and cut in 60–90 minutes of attention. Past eight pages it has
stopped being a map.

## Example Invocation
`/product-research should we build AI meeting notes into our scheduling product — decision is this vs the sync-reliability work, belief is ops leads want it, falsifier is no unprompted public demand`
`/product-research @ground-truth.md`
`/product-research` — then answer the four questions
