# Research map — "AI skills for PMs" vs "the eval layer for PMs who ship AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09T04:18:32Z UTC, before the first search)

| Field | Value |
|---|---|
| **Decision** | **Position** the landing page one of two ways: **A** "AI skills for PMs" (the free Claude Code skills repo is the product; memory + evals are the paid add-on) · **B** "the eval layer for PMs who ship AI features" (evals are the product; the free skills are the on-ramp). Chosen this week. |
| **Goal it serves** | *Not given as a number.* The user said "pick the positioning for the landing page this week." The number the positioning is supposed to move (landing-page sign-ups? free→paid?) was not supplied and is **not substituted from the web** — see angle 1. |
| **Belief** | Two halves, both must hold: **(B1)** PMs who have shipped an AI feature have a measurement problem they can name in their own words; **(B2)** nobody is selling them a fix. |
| **Falsifier** | Fires if **either** (F1) people are already selling evals to PMs, **or** (F2) PMs do not describe measurement as a problem anywhere in their own words. |
| **Already known** | Nothing supplied by the user. The run assumes no prior findings and will not credit any. |

### Angle map and search keys (written before searching)
The user pre-cut the map in the request — *"the users' language, who sells into this, what they charge"* — so angles **3, 2, 4** run in full. The rest are reported, not silently dropped.

| # | Angle | Status | Search keys (problem phrase + platform + company + angle word) |
|---:|---|---|---|
| 1 | Goal | **ask** — no number supplied | — |
| 2 | Lay of the land | run | "LLM evals" vendor pricing · "AI evals for product managers" course · "Claude Code skills for product managers" repo · "PM skills" marketplace |
| 3 | The users' words | run | HN Algolia: "product manager evals", "measure AI feature", "vibe check LLM quality" · Reddit archive API: r/ProductManagement "evals", "AI feature metrics", "how do you measure" · Quora: site:quora.com product manager evals |
| 4 | Offerings + evidence of use | run | Braintrust / LangSmith / Langfuse / Arize Phoenix / promptfoo / DeepEval pricing pages · GitHub stars + last commit · Maven "AI evals" course price |
| 5 | Method / canon | **cut by user** | — |
| 6 | Cases | **cut by user** | — |
| 7 | Constraints | **cut by user** | — |
| 8 | Distribution | light — the rooms angle 3 surfaces, reported for free | same rooms as angle 3 |

---

## 1 · The map

**One screen.** Evals for PMs is already a **paid category** — sold as education at **$420 → $4,200** per seat and as engineer-first tools at **$0 → $249/mo** — and the biggest free Claude Code PM-skills repo already ships an evals skill. PMs do name the problem, in small concrete words, but the forum lane (Reddit) was unreadable, so *unprompted* mass demand is unverified.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| **PM shipping an AI feature** (direct) | *"I didn't need anything fancy, just 'did the agent answer the question', 'did the agent cover the 5 things it needed to'"* (S2) · *"can you prove they are accurate, consistent, and good enough to ship?"* (S16, vendor framing) | *"quick and dirty"* LLM-as-judge on transcripts (S2); *"a few prompts in a spreadsheet"* (S8, vendor claim); existing tools *"too slow and cumbersome"* (S2) | A PM-runnable eval that doesn't *"touch a shit load of infra"* (S2) | Show HN (S2), Sharebird (S1), Maven cohorts (S17: 50+/week) |
| **Senior PM / PM leader** (direct) | *"Accuracy is table stakes...outcomes, predictability, and usability are what turn AI into real product value."* (S1) · *"There's no one size fits all for evals"* (S1) | Outcome / usability / latency criteria they define per problem (S1) | Shared criteria — the question itself is "what do *you* rely on?" (S1) | Sharebird Q&A (S1), Reforge (S19), Product School (S18) |
| **Engineer owning the eval suite** (adjacent) | *"a tweak to a prompt passed an initial vibe check, but performed worse"* (S10) · *"an hour of unscientific manual prompting"* (S9) | promptfoo 25.8k★ (S26), Langfuse 35.5k★ (S27), DeepEval 18.7k★ (S28) — all pushed this week | Repeatability *"agnostic to who's running them"* (S10) | HN threads (S9, S10) |
| **Employers hiring** (adjacent) | *"care deeply about evals and quality"* (S11) | — | PMs/engineers who can do this (S11) | HN Who is hiring (S11) |
| **Sellers** | Education: S16 $420 · S18 $2,999 · S19 $1,995/yr · S17 $4,200 · Tools: S21 $0/$249 · S22 $0/$39 · S23 $0/$29/$199/$2,499 · Free skills: S29 lenny-skills "AI Evaluation Strategy" | — | — | Maven (S20: 6 listings), Reforge, Product School, vendor blogs (S8), Lenny's (S7: 580 shares) |

**Cases to follow:**
1. **Hamel Husain + Shreya Shankar, Maven** (S4, S17) — what they did: a 6-week cohort course titled *for Engineers & PMs*, $4,200. Good: 1,016 reviews at 4.7, 50+ enrolling per week — the price ceiling and the proof PMs pay. Bad: engineer-heavy, 3–5 h/week; the PM is a secondary audience ("Can PMs also get value? Yes!"). Ugly: none found.
2. **Madalina + Catalina Turlea, Maven** (S16) — what they did: a 3-hour, $420, PM-only workshop, "from scratch". Good: 5.0 from 24 reviews; the copy is the sharpest PM-voice framing found (*"polished answers… can you prove they are good enough to ship?"*). Bad: small (24 reviews). Ugly: none found.
3. **RefoundAI/lenny-skills** (S29) — what they did: 76 free, MIT, "ungated" PM skills for Claude Code, including "AI Evaluation Strategy — Move beyond vibe checks to systematic, empirical measurement". Good: 1,381 stars in 8 months. Bad: no push in 12 weeks. Ugly for *you*: it is positioning A, done, free, with the evals skill already inside.
- *Cautionary:* **Beval** (S2) — a PM built the "quick and dirty" eval tool PMs describe wanting; Show HN got 2 points and 1 comment. The need being real does not make the room care.

---

## 2 · Angles

### Angle 1 — Goal · *not searched, by rule*
No number was supplied. The map does not substitute one. **Ask:** which number this week's landing page must move — repo installs / email sign-ups / paid-intent clicks — and the size that would matter. This is the only thing in the map that could flip the verdict's next step (see §3).

### Angle 2 — Lay of the land · *who is in this space* — searched Maven, Reforge, Product School, vendor pricing pages, GitHub; opened each
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 2.1 | Maven has a **category page literally named "for product managers / AI evals"** with 6 listings | S20 | HIGH | **contradicts B2** |
| 2.2 | Four independent sellers run PM-targeted eval education at $420 (S16), $1,995/yr (S19), $2,999 (S18), $4,200 (S17); audience lines name PMs explicitly in all four | S16–S19 | HIGH | **contradicts B2** — pattern on 4 independent sources |
| 2.3 | Tool vendors are engineer-first: LangSmith and Langfuse pricing pages never mention PMs (S22, S23); Braintrust is the exception with a "For PMs" resource and a PM-targeted blog (S8, S21) | S21–S23 | HIGH | **contradicts B2** (one tool vendor already sells to PMs); **confirms** that most tools don't — a gap in *tools*, not in *fixes* |
| 2.4 | Free "skills for PMs" repos exist: lenny-skills 1,381★ (S29), aakashg 160★ (S30); further marketplaces seen in snippets only (S31) | S29–S31 | HIGH ×2, ZERO ×1 | **unknown vs belief; bears on decision A** — labelled *weak signal* (2 opened) |
| 2.5 | lenny-skills includes an **"AI Evaluation Strategy"** skill, free and ungated | S29 | HIGH | **contradicts B2** — a free fix already exists in the exact distribution channel (Claude Code skills) |
**Insight:** Evals-for-PMs is a priced, reviewed category — $420 to $4,200 for education, $0–$249/mo for tools — and the free version already lives in the top PM-skills repo. · **Impact:** B2 is false; positioning B enters a market, not a blue ocean. Positioning A enters a free commodity.

### Angle 3 — The users' words · *verbatim only* — searched HN Algolia (5 queries), Sharebird, Substack posts by PMs, Show HN; Reddit blocked, Quora empty, X not searched
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 3.1 | A PM shipping AI products names the need in concrete terms: *"did the agent answer the question", "did the agent cover the 5 things it needed to"* — and says existing tools are *"too slow and cumbersome"* | S2 | HIGH (direct) | **confirms B1** |
| 3.2 | A PM community asks, unprompted: *"What evaluation criteria (beyond accuracy) do you consistently rely on for AI features?"*; two senior PMs answer with outcome/usability/latency, and *"no one size fits all"* | S1 | HIGH (direct) | **confirms B1** — the problem is named; the answer is "define it yourself" |
| 3.3 | A PM writes about evals as a product discipline, but the quoted pain is integration hesitation, not AI measurement | S3 | HIGH (direct, tangential) | **unknown** — not counted toward B1 |
| 3.4 | Creators and vendors describe the PM problem in near-identical words: *"intuition and demos alone"* (S5), *"can't just 'test' an AI feature"* (S6), *"a few prompts in a spreadsheet"* (S8), *"ship prompt changes and hope nothing breaks"* (S4), *"beyond vibe checks"* (S7, 580 shares) | S4–S8 | HIGH (creator/vendor) | **confirms B1 weakly** — these are people *selling* the framing, so they also **confirm F1** |
| 3.5 | Engineers describe the same failure — *"passed an initial vibe check, but performed worse"* (S10), *"an hour of unscientific manual prompting"* (S9) | S9, S10 | HIGH (adjacent) | **adjacent** — not merged with PM evidence |
| 3.6 | On HN, PM + evals surfaces almost only as **job ads** (*"care deeply about evals and quality"*, S11); direct "how do you measure" queries return **0** (S12) | S11, S12 | HIGH (searched) | **weak contradiction of B1** — the pain is not voiced on HN in PM words |
| 3.7 | **Reddit r/ProductManagement not read** — arctic-shift 422 ×3, pullpush 429 ×2, search engine refuses reddit.com. **Quora: zero results** for the site: query. **X: not searched.** | S13–S15 | ZERO / searched-empty / not searched | **unknown** — the lane where unprompted PM language would live is unverified |
**Insight:** PMs do name the problem — but in only **2 direct rows** (S1, S2); the rest of the "PM voice" is creators and vendors repeating one framing ("beyond vibe checks"). · **Impact:** B1 is a **weak signal**, not a confirmed pattern (threshold is 3 direct sources); F2 did not fire, but the forum lane that would have settled it was blocked.

### Angle 4 — Offerings, and evidence of use · *what exists and is it used* — opened pricing pages and GitHub API for each
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 4.1 | Education price ladder for PMs: **$420** (3 h workshop, 5.0/24) → **$1,995/yr** (Reforge membership) → **$2,999** (Product School cert) → **$4,200** (Hamel/Shreya, 1,016 reviews, 50+/week) | S16–S19 | HIGH | **contradicts B2**; sets the price anchors a paid layer competes against |
| 4.2 | Tool price ladder: Braintrust $0 / $249/mo; LangSmith $0 / $39/seat; Langfuse $0 / $29 / $199 / $2,499/mo; Arize not readable (403); PostHog "free" pitch, pricing not read | S21–S25 | HIGH (3), ZERO (2) | **contradicts B2**; the $0 tiers are the real competitor for a solo PM |
| 4.3 | OSS evals are alive, not museums: promptfoo 25.8k★ pushed 2026-10-09; Langfuse 35.5k★ pushed 2026-10-09; DeepEval 18.7k★ pushed 2026-10-07 | S26–S28 | HIGH | **contradicts B2** — but all three are "developer-first" (S26) / for "teams" (S27); none opened positions for PMs |
| 4.4 | The one PM-built, PM-shaped eval tool found (Beval) got 2 points on HN | S2 | HIGH | **unknown** — need is real, pull is unproven |
| 4.5 | lenny-skills: 1,381★, 177 forks, MIT, free, evals skill included, **12 weeks since last push**; aakashg: 160★, **7 months since last push** | S29, S30 | HIGH | **bears on A** — free PM-skills repos are starred, then go quiet |
**Insight:** What is sold to PMs is *education* (expensive) and *engineer tools* (free at the bottom); nothing opened is an eval a PM runs inside their own workflow — but that absence is only in this sample, not a searched claim. · **Impact:** contradicts B2 as stated; leaves the *shape* of a PM-workflow eval product **unknown**.

### Angle 5 — Method / canon · *cut by user* — not searched.
### Angle 6 — Cases · *cut by user* — not searched; the three cases in §1 come from angles 2–4, not from a case search.
### Angle 7 — Constraints · *cut by user* — not searched.

### Angle 8 — Distribution · *reported from angle 3's rooms, no extra search*
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 8.1 | Where PMs who care about evals demonstrably gather, with money or attention: Maven cohorts (50+/week, S17), Lenny's (580 shares on the evals guide, S7), Aakash Gupta's newsletter (50 likes, S6), Sharebird (800 views on one answer, S1), lenny-skills stargazers (1,381, S29) | S1, S6, S7, S17, S29 | HIGH | **unknown vs belief** — reach map only |
| 8.2 | HN is not the room: a PM-built eval tool got 2 points (S2); PM+evals surfaces as job ads (S11) | S2, S11 | HIGH | **unknown** |
**Insight:** The audience for B is reachable through three creators' newsletters and one repo's stargazers; HN is not it. · **Impact:** none on the belief; sets where the landing page gets its first traffic.

---

## 3 · Verdict

**Belief: contradicted** — because B2 ("nobody is selling them a fix") is false on six independent opened sources, and B1 ("PMs can name the problem") holds only as a weak signal. The three findings that decided it:
1. **Four sellers already sell evals to PMs by name**, at $420 / $1,995-yr / $2,999 / $4,200, with 1,016 reviews behind the most expensive (S16–S19); Maven has a category page for it (S20).
2. **The free fix already exists in your channel**: lenny-skills (1,381★, MIT, "ungated") ships "AI Evaluation Strategy — Move beyond vibe checks…" as a Claude Code skill (S29). Braintrust, a tool vendor, publishes "Evals for PMs" and a "For PMs" page (S8, S21).
3. **PMs name the problem in their own words — twice** (S1, S2); the rest of the chorus is creators and vendors (S4–S8). The forum lane that would show unprompted demand (Reddit) was unreadable (S13).

**Falsifier: fired** — F1 (people selling evals to PMs) fired. F2 (PMs don't describe it) did not fire, on a weak signal.

**Contradicting evidence** (against the belief as written): S4, S16, S17, S18, S19, S20 (PM-named eval courses and a marketplace category) · S21, S8 (tool vendor selling to PMs) · S29 (free evals skill in the top PM-skills repo) · S26–S28 (active OSS eval tooling). Against B1: S12 (HN "how do you measure" → 0), S11 (HN surfaces PM+evals only as job ads).

**Top three, by impact on the goal** (positioning the landing page this week):
1. **Positioning B is a real, priced category, not a blue ocean** — so the page can borrow the category's words and price anchors ($420 workshop, $4,200 course, $249/mo tool) but **cannot claim "nobody sells you a fix."** The honest claim is narrower: the fix is sold as a course you take or an engineer's tool you install.
2. **Positioning A is a free commodity with your paid feature already inside it** — lenny-skills gives away 76 skills including evals; "AI skills for PMs" makes you the third free repo, and hides the paid layer behind the free one.
3. **Use the PM's words, not the category's** — *"did the agent answer the question", "did it cover the 5 things it needed to", "quick and dirty", "can you prove it's good enough to ship?"* (S2, S16). "The eval layer" is vendor language; nobody opened said it.

**Next step: decide — B, reframed.** Position as the eval a PM runs inside the workflow they already use (Claude Code), against the $4,200 course and the engineer's tool — and drop the "nobody is selling a fix" premise from the copy. The one thing that would reverse this is angle 1: if the number this week is raw repo installs rather than paid intent, A's broader audience wins on reach. The map cannot weigh that because no number was given; the unverified Reddit lane affects the *copy*, not the A-vs-B choice, since both options carry it equally.

---

## 4 · Self-check (not a scoreboard)

| # | Check | Actual value |
|---:|---|---|
| 1 | Ground truth before search | §0 written **2026-10-09T04:18:32Z**; first fetch issued in the following turn; earliest SOURCES row read 2026-10-09 after that stamp |
| 2 | Every claim sourced and marked | 22 findings in §2; each cites an S# carrying HIGH / MEDIUM / ZERO or an explicit searched-empty / not-searched label |
| 3 | No snippet-sourced HIGH | All HIGH rows have a URL and date read 2026-10-09; snippet-only rows (S31, S32) are ZERO; S32's price conflicts with the opened page and was not used |
| 4 | Patterns need three | "People sell evals to PMs" — 6 independent HIGH (S16–S21, S29) · "PMs name the problem" — **2 direct** (S1, S2) → **labelled weak signal** · "free PM-skills repos are common" — 2 opened (S29, S30) + snippets → **labelled weak signal** |
| 5 | Empty angles reported | Angle 1: ask · 5, 6, 7: cut by user · Reddit: blocked (S13) · Quora: searched-empty (S14) · X: not searched (S15) · HN direct-pain queries: 0 (S12) |
| 6 | Every insight states its impact | 5 angle insights + 22 findings, each with confirms / contradicts / unknown against B1 or B2 |
| 7 | The verdict is honest | §3 lists all 11 contradicting rows, including the two that cut against B1 |
| 8 | Ends in a step a decision can take | **decide** — with the one named condition (angle 1's number) stated, not "more research" |
