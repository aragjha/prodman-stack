# Research map — positioning a free PM-skills repo: "AI skills for PMs" vs "the eval layer for PMs shipping AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09 19:36 IST, before the first search)
**Decision:** Position · the landing-page headline and copy for the free PM-skills repo, which ships this week. Option A is "AI skills for PMs". Option E is "the eval layer for PMs shipping AI features".
**Goal it serves:** email signups from the page. Target is 50 in week 1 (user's number, ASK).
**Belief:** The PM believes the eval framing will convert better than the skills framing, because it names a pain the skills framing doesn't. Split:
- **B1:** PMs in the lane describe evals as *their own* problem, in their own words.
- **B2:** no free repo or resource already owns the "evals for PMs" angle.
- **B3:** therefore E converts to signups better than A. The web cannot measure this. Only a test on the page can.
**Falsifier (user's):** no PM in the lane describes evals as their problem in their own words (fires B1), **or** a free repo already owns that angle (fires B2).
**Already known:** none stated. The repo exists and is free.

**Angle cuts:** angle 7 (constraints) was cut. No regulation or platform rule limits what landing-page copy can say. Angles 1–6 and 8 were run. Contradicting keys ran first, e.g. "evals hype overrated", "PMs don't need evals", "engineers should own evals" and "free evals repo for PMs".

## 1 · The map
Both positions already have a free incumbent. **"AI skills for PMs"** is owned outright by a 7,215-star repo (S8), with a 1,433-star challenger (S12). **"Evals for PMs"** is the lane's loudest theme. Lenny, Aakash, Braintrust and Arize all frame it as *the* new PM skill (S14–S17), which is a pattern on 4 independent sources. But the free eval-skills plugin that matters is engineer-framed (S10). The only PM-named eval repo has 4 stars (S9). In their own words, PMs describe eval pain only thinly: 2 first-person sources, which makes it a weak signal (S4, S5). The 2026 conversation has moved from "we have no evals" to "eval theatre": suites nobody can read, which no ship decision hangs on (S20, S18).

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| PM on a team shipping AI features | "wanting to do 'quick and dirty' LLM based evaluation on conversation transcripts and traces" (S4) | Gemini in Google Sheets, then hand-written OpenAI API calls in Python (S4) | A PM-sized way to run and read an eval | HN Show/Ask threads, small (S4, S7) |
| PM at a frontier lab | "Evals come up a lot these days for PMs." (S5) | Writing the eval spec themselves (S5) | n/a: this PM already owns it | personal blog, internal docs (S5) |
| PM who owns the launch call | "The product manager owns the launch. The engineer owns the meaning of the numbers." (S18, an engineer writing about PMs, *adjacent*) | Scorecards they cannot read (S18) | A translation from eval number to ship/hold decision (S18, S20) | not found in PM rooms (S2, S3) |
| PM learning AI | "AI evals is the most important new skill for PMs." (S15, influencer, not user) | $4,200 cohort course (S11), free newsletters (S14, S15), vendor workshops (S13) | A free, hands-on, PM-framed tool. S9 tries this and has 4 stars | Lenny's List, Maven, Substack (S11, S14, S15) |

**Cases to follow:**
1. **Hamel Husain + Shreya Shankar.** A paid course plus a free skills plugin. **Good:** 5,000+ students and a 1.5–1.7k-star free plugin (S10, S11). **Bad:** framed for coding agents and engineers. **Ugly:** a $4,200 price that most individual PMs will not expense. (S10, S11)
2. **Dean Peters.** One author, two framings. **Good:** the skills repo has 7,215 stars (S8). **Bad:** the evals-for-PMs repo has 4 stars after 3 months (S9). **Ugly:** stars are not signups, and the two repos differ in age and format. (S8, S9)
3. **The eval-theatre backlash.** **Good:** it names the live pain precisely (S20). **Bad:** "Most AI teams don't need evals" is being said loudly (S19). **Ugly:** a generic "eval layer" headline reads as more of the theatre. (S19, S20)

## 2 · Angles

### 1 · Goal — your number, not the web's
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | B3: the target is 50 signups in week 1. Expected visitors and baseline signup rate are not known | S1 | ASK | unknown | Without a visitor count, "converts better" cannot be tested this week. Through *North Star / inputs*, the input is signups per visitor, and that input is unmeasured |
**Insight:** through North Star / input metrics, 50 signups is an output. The decision turns on signups per visitor per headline, and nobody has that number yet · **Belief:** unknown · **Also changes:** the next step.

### 2 · Lay of the land — repo listings, influencer and vendor posts on evals for PMs
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | B3: "AI skills for PMs" is already owned by a free repo with 7,215 stars and 77 skills, plus a 1,433-star challenger | S8, S12 | HIGH | confirms | Option A launches into a category with a dominant free incumbent. That is weak evidence for B3, because stars are not signups |
| 2.2 | B1: influencers and vendors call evals *the* new PM skill. That is a pattern on 4 independent sources | S14, S15, S16, S17 | HIGH | unknown | Not users' words, so it cannot satisfy the falsifier. They frame evals as a **skill**, which means the two options are not opposites: "evals, the AI skill PMs are missing" is a possible bridge |
| 2.3 | B1: a large share of the push comes from eval vendors (Braintrust, Arize). A critic says the money behind it is selling logging | S13, S16, S17, S19 | HIGH | contradicts | Demand may be supply-side. Through *Crossing the Chasm*, vendor launches are not buyer adoption |
**Insight:** through *Obviously Awesome*, A's competitive alternative is a free 7k-star repo, while E's is an engineer-framed plugin and a $4,200 course. E has the unique attribute and A does not · **Belief:** confirms (B3, weak) · **Also changes:** the headline has to name the alternative it beats.

### 3 · The users' words — HN Algolia API, Reddit archive API, Quora
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | B1: a PM on an AI team describes needing quick evals on transcripts and traces, getting blocked by Sheets, and building a tool for it | S4 | HIGH | confirms | Use "quick and dirty" and "transcripts and traces" as copy vocabulary |
| 3.2 | B1: a Meta Llama PM writes "Evals come up a lot these days for PMs." and "Evals are the language of GenAI." | S5 | HIGH | confirms | This PM is a visionary (a lab PM), not a pragmatist |
| 3.3 | B1: on HN, the PM evals guide got 3 pts and 0 comments. A comment search since 2025 found only one PM describing their own eval pain | S6, S7 | HIGH | contradicts | Weak and *adjacent*: HN is an engineers' room, so silence there is not silence from PMs |
| 3.4 | B1: r/ProductManagement could not be read (the archive API refused), and the Quora search returned nothing | S2, S3 | NONE | unknown | The room where PMs actually talk is unread. This is the largest hole in B1 |
**Insight:** through *JTBD*, the job in the one clear PM voice is "check if my AI output is good, fast, without the team". B1 holds on 2 first-person sources, so it is a **weak signal**, not a pattern · **Belief:** confirms (weak) · **Also changes:** the copy should use S4's words, not "eval layer".

### 4 · Offerings and evidence of use — GitHub API (stars and last push), Maven pricing
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | B2: a free repo literally named "Evals for Product Managers" exists, with 4 stars and 1 push since July. No PM-specific eval repo has more than 15 stars | S9, S21 | HIGH | confirms | The PM-framed eval slot is named but not owned by traction |
| 4.2 | B2: the free eval-skills plugin for coding agents (1,675 + 1,475 stars) is maintained by the authors of the leading "Engineers & PMs" course | S10, S11 | HIGH | contradicts | The adjacent slot is owned. E must say how it differs, e.g. "for the PM, not the pipeline" |
| 4.3 | B1: people pay $4,200 for an evals course for engineers and PMs: 4.7 from 1,019 reviews, 50+ enrolled last week | S11 | HIGH | confirms | Paid demand exists. The PM share of it is unknown (*adjacent*: the audience is mixed) |
| 4.4 | B2: a 1,433-star free PM skills repo already sells an eval-style "decision layer: which skill, is it safe, ship or slip" | S12 | HIGH | contradicts | "Skills + eval" is already a combined pitch, so E is less unique than it looks |
**Insight:** through *Kano*, nothing can be said here. Kano needs customer answers and must not be applied to headlines. Through *Cagan's value risk*, people are paying for eval learning, so value risk is retired for the course format, not for a free repo · **Belief:** unknown (B2 split: 4.1 confirms, 4.2 and 4.4 contradict) · **Also changes:** E's headline needs a differentiator against S10.

### 5 · Method — the PM canon (FRAMEWORKS.md)
| # | Framework · what it predicts here | Evidence | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | **JTBD** (*Competing Against Luck*). The job is "know if my AI feature is good enough to ship, and defend it", and the real competitor is Sheets plus gut feel. Agrees | S4, S18 | HIGH | confirms | Headline names the job (ship call), not the artifact (evals) |
| 5.2 | **Obviously Awesome** (Dunford). Start from the competitive alternatives. A's is a free 7k-star repo, so A has no unique attribute. E's are engineer-framed tools and a $4,200 course, so E's attribute is "for the PM who owns the ship call". Agrees | S8, S10, S11 | HIGH | confirms | Pick E's category frame, and name the alternative |
| 5.3 | **Crossing the Chasm** (Moore). Vendor and influencer talk comes from visionaries, while pragmatists buy once peers have results. The backlash shows the first wave already produced "eval theatre". Prediction: "more evals" lands as fatigue, and "make the number mean a decision" lands with pragmatists. Partly disagrees | S17, S19, S20 | HIGH | contradicts | A plain "eval layer" headline is at risk. It has to be reframed as ship/hold |
| 5.4 | **Lean BML + The Mom Test**. The web cannot settle B3. The cheapest test is two headlines on the same page, and the follow-up is past-behaviour interviews ("last time you shipped an AI change, how did you decide?"). Agrees with the gap | S1 | ASK | unknown | Sets the next step |
**Insight:** three frameworks favour the eval *position* (JTBD, Dunford) but warn against the eval *word* (Moore) · **Belief:** confirms (B3, conditional on the reframe) · **Also changes:** the copy.

### 6 · Cases — good, bad, ugly
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | B3: same author, same audience. The skills framing has 7,215 stars and the evals-for-PMs framing has 4 | S8, S9 | HIGH | contradicts | *Adjacent*: stars are not signups, and the repos differ in age (8 vs 3 months) and format (skills vs notebooks). Still the closest natural experiment found |
| 6.2 | B1: "uncommon to find a serious AI product with no eval suite", and teams ran suites for a year with nothing changed. One critic says most teams "don't need evals" | S19, S20 | HIGH | contradicts | The pain has moved from *no evals* to *evals that decide nothing*. E's copy must target the second |
| 6.3 | B1: the translation gap. The PM owns the launch but cannot read the eval numbers | S18, S16 | HIGH | confirms | *Adjacent*: written about PMs, not by them. The sharpest pain statement found, so it can be used as copy |
**Insight:** through *Escaping the Build Trap*, the live pain is output (an eval suite) mistaken for outcome (a ship decision). That is the sentence the eval position can own · **Belief:** contradicts (for the generic eval framing) · **Also changes:** the headline wording.

### 7 · Constraints — cut
Cut at the angle map: no regulation or platform rule bears on landing-page copy.

### 8 · Distribution — where the eval-for-PM message already travels
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Eval-for-PM content spreads through Lenny's Newsletter and List, Aakash's newsletter (an eval episode library) and Maven | S11, S14, S15 | HIGH | unknown | The launch posts go in these rooms |
| 8.2 | HN does not carry PM eval content (3 pts, 2 pts) | S7, S4 | HIGH | unknown | Do not count HN traffic toward the 50 signups |
**Insight:** the rooms that would send PM traffic are newsletter-led, and they already teach evals as a skill · **Belief:** unknown · **Also changes:** where the week-1 traffic comes from.

## 3 · Verdict
**Contradicting rows in section 2 (listed before judging):** 2.3, 3.3, 4.2, 4.4, 5.3, 6.1, 6.2. That is seven rows.

**Belief:** **still unknown.** The web cannot confirm that E converts better (B3). The pieces under it split. **B1 is a weak confirm:** two PMs describe the pain in their own words (3.1, 3.2) and $4,200 of paid demand exists (4.3), but the pain has moved to "eval theatre" (6.2). **B2 is partly contradicted:** the PM-named slot is empty (4.1), but the free eval-skills slot is owned (4.2) and a 1.4k-star PM skills repo already sells eval-scoring (4.4). The three findings that decided it: 2.1 (A collides with a 7k-star incumbent), 6.2 (the pain moved), and 1.1 (no conversion number).
**Falsifier:** **partly fired.** The B1 half did not fire: PMs do describe evals as their own problem (S4, S5), but only on two sources. The B2 half partly fired: no PM-specific free repo owns the angle, but a free eval-skills repo with roughly 3k stars across its two homes owns the neighbouring slot.
**Contradicting evidence:** 2.3 (vendor-driven push) · 3.3 (HN silence, *adjacent*) · 4.2 (Hamel/Shreya own free eval skills) · 4.4 (a skills repo already pitches eval-scoring) · 5.3 (Chasm: eval fatigue among pragmatists) · 6.1 (same author: 7,215 stars vs 4, *adjacent*) · 6.2 (eval theatre backlash).
**Top three, by impact on 50 signups:**
1. **A is the weaker position whatever the test says** (2.1, 5.2). "AI skills for PMs" asks visitors to choose you over a free 7,215-star repo.
2. **Do not sell "evals". Sell the ship call** (6.2, 6.3, 5.3). The pain PMs pay attention to now is "my eval number decides nothing", in S4's words, "quick and dirty" checks on "transcripts and traces".
3. **Name the difference from Hamel/Shreya** (4.2). Their plugin is for coding agents building pipelines. Yours has to be visibly for the PM who makes the launch call.
**Dropped:** none.
**Next step:** **one named gap:** the signups-per-visitor rate of headline E (reframed as the ship call) versus headline A, read from a 50/50 split of this week's page traffic on day 7.
**Other gaps — not needed for this decision:** r/ProductManagement verbatims (archive API refused, S2) · LinkedIn PM posts (login wall, not attempted) · search-interest trend for "AI evals PM" (not checked) · India vs US PM audience split (not checked) · whether the repo's actual contents back an "eval layer" claim (not in scope, not read).

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 19:36 IST. The first search (SOURCES S2–S22, all read 2026-10-09) ran after it |
| 2 Every claim sourced and marked | 21 section-2 rows, each citing an S# with a mark (HIGH 18 · NONE 1 (3.4) · ASK 2 (1.1, 5.4)) |
| 3 No snippet-sourced HIGH | 16 HIGH rows in SOURCES, all with URL and date. verify_quotes.py: 18 quotes OK, 0 MISMATCH, 0 UNREACHABLE. 2 CUT fixed with "…" (S13, S16) (run-02/verify-output.txt) |
| 4 Patterns need three | One pattern claimed: "evals = top PM skill" on 4 sources (S14–S17). B1 user pain is on 2 sources and labelled weak signal |
| 5 Empty angles reported | Angle 7 is reported as cut. Empty searches are S2, S3, S6, S21, S22 (NONE) |
| 6 Every insight states impact | 7 of 7 angle insights carry Belief and Also changes |
| 7 Verdict honest | 7 contradicting rows labelled, 7 cited, dropped: none |
| 8 Ends in a decision step | one named gap: the per-headline signup rate |
| 9 PM canon | Angle 5 is present. JTBD, Obviously Awesome, Crossing the Chasm, Lean/Mom Test, each with a prediction and agree/disagree. Kano explicitly not applied (misuse) |
