# Research map — "AI skills for PMs" vs "the eval layer for PMs who ship AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09 12:40 IST, before the first search)
**Decision:** *position* — the landing page for a free repo of Claude Code skills for PMs, with a paid memory + evals layer, leads with either (A) "AI skills for PMs" or (B) "the eval layer for PMs who ship AI features". Chosen this week.
**Goal it serves:** the landing page's conversion number — *unconfirmed*: the user named "pick the positioning this week" but not the number (free-repo installs? paid-layer signups? the threshold that matters?). Asked for in S1; never substituted with the web's numbers.
**Belief:** PMs who have shipped an AI feature have a measurement problem they can name, and nobody is selling them a fix.
**Falsifier:** (a) people are already selling evals to PMs, **or** (b) PMs do not describe measurement as a problem anywhere in their own words. Either half firing drops the belief.
**Already known:** *unconfirmed* (not supplied) — drafted as: the user knows Claude Code skills/plugins exist and that eval tooling for engineers exists; what is not known is whether any of it is sold *to PMs* and whether PMs themselves say "measurement" is the pain.

### Angle map and search keys (user asked for: users' language · who sells into this · what they charge)
| # | Angle | Kept? | Keys written before searching |
|---:|---|---|---|
| 1 | Goal | kept as ASK | which number on the landing page, and the threshold |
| 2 | Lay of the land | **kept** | "evals for product managers" course · "AI evals" PM Maven · "AI PM" course evals · "LLM evaluation" "product manager" pricing |
| 3 | Users' words | **kept** | HN Algolia: "evals product manager" · Reddit archive r/ProductManagement: "evals", "measure AI feature" · Quora: "how do product managers measure AI feature success" |
| 4 | Offerings + evidence of use | **kept** | GitHub "claude code skills product manager" · promptfoo / langfuse repo pages · Maven enrolment counts · Braintrust / LangSmith pricing pages |
| 5 | Method — canon | kept, light | Hamel Husain "Your AI product needs evals" · Lenny "PM's guide to evals" · Continuous Discovery Habits (outcome metrics) |
| 6 | Cases | kept, light | companies that positioned "evals for PMs" · "AI evals" product launches aimed at PMs · shut-downs (Humanloop) |
| 7 | Constraints | **cut** (*unconfirmed*) — a positioning call carries no regulatory or platform limit; Anthropic marketplace terms would bind both options equally | — |
| 8 | Distribution | kept, light | the rooms from angle 3 · Lenny's · Maven · LinkedIn |

*(sections 1–4 written after the search; first source read 2026-10-09 ~12:42 IST)*

---

## 1 · The map
**In one screen:** the second half of the belief is dead — at least seven named sellers already sell evals *to PMs by name* (courses $420–$4,200, certifications, tools $200–$249/mo, an analytics vendor). The first half ("a problem they can name") is alive but thin: the only PM-voiced words that could be opened are a 192-comment HN thread, three PM-educators and one sceptic; the Reddit lane could not be opened. The white space that does exist is **format**, not category: none of the three largest free PM skill repos for Claude Code (26.8k★, 7.2k★, Anthropic's official plugin) ships an eval skill.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| PM who has shipped an AI feature (the target) | "you'll bump into this invisible wall: 'How do we know if it's working?'" (S19) · "'intuition as evals.' That's actually the crux. PMs have context about what the product should…" (S16) · "Your AI feature returns polished answers. But can you prove they are accurate, consistent, and good enough to ship?" (S3, seller's copy) | demos and spot-checks (S2 "spot-checking AI outputs by hand"); a vendor dashboard that "lives behind an engineering queue" (S11) | a way to run the eval where the PM already works, without an engineer — and to *interpret* it (S20) | HN PM threads (S41) · Lenny's, paywalled (S7, S25) · Product Compass (S40) · Maven cohorts (S2–S5) |
| PM buying "evals" training | "Evals feel like an engineer's job, the information is scattered, the courses long and expensive." (S5) | Hamel/Shreya $4,200 (S2) · Turlea $420 (S3) · AI Product Academy cert (S4) · Boiteux $499 (S5) · Product School cert (S8) | a cheaper, in-workflow option — S5 is explicitly positioned against "long and expensive" courses | Maven · Product School · Lenny's |
| PM buying an eval *tool* | "every prompt tweak and quality check waits on someone else" (S11) | Confident AI $200/mo (S12) · Braintrust $249/mo (S10) · Arize $50/mo, LangSmith $39/user (S11) · Amplitude Agent Analytics (S13) | the tools assume an engineering setup first (S11: "engineering completes initial setup once") | vendor blogs · HN |
| Engineers (adjacent) | job ad: "through the evals that prove they accomplish the user's goal" (S24) | Promptfoo, Langfuse (S11) | — | HN hiring threads |
| PM using Claude Code skills (option A's buyer) | "Most Product Managers use AI like a chatbot: you ask a question, you copy the answer." (S14) | pm-skills 26,845★ MIT (S26) · Product-Manager-Skills 7,209★ (S28) · Anthropic official plugin (S29) · a $499 course with 3 reviews (S14) | **no eval skill in any of the three** (S27, S28, S29) | GitHub · Product Compass · Maven |

**Cases to follow:**
- **Hamel & Shreya (good)** — sold "AI Evals For Engineers & PMs" at $4,200 with 1,016 reviews and "50+ people enrolled last week" (S2), "5,000+ engineers & PMs" claimed (S30). The category is paid for, at scale. Source S2, S30.
- **Humanloop (ugly)** — an eval/observability platform, acquihired by Anthropic, "shut down its AI platform on September 8, 2025" (S36). The tool layer consolidates toward the model vendors; a tool-shaped eval play competes with Anthropic itself. Source S36.
- **"Eval Theatre" (bad)** — "an eval suite nobody can interpret, that has never caught anything, and that no decision has ever hung on" (S20). The gap after the suite exists is ownership and interpretation, and "the person with that expertise is the PM". Source S20.

---

## 2 · Angles

### Angle 1 — Goal · the number is the user's, not the web's
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Asked for: the landing-page metric this positioning must move and the threshold | S1 | ASK | unknown | nothing until supplied; the A/B choice below does not reverse on it |
**Insight:** the decision is a positioning call, and neither option is sensitive to which conversion number is chosen · **Belief:** unknown · **Also changes:** nothing.

### Angle 2 — Lay of the land · who sells into this, and what they charge · searched Maven, course roundups, vendor blogs and pricing pages
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | "AI Evals For Engineers & PMs" — $4,200, 4.7★ / 1,016 reviews, cohort Oct 10, "50+ people enrolled last week"; copy names PMs and "spot-checking AI outputs by hand" | S2 | HIGH | **contradicts** ("nobody is selling") | the decision: B enters an occupied, priced category |
| 2.2 | "Build AI Evals from Scratch for Product Managers" — $420, 5.0★ / 24 reviews, PM-only | S3 | HIGH | **contradicts** | B's price anchor: a PM-only eval course sells at $420 |
| 2.3 | "AI Evals for PMs Certification" — Marily Nika, 4.4★ / 21 reviews, PM-only | S4 | HIGH | **contradicts** | — |
| 2.4 | "Build Your First AI Eval" — $499, PM-first, positioned against "courses long and expensive" | S5 | HIGH | **contradicts** | the build: a sub-$500 "first eval" is already a product; the paid layer must be cheaper or in-workflow |
| 2.5 | Aman Khan: free 45-min lesson "Mastering Evals as an AI Product Manager" (Apr 2025) + Lenny's paid guide, 580 likes · 48 restacks | S6, S7 | HIGH | **contradicts** | distribution: the educating has been done; the page can assume the word "evals" |
| 2.6 | Product School sells an "AI Evals Certification" (no price shown) | S8 | HIGH | **contradicts** | — |
| 2.7 | Tool vendors address PMs by name: Braintrust "Evals for PMs" (Mar 2026), $249/mo Pro; Confident AI "for Product Managers", $200/mo Starter; Amplitude "Agent Analytics" for product teams | S9, S10, S11, S12, S13 | HIGH | **contradicts** | B must say what it is *not*: not a $200–$249/mo dashboard behind an engineering queue |
| 2.8 | Option A's paid comparables: "Claude Code for Product Managers" $499 — 3 reviews | S14 | HIGH | unknown (not about the belief) | A has one paid comparable with almost no evidence of use |
| 2.9 | Roundup prices for S2 ($5,000 → $3,750, 768 reviews) lag the live page ($4,200, 1,016) | S15 | MEDIUM | unknown | trust: quote live pages, not roundups, on the landing page |
**Insight:** "evals for PMs" is a named, priced category with ≥7 independent sellers (S2–S9, S11–S13) — a pattern, not a weak signal · **Belief:** contradicts · **Also changes:** the decision — B cannot claim an empty market; its claim has to be a cheaper, in-workflow format.

### Angle 3 — The users' words · unprompted PM language · searched HN Algolia (3 queries), Reddit archive (blocked), Quora (empty), PM-authored posts
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | HN, 192-comment PM thread: "'intuition as evals.' That's actually the crux. PMs have context about what the product should…" | S16, S17 | HIGH | weak confirm (2 voices, one thread) | the page's language: PMs frame it as *their* judgement needing to scale, not as "measurement" |
| 3.2 | Same thread: "Nor do I know what an 'eval' is, or which of the no less than three different deacronymings of 'PM'…" | S18 | HIGH | counter-signal | the word "eval" is not universal on a general tech forum; it is on PM/Maven surfaces (S2–S8) |
| 3.3 | PM-educator, first person: "I see PMs trying to ship GenAI features based on intuition and demos alone." · "'How do we know if it's working?'" | S19 | HIGH — adjacent | weak confirm (an educator, not a complaint) | the page's headline question candidate: "How do we know if it's working?" |
| 3.4 | Sceptic: suites exist "that no decision has ever hung on"; "the person with that expertise is the PM" | S20 | HIGH | counter-signal to "nobody sells" (the problem has moved past having a suite) · confirms the PM owns the domain knowledge | the build: the paid layer's value is interpretation + ownership, not another score |
| 3.5 | Employer's words: a Senior PM, AI Agents role owns "the evals that prove they accomplish the user's goal" | S24 | HIGH — adjacent | adjacent, confirms (demand for the skill, not a complaint) | distribution: hiring threads name the skill |
| 3.6 | Reddit r/ProductManagement — could not be opened (archive 429 ×3, DNS, direct fetch blocked) | S21 | ZERO | unknown | one named gap candidate (see verdict) |
| 3.7 | Quora — nothing found; HN first-person PM queries — nothing found beyond 3.1 | S22, S23 | NONE | unknown | — |
| 3.8 | Lenny's 26 PM comments on the evals guide exist but are paywalled | S25 | ZERO | unknown | — |
**Insight:** PMs who speak about this say "intuition" and "how do we know if it's working", not "measurement" — but only 3 PM-voiced rows could be opened, so "PMs name the problem" is a **weak signal**, not a pattern · **Belief:** weak confirm (first half) · **Also changes:** the landing-page copy — use their phrasing, not "measurement problem".

### Angle 4 — Offerings, and evidence of use · what exists free/paid and whether it is used · opened GitHub API + READMEs, course pages
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | pm-skills: 26,845★, 2,844 forks, MIT, pushed 2026-09-14 — alive and free | S26 | HIGH | unknown (option A's market, not the belief) | A is commoditised at $0 by a 26.8k★ repo |
| 4.2 | pm-skills has `metrics-dashboard`, `ab-test-analysis`, `/ship-check` — **no eval skill** | S27 | HIGH | **confirms** (nobody sells the fix *in this format*) | the build: the first paid-layer skill should be the one the 26.8k★ repo lacks |
| 4.3 | Product-Manager-Skills: 7,209★, pushed 2026-09-01, CC BY-NC-SA — no eval/metrics skill | S28 | HIGH | **confirms** (format gap) | same |
| 4.4 | Anthropic's official product-management plugin: `/metrics-review` but no eval command | S29 | MEDIUM | confirms (format gap), unverified at the repo | trust: open the plugin README before claiming this on the page |
| 4.5 | Evidence the eval category is used: "5,000+ engineers & PMs" (seller's claim), 1,016 reviews; PM-only courses 24 + 21 reviews | S30, S2, S3, S4 | HIGH | contradicts ("nobody sells") · PM-specific volume is small (45 reviews across two PM-only courses) | the decision: PM-only demand is real but counted in dozens, not thousands |
**Insight:** the category is sold and used; the *format* — an eval skill inside the PM's Claude Code workflow — is empty in all three large free repos · **Belief:** contradicts as written, confirms if rewritten to "nobody sells it as a skill" · **Also changes:** the build and the positioning sub-line.

### Angle 5 — Method, what the canon says · opened the two primary posts; book not opened
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | Hamel (2024): "unsuccessful products almost always share a common root cause: a failure to create robust evaluation systems" · "beyond vibe checks" | S32 | HIGH | confirms (the problem is real and named by the canon) | the method: error analysis first, then evals |
| 5.2 | Lenny's/Hamel+Shreya podcast: "eval prompts effectively become living product requirements documents" | S33 | HIGH | confirms | the build: an eval skill is a PRD skill with a test attached — which is what PM skill repos already do for PRDs |
| 5.3 | Kevin Weil (via Mind the Product): "Writing evals is going to become a core skill for product managers." | S34 | MEDIUM | confirms (authority, second-hand) | distribution: quotable on the page, with the source |
| 5.4 | Continuous Discovery Habits — not opened this run | S35 | ZERO | unknown | — |
**Insight:** the canon has already named evals as a PM skill, so B does not need to educate the market — it needs to be distinct from the people who did · **Belief:** confirms the first half · **Also changes:** copy — the page can assume the word.

### Angle 6 — Cases · good, bad, ugly · opened the Humanloop sunset notice, three practitioner posts
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Humanloop (evals + observability platform) acquihired by Anthropic; platform shut down 2025-09-08 | S36 | HIGH | unknown (not about the belief) | the decision: a *tool*-shaped eval product competes with the model vendors; a *skill*-shaped one rides on them |
| 6.2 | "Eval theatre": green dashboards no decision hangs on | S20 | HIGH | counter-signal | the build: ship interpretation, not scores |
| 6.3 | PM newsletters explain evals from scratch in 2026 (Aakash, 50 likes; HackerNoon, no data) | S37, S38 | HIGH | confirms (still being explained = still a felt gap) | — |
| 6.4 | Product School's "$33.9 billion… 1 in 100 companies" — unsourced on page | S39 | ZERO | unknown | never reuse these numbers |
**Insight:** the one failure found is a tool, the successes are teaching — B as a skill (teaching-shaped, inside the workflow) sits on the winning side of that line · **Belief:** unknown · **Also changes:** the build's shape.

### Angle 7 — Constraints · cut (see section 0; *unconfirmed*)
nothing searched — the angle was cut before searching, on 2026-10-09, because a positioning choice carries no regulatory or platform limit that bears on A vs B.

### Angle 8 — Distribution · where these PMs are · from the rooms that surfaced in angles 2–3
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | A PM-topic HN thread drew 206 pts · 192 comments (Mar 2026) and the eval exchange happened inside it | S41 | HIGH | unknown | the launch post lives on HN as a PM take, not a tool launch |
| 8.2 | Product Compass: "#1 AI and PM newsletter"; its author owns the 26.8k★ repo (S26) — the room and the incumbent are the same person | S40 | MEDIUM | unknown | distribution via the incumbent's room, or against it, is a choice to make |
| 8.3 | dev.to / Substack PM-eval explainers exist, low engagement (13 shares; counts not shown) | S19, S42 | HIGH | unknown | — |
**Insight:** the rooms are HN (PM takes), Lenny's (paywalled), Product Compass (incumbent-owned), Maven · **Belief:** unknown · **Also changes:** the next step after positioning — where the first post goes.

---

## 3 · Verdict
**List first (every row labelled contradicts / weak confirm / counter-signal / adjacent / trust in section 2):** S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S30 (contradicts) · S16, S17, S19 (weak confirm) · S18, S20 (counter-signal) · S24 (adjacent, confirms) · S15, S29 (trust).

**Belief:** **contradicted** — because (1) "nobody is selling them a fix" fails on seven independent, opened sellers that name PMs: $4,200 / 1,016 reviews (S2), $420 PM-only (S3), a PM-only certification (S4), $499 (S5), Product School (S8), Braintrust and Confident AI at $249 / $200 a month (S9–S12); (2) "a measurement problem they can name" survives only as a weak signal — three PM-voiced rows (S16, S17, S19), phrased as "intuition" and "how do we know if it's working", with the Reddit lane unopened (S21); (3) the format gap is real: no eval skill in the 26.8k★, 7.2k★ or official repos (S27, S28, S29).
**Falsifier:** **fired** — half (a). Half (b) did not fire, and was only partly testable (S21 ZERO, S22–S23 NONE).
**Contradicting evidence:** S2, S3, S4, S5, S6, S7, S8, S9, S10, S11, S12, S13, S30 — sellers of evals to PMs, by name and price. Counter-signals S18 (the word "eval" is not universal outside PM rooms) and S20 (suites exist that no decision hangs on — the unsolved part is interpretation). Weak confirms S16, S17, S19 are cited above and are not enough for a pattern. Adjacent S24 is a hiring signal, not a user's complaint. Trust rows S15 (roundup prices stale vs live page) and S29 (plugin not opened) are flagged; none dropped.
**Top three, by impact on the goal (the landing page):**
1. B's category is occupied and priced — courses $420–$4,200, tools $200–$249/mo (S2–S5, S10, S12). The page cannot say "nobody does this"; it can say "not a course, not a dashboard".
2. The empty slot is format: none of the three big free PM skill repos ships an eval skill (S27, S28, S29). "The eval layer" is defensible only as *a skill that runs where the PM already works*.
3. A is free at 26.8k★ MIT (S26) and its only paid comparable has 3 reviews (S14). "AI skills for PMs" has no price anchor above zero and no differentiation.
**Next step:** **decide** — B, rewritten: lead with "the eval layer for PMs who ship AI features", sub-line the format ("skills that run in Claude Code, where you already work — not a $4,200 course, not a dashboard behind an engineering ticket"), use the users' phrasing ("how do we know if it's working?", S19) and drop every claim of an empty market. The ASK (S1) and the Reddit gap (S21) do not reverse A vs B: A has nothing to reverse to.

---

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | section 0 written 12:40 IST; first page opened ~12:42 IST; nothing in sections 1–4 predates it |
| 2 Every claim sourced and marked | 42 SOURCES rows; every finding row in section 2 cites an S# and the row carries a mark |
| 3 No snippet-sourced HIGH | 30 HIGH rows, each with a URL and date read; two roundup-only rows (S29, S31) and the roundup price (S15) held at MEDIUM |
| 4 Patterns need three | "sellers of evals to PMs" = 7 opened sellers (S2–S5, S8, S9, S11); "PMs name the problem" = 3 rows, labelled **weak signal** |
| 5 Empty angles reported | angle 7 cut with reason; angle 3 carries ZERO (S21, S25) and NONE (S22, S23) rows with search strings; angle 1 is ASK |
| 6 Every insight states its impact | 8 angle insights, each with Belief + Also changes; 1 row marked unknown with "nothing" (1.1) |
| 7 The verdict is honest | 21 labelled rows listed before the verdict; all 21 cited in *Contradicting evidence*; none dropped |
| 8 Ends in a step | decide (B, rewritten); the two open items (S1, S21) are stated as not reversing the choice |
