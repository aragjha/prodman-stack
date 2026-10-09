# Research map — "AI skills for PMs" vs "the eval layer for PMs who ship AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09 16:05 IST, before the first search)
**Decision:** Position the landing page as **(A) "AI skills for PMs"** or **(B) "the eval layer for PMs who ship AI features."** Position choice, made this week.
· **Goal it serves:** a landing-page positioning picked this week. The number it is meant to move is **not given**: drafted as *landing-page visitor → free-repo signup rate, and free → paid conversion on the memory + evals layer*, current baselines unknown. *Unconfirmed* (S1, ASK).
· **Belief (split, as given):**
  - **B1:** PMs who have shipped an AI feature have a measurement problem they can name in their own words.
  - **B2:** Nobody is selling them (PMs specifically) a fix.
· **Falsifier (as given):** B2 drops if people are already selling evals to PMs. B1 drops if PMs don't describe measurement as a problem anywhere in their own words.
· **Already known:** the product exists as a free repo of Claude Code skills plus a paid memory + evals layer. Nothing else stated. No prior research on competitors or user language given.

**Search keys (problem phrase + platform + company + angle word):**
- Angle 2/4: "AI evals course product managers" · "evals for PMs" Maven · "Lenny's AI evals" · Braintrust / Arize / LangSmith / Humanloop pricing · "Claude Code skills product managers" GitHub
- Angle 3: HN Algolia "evals product manager" · Reddit r/ProductManagement "evals" / "how do you measure AI feature" · "hard to evaluate LLM feature PM"
- Angle 5: Obviously Awesome (competitive alternatives, market category), Crossing the Chasm (beachhead), JTBD, Kano
- Angle 6: Hamel Husain / Shreya Shankar evals course numbers · Aakash Gupta / Lenny evals posts
- Angle 7: platform constraints (Claude Code skills format, open distribution)
- Angle 8: Lenny's Newsletter, Maven, Product Hunt, r/ProductManagement

Angle map shown in full; no angle cut (user asked for the map, "the users' language, who sells into this, what they charge" = angles 2, 3, 4 primarily; 1, 5, 6, 7, 8 run light).

## 1 · The map
Two candidate positions, two very different markets. **"AI skills for PMs" is a free, crowded shelf** (a 7.2k-star free repo, a 1.4k-star Lenny repo, Aakash's $49 PM OS). **"Evals for PMs" is a paid category that already exists**, with at least five sellers naming PMs as the buyer, priced $399 to $4,200, the leader showing 1,017 reviews, plus a $249/month tool vendor writing "evals for PMs" content. What we did *not* find: a PM-facing eval layer that runs inside Claude Code. The pain in PMs' *own* words is thin (two direct sources). Most "PMs can't measure their AI" language is seller copy.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| PMs who have shipped an AI feature | "I didn't need anything fancy, just 'did the agent answer the question'" (S13) · "There's no one size fits all for evals" (S14) | Spreadsheets, "Gemini in Google Sheets" (S13); courses $399–$4,200 (S2–S6); Braintrust $0/$249 (S8) | A *doing* tool, not a course, that a PM runs without engineering. Weak signal: one PM built their own (S13) | Maven (S2, S4, S6), Lenny's Newsletter / podcast (S15, S24), Sharebird (S14) |
| PMs using Claude Code (position A) | none found in their own words. Seller copy only (S11, S12) | Free repos: deanpeters 7,214★ (S10), Lenny 1,381★ (S9), aakashg 160★ (S11) | Not much. The shelf is full and free. Paid ceiling seen: $49 (S12) | GitHub, Aakash's and Lenny's newsletters |
| *Adjacent:* engineers / AI teams | "evals are hard" (S17) · "20% instrument LLM observability from day 1" (S16) | Braintrust (S8), LangWatch MCP in Claude Code (S27) | Not the PM. Shown only as context | HN |

**Cases to follow:**
- **Hamel Husain & Shreya Shankar, "AI Evals For Engineers & PMs"** — a course that names PMs as buyers. *Good:* $4,200 with 1,017 reviews (S4). *Bad:* teaching only, it hands you no running tool. *Ugly:* the leader is huge, so anything framed "evals for PMs" gets compared to it. Source S4, S15.
- **Aakash Gupta, pm-claude-code-setup → PM OS** — the same free-repo-plus-paid shape as yours. *Good:* clean funnel from free repo to paid (S11). *Bad:* the paid tier is $49 one-time (S12) and the repo has 160★. *Ugly:* no evals and no memory, so nothing ongoing to charge for. Source S11, S12.
- **Beval (a PM-built eval tool)** — *Good:* exactly the "doing" job (S13). *Bad:* 2 points on Show HN. *Ugly:* HN is the wrong room for PMs, and we found no traction anywhere. Source S13.

## 2 · Angles
Belief split from section 0: **B1** = PMs who shipped AI can name a measurement problem. **B2** = nobody sells them a fix. Each row says which one it judges.

### 1 Goal — approach: ask; the web cannot supply this
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | [B1/B2] The number this positioning moves and its baseline were not given | S1 | ASK | unknown | The verdict can pick a position, but it can't size the win. Set a signup-rate target before launch |
**Insight:** read through North Star: without a stated input metric, "pick the positioning" can't be scored afterwards · **Belief:** unknown · **Also changes:** add the metric to the landing-page brief.

### 2 Lay of the land — approach: vendor blogs and newsletters framing "evals for PMs"; searched "evals for product managers", "Beyond vibe checks", "Claude Code skills for product managers"
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | [B2] Braintrust, an eval-tool vendor, publishes a dedicated "Evals for PMs" guide. PMs are already a marketing target | S7 | HIGH | contradicts | A paid tool vendor is already courting PMs |
| 2.2 | [B1] "Most AI features ship without a structured way to measure quality" and "you are flying blind" are claims by sellers and commentators, not by PMs. The S18 piece cites no data | S7, S18, S25 | HIGH | unknown | Use as category framing, not as proof of pain (Mom Test) |
| 2.3 | [B2] Productboard, a PM-tool vendor, calls evals "the defining skill" but sells no evals product | S25 | HIGH | confirms | PM-tool incumbents have not built it into a product (yet) |
| 2.4 | [B2] Lenny's Newsletter ran a paid "PM's complete guide to evals" (Apr 2025) | S24 | MEDIUM | contradicts | The biggest PM room already sells this content |
**Insight:** through *Obviously Awesome*, the market category "evals for PMs" has already been named and claimed by vendors and media. You would be entering a category, not creating one · **Belief:** contradicts (B2) · **Also changes:** landing copy cannot say "nobody is selling this".

### 3 The users' words — approach: HN Algolia, Reddit archive APIs, site:reddit / site:quora, Sharebird, first-person PM posts
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | [B1] A PM, unprompted, describes wanting "quick and dirty" evals on traces and being "blocked by 'Gemini in Google Sheets'" | S13 | HIGH | confirms | Weak signal (one source, 2 pts). The job is *doing*, not learning |
| 3.2 | [B1] A Google GPM says evals have to be defined per problem, and treats defining them as the PM's own job | S14 | HIGH | confirms | Weak signal. The PM owns "what good is", which supports a PM-run layer |
| 3.3 | [B1] *Adjacent:* a vendor's LinkedIn poll found only 20% instrument LLM observability from day 1 | S16 | HIGH | confirms | Adjacent (teams, vendor poll, n unknown). Not merged with direct evidence |
| 3.4 | [B1] *Adjacent:* engineers say "evals are hard" | S17 | HIGH | confirms | Adjacent (engineers) |
| 3.5 | [B1] Reddit r/ProductManagement could not be reached. The archive APIs refused agents and were not bypassed | S19 | ZERO | unknown | The largest PM voice source is unread. Does not change the decision: B1 already holds without it |
| 3.6 | [B1] Nothing found: site:reddit, site:quora, HN PM-voice queries, and a first-person PM evals post contained no further measurement-pain statements | S20, S21, S29, S30 | NONE | unknown | Own-words volume stays a weak signal |
**Insight:** through *The Mom Test*, most of the "PMs can't measure" language is sellers describing their buyer. Only two PMs said it themselves. The B1 falsifier did not fire, but the evidence is thin · **Belief:** confirms (B1, weak) · **Also changes:** hero copy should borrow S13's phrasing ("did the agent answer the question"), not seller phrasing.

### 4 Offerings, and evidence of use — approach: open each course and pricing page, plus gh api for repo stars and last push
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | [B2] "AI Evals For Engineers & PMs": $4,200, 4.7/5 from 1,017 reviews | S4 | HIGH | contradicts | Category leader. Shows engineers and PMs pay for measurement training (reviews are not split by role) |
| 4.2 | [B2] Product School "AI Evals Certification": $2,999, targets PMs | S3 | HIGH | contradicts | Price anchor |
| 4.3 | [B2] Tailabs "AI Evals Bootcamp for Product Leaders and PMs": $399, 8 reviews | S2 | HIGH | contradicts | Low-end price anchor |
| 4.4 | [B2] Reforge "AI Evals" for PMs, membership, live from Oct 21 2026 | S5 | HIGH | contradicts | Fresh entrant this month |
| 4.5 | [B2] Marily Nika "AI Evals for PMs Certification", 21 reviews, for "'ship or hold' calls" | S6 | HIGH | contradicts | The JTBD phrase to use |
| 4.6 | [B2] Braintrust, a tool, $0 Starter / $249 per month Pro | S8 | HIGH | contradicts | The tool exists, built for engineers but marketed to PMs (2.1) |
| 4.7 | [B2] The free Lenny skills repo (1,381★, pushed 2026-07-16) ships an "AI Evaluation Strategy" skill for Claude Code | S9 | HIGH | contradicts | A free evals *skill* for PMs already sits in your exact surface |
| 4.8 | [B2] The PM-skill repos with the most stars have no eval layer: deanpeters (7,214★) has no eval skill, Aakash's PM OS mentions no evals | S10, S12 | HIGH | confirms | The opening is a running eval *layer*, not another skill |
| 4.9 | [B2] *Adjacent:* LangWatch MCP puts evals inside Claude Code, aimed at engineers. A "PM evals" training repo has 2★ | S27, S23 | HIGH | unknown | The in-Claude-Code surface is technically proven but has no PM-facing product |
| 4.10 | [B1/B2] Position A's shelf: free repos at 7,214★ / 1,381★ / 160★, and the only paid tier seen is $49 one-time | S9, S10, S11, S12 | HIGH | unknown | Position A has a $49 ceiling and a free 7k-star incumbent |
| 4.11 | [B2] Two more Maven "evals for PMs" courses appear in search but returned 404 | S28 | ZERO | unknown | Not counted |
**Insight:** Kano. "Skills for PMs" is now a *basic*: free and everywhere, so its absence costs you and its presence earns nothing. "Evals" is a *performance* attribute, with five sellers and 1,017 reviews at $4,200. Pattern holds on ≥3 sources (S2–S6) · **Belief:** contradicts (B2) · **Also changes:** the paid layer can be priced against $399–$4,200 courses, not against $49.

### 5 Method — the PM canon (never cut)
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | [B2] **Obviously Awesome (Dunford), competitive alternatives → market category.** Prediction: A is judged against free repos (S10) and $49 (S12). B is judged against $399–$4,200 courses (S2–S4) and $249/mo tools (S8). Evidence agrees: B is an existing, paid category | S2, S3, S4, S8, S10, S12 | HIGH | contradicts | Choose B, framed against the alternative: "the eval layer, not another course" |
| 5.2 | [B2] **Crossing the Chasm (Moore), beachhead.** Prediction: pragmatists buy from the category leader, so a newcomer has to win a narrow niche. Evidence: the leader is S4. No PM-facing eval layer inside Claude Code was found (4.8, 4.9) | S4, S9, S23, S27 | HIGH | unknown | Beachhead = PMs already working in Claude Code who shipped an AI feature |
| 5.3 | [B1] **JTBD (Christensen, *Competing Against Luck*).** Job: "make a ship-or-hold call I can defend" (S6), against "a dashboard nobody trusts" (S2). Prediction: courses get hired to *learn*, tools to *do*. Evidence: the PM in S13 built a tool because nothing did the job | S2, S6, S13 | HIGH | confirms | Sell the call ("ship or hold"), not the skill |
| 5.4 | [B1] **The Mom Test (Fitzpatrick).** Prediction: seller copy makes the pain look bigger than users' own words show. Evidence agrees: 4 seller sources against 2 PM sources | S2, S3, S7, S18, S13, S14 | HIGH | unknown | Run a few real PM conversations before trusting the hero line |
| 5.5 | [B1/B2] **Kano**, applied in angle 4: skills = basic, evals = performance | S4, S10 | HIGH | unknown | Position A cannot carry the paid layer |
**Insight:** all four frameworks point the same way. B is the positioning that can carry a paid layer, but only as a niche inside an existing category, not as a category nobody sells · **Belief:** contradicts (B2) · **Also changes:** positioning copy and pricing anchor.

### 6 Cases — approach: course pages, creator product pages, Show HN, post-mortem search
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | [B2] Hamel & Shreya built the #1 evals course and say they trained 2,000+ PMs and engineers (podcast, Sep 2025). The page now claims 5,000+ | S15, S4 | MEDIUM | contradicts | Proof of demand, and the comparison you will face |
| 6.2 | [B1/B2] Aakash: free repo (160★) → $49 PM OS, no evals | S11, S12 | HIGH | unknown | The ceiling for position A |
| 6.3 | [B2] Beval, a PM-built eval tool, got 2 pts on Show HN | S13 | HIGH | unknown | A doing-tool for PMs exists, but its pull is unproven. The room matters |
| 6.4 | [B1/B2] Nothing found: no PM post-mortem of shipping AI "blind" | S26 | NONE | unknown | — |
**Insight:** through *Escaping the Build Trap*, the winning case sells an outcome (confidence to ship) and the capped case sells outputs (more commands) · **Belief:** contradicts (B2, via 6.1) · **Also changes:** price the paid layer as an outcome.

### 7 Constraints — approach: Claude Code docs, repo licences
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | [B1/B2] Skills are plain `SKILL.md` files shared by committing `.claude/skills/` to git, so whoever has the file can copy it | S22 | HIGH | unknown | The paid memory + evals layer has to be a hosted service or state, not more skill files |
| 7.2 | [B1/B2] deanpeters' repo is CC BY-NC-SA 4.0 (non-commercial) | S10 | HIGH | unknown | Can't bundle it into the paid layer |
**Insight:** read as RICE effort, B's paid layer needs a service. A's doesn't, but A has nothing defensible to charge for · **Belief:** unknown · **Also changes:** build scope for the paid tier.

### 8 Distribution — approach: where the sellers and the voices in angles 3–4 sit
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | [B1/B2] Maven is where evals-for-PM courses sell (3 courses opened) | S2, S4, S6 | HIGH | unknown | The audience gathers there. A free eval skill could be a Maven lightning lesson |
| 8.2 | [B1/B2] Lenny's Newsletter / podcast is the main room (guide, podcast, skills repo) | S9, S15, S24 | HIGH | unknown | Get the evals layer listed beside lenny-skills |
| 8.3 | [B1/B2] HN is not a PM room: 2–3 pts on PM evals posts | S13, S24 | HIGH | unknown | Weak signal. Don't launch on Show HN |
| 8.4 | [B1/B2] Reddit unread (blocked) | S19 | ZERO | unknown | Unread. Matters for distribution, not for this decision |
**Insight:** through *Crossing the Chasm*'s word-of-mouth rule, the beachhead's rooms are Maven and Lenny, both already full of eval sellers. You'd be distributing into your competitors' rooms · **Belief:** unknown · **Also changes:** launch channel.

## 3 · Verdict
**Rows labelled contradicts in section 2:** 2.1, 2.4, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 5.1, 6.1 (11 rows, all B2). None on B1.

**Belief:** **contradicted.** B2 is contradicted. B1 is confirmed, but weakly. Decided by: (1) 4.1, a $4,200 "AI Evals For Engineers & PMs" course with 1,017 reviews; (2) 4.7, a free evals skill for PMs already in Claude Code (lenny-skills); (3) 3.1 and 3.2, the only two PMs found naming the problem in their own words.
**Falsifier:** **fired** for B2 ("people selling evals to PMs already": five courses, one tool, one free skill). Did **not** fire for B1: PMs do describe it, but the evidence is a weak signal of two.
**Contradicting evidence:** 2.1 Braintrust's evals-for-PMs guide · 2.4 Lenny's paid PM evals guide · 4.1 Hamel & Shreya $4,200 · 4.2 Product School $2,999 · 4.3 Tailabs $399 · 4.4 Reforge AI Evals · 4.5 Marily Nika certification · 4.6 Braintrust $0/$249 · 4.7 lenny-skills evals skill · 5.1 Obviously Awesome: evals for PMs is an existing paid category · 6.1 2,000–5,000+ trained by the category leader. None dropped.
**Top three, by impact on the goal:**
1. **Position A has a $49 ceiling.** It sits against a free 7,214★ incumbent (4.10, 6.2), so it can't carry a paid memory + evals layer.
2. **Position B is a real paid category, priced $399–$4,200, but it's taken for "learning evals."** The open slot is a PM-run eval *layer* inside Claude Code (4.8, 4.9, 5.2). "Nobody sells this" must come off the page.
3. **The pain's hero language should be PM words, not seller words:** "did the agent answer the question", "ship or hold" (3.1, 4.5, 5.3). Own-words evidence is thin, so treat the hero line as a test.

**Next step: decide.** Position as B, reframed: *"the eval layer for PMs who ship AI features: runs in your Claude Code, not another course."* The free skills repo becomes the on-ramp, not the headline. This doesn't hinge on a number the map lacks. Even if A drew more signups, its paid ceiling (4.10) wouldn't fund the paid layer. The landing page is reversible.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09 16:05 IST, before the first search (S2 onward) |
| 2 Every claim sourced and marked | 37 section-2 rows, each with an S# and a mark |
| 3 No snippet-sourced HIGH | 20 HIGH rows in SOURCES, each with a URL and date read. Search-only or paywalled items marked MEDIUM (S15, S24) |
| 4 Patterns need three | "evals for PMs is a sold category": S2–S6 (5). "PM skills shelf is free and crowded": S9, S10, S11 (3). "Maven is the room": S2, S4, S6 (3). PM own-words pain: labelled weak signal (2) |
| 5 Empty angles reported | All 8 angles have rows. NONE/ZERO rows: S19, S20, S21, S26, S28, S29, S30 |
| 6 Every insight states impact | 8/8 angle insights carry Belief and Also changes |
| 7 Verdict honest | 11 contradicting rows labelled, 11 cited, 0 dropped |
| 8 Ends in a step | decide |
| 9 PM canon | Obviously Awesome, Crossing the Chasm, JTBD, Mom Test, Kano, Escaping the Build Trap, North Star, RICE. Each states a prediction and whether the evidence agrees |
