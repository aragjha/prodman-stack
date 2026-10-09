# Research map — "AI skills for PMs" vs "the eval layer for PMs who ship AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09 19:35 IST, before the first search)
**Decision:** Position the landing page as (P1) "AI skills for PMs" or (P2) "the eval layer for PMs who ship AI features". Choose P2 only if both B1 and B2 hold.
**Goal it serves:** Pick the landing-page positioning this week. The number it should move (landing-page visitor → free-repo signup, and free → paid conversion on the memory+evals layer) was **not given** — *unconfirmed*, recorded as ASK.
**Belief (third person, split):**
- **B1:** The PM believes PMs who have shipped an AI feature have a measurement (evals) problem they can name in their own words.
- **B2:** The PM believes nobody is currently selling an evals fix to PMs.
**Falsifier (user's own, confirmed):** (F2) finding people already selling evals to PMs → drops B2; (F1) PMs not describing measurement as a problem anywhere in their own words → drops B1.
**Already known:** The product exists in outline: a free repo of Claude Code skills for PMs + paid layer (memory, evals). Nothing else stated as already seen — *unconfirmed*.

**Angle map and search keys (contradicting keys run first):**
| # | Angle | Kept? | Search keys (problem phrase + platform + company + angle word) |
|---:|---|---|---|
| 1 | Goal | kept (ASK) | conversion baseline — ask the user |
| 2 | Lay of the land | kept | "AI evals course for product managers"; "eval tool for PMs" Braintrust / Arize / LangSmith / Humanloop; "Claude Code skills for product managers" |
| 3 | Users' words | kept | HN Algolia "product manager evals"; Reddit r/ProductManagement "evals" "AI feature" "how do you measure"; "evals are hard" PM |
| 4 | Offerings + use | kept | Maven "AI evals" course price; GitHub "pm skills claude code" stars + last commit; Lenny's "evals" |
| 5 | Method (canon) | never cut | Dunford, JTBD, Crossing the Chasm, Kano (not from competitor counts) |
| 6 | Cases | kept, light | "evals for PMs" course enrolment numbers; "Humanloop shut down / acquired" |
| 7 | Constraints | cut — positioning copy has no regulatory constraint | — |
| 8 | Distribution | kept, light | Lenny's newsletter / Maven / LinkedIn creators teaching evals to PMs |

Contradicting keys (run first): "evals course for product managers" (tests F2), "eval platform for product managers" (F2), "PMs don't need evals" / "evals overrated" (F1).

---

## 1 · The map
"Eval layer for PMs" is not an empty shelf. It is a standing Maven category (S27) with at least six paid PM-facing eval courses priced $399–$4,200 (S2, S4, S5, S6, S7, S8), and at least two eval platforms with a PM landing page and self-serve tiers at $200–$249/month (S9, S10, S11). "AI skills for PMs" is crowded too, but free: pm-skills has 26,856 stars and was pushed today (S18), Product-Manager-Skills has 7,215 (S19). The two positions overlap in one repo: Hamel Husain's free evals-skills (1,675 stars), the companion to the $4,200 course (S20). Unprompted PM pain in PMs' own words is thin: one HN comment (S13). Reddit could not be read (S23).

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| PM on a team shipping AI, no eng help for exploring | "In my day to day as a Product Manager working in a team that ships AI products, I often found myself wanting to do …" (S13) | Gemini in Google Sheets, then hand-written Python calls to the OpenAI API (S13) | A product for quick evals a PM runs alone (S13). One voice only, so a weak signal | HN Show/Ask threads (S13) |
| PMs paying to learn evals | "This course is popular 50+ people enrolled last week." (S2) · "… Homework 1 study group for nontechnical students …" (S3) | Cohort courses $399–$4,200 (S2, S4–S7) | Courses claim the gap is "deep dives : four weeks … a price above $4,000" (S5). The cheap, fast end is already being sold at $399–$499 | Maven (S27), Reforge (S8), Product School (S6), Lenny's (S15) |
| PMs at teams buying tooling | "For Product Managers Track AI quality without writing code." (S9, vendor's words, not users') | Braintrust, Confident AI, LangSmith (S9–S11) | nothing found from users; the vendors set this framing | vendor content, vendor comparison pages (S9, S12) |
| Skeptics | "Most AI teams don't need evals. They need logging, QA, and taste." (S16) | logging, QA (S16) | n/a. The thesis is that the category itself is oversold | Substack/X (S16) |

**Cases to follow:**
- **Hamel Husain & Shreya Shankar, *AI Evals For Engineers & PMs*.** What they did: an expensive course first, then free skills that point back to it (S2, S20). Good: 4,500+ students claimed, 1,019 ratings at $4,200. Bad: built for engineers and PMs together, so nontechnical students need a separate study group (S3). Ugly: it already holds the "evals as skills" spot for free (S20).
- **Jules Boiteux, *Build Your First AI Eval*.** What he did: positioned against the $4,000 deep dive as $499, three sessions, Claude Code-based (S5). Good: this is the exact wedge an "eval layer for PMs" would take. Bad: it is already taken. Ugly: nothing found.
- **Humanloop.** What it did: an eval platform pitched at PMs and domain experts. Good: acquired by Anthropic. Ugly: the standalone product was shut down in Sep 2025 (S22, MEDIUM). A PM-friendly eval tool alone did not stay a standalone business.

## 2 · Angles

### 1 · Goal — approach: ask; never substitute the web's numbers
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Current visitor → signup and free → paid baselines were not supplied; the landing page's target number is unknown | S1 | ASK | unknown | Through North Star, the input metric this positioning should move (signup rate for the free repo) needs a baseline before the choice can be judged |
**Insight:** North Star: with no baseline, either headline "wins" by assertion. · **Belief:** unknown · **Also changes:** next step.

### 2 · Lay of the land — approach: course marketplaces, vendor PM pages, PM-skills repos · searched "AI evals course for product managers", "eval platform for product managers", "Claude Code skills for product managers github"
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | Maven runs "AI Evals" as a standing category under Product | S27 | HIGH | contradicts (B2) | Positioning: P2 lands in a named, crowded category |
| 2.2 | Reforge sells a live AI-evals course explicitly "for product managers" | S8 | HIGH | contradicts (B2) | — |
| 2.3 | Confident AI has a "For Product Managers" solution page: "Track AI quality without writing code." | S9 | HIGH | contradicts (B2) | Tools already sell evals to PMs, not only courses |
| 2.4 | Free "AI skills for PMs" category: Anthropic plugin, Huryn, Peters, Vellotti named as starting points (search summary, not opened) | S26 | ZERO | unknown | P1 is also crowded; see 4.6–4.7 for opened evidence |
**Insight:** Through *Obviously Awesome*: the competitive alternatives for P2 are a $4,200 course and a $249/mo platform. "Eval layer for PMs" alone is not a unique attribute. · **Belief:** contradicts (B2) · **Also changes:** the landing page needs an attribute the alternatives lack.

### 3 · The users' words — approach: HN Algolia, Reddit archive APIs, Quora, PM Q&A, PM blogs · contradicting keys first ("evals overrated", "don't need evals")
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | A PM shipping AI names the problem unprompted: blocked by Sheets, learned Python, wanted "a 'product'" | S13 | HIGH | confirms (B1) | One voice, so weak signal. It is also a seller: he built Beval, a PM eval tool (B2 contradicts) |
| 3.2 | Writer frames evals as "the biggest gap most product managers have"; teams lack them or have ad-hoc ones | S14 | HIGH | confirms (B1) | Educator voice, not an unprompted user complaint. Weak |
| 3.3 | Vendor blog: "Most AI features ship without a structured way to measure quality." | S12 | HIGH | confirms (B1) | Vendor framing, a seller's words, not users'. Also a PM-targeted seller (B2) |
| 3.4 | Eval-startup founder: "Most AI teams don't need evals. They need logging, QA, and taste." | S16 | HIGH | contradicts (B1) | Weak (one voice, 19 likes). Logging and QA may be the language PMs use instead of "evals" |
| 3.5 | Sr. Director PM on Sharebird frames AI evaluation as criteria ("Accuracy is table stakes."), not as a pain | S17 | HIGH | unknown | PMs who talk about it describe a practice, not a problem. Low engagement (2 answers) |
| 3.6 | Nontechnical students form enough of the $4,200 course to get their own study group | S3 | HIGH | confirms (B1) | Behaviour, not words: nontechnical people (likely PMs) pay to fix this |
| 3.7 | Reddit r/ProductManagement could not be read; both archive APIs refused | S23 | ZERO | unknown | The richest PM room is unread, so B1's verbatim evidence is incomplete |
| 3.8 | HN searches for PM first-person eval pain found nothing beyond 3.1; Quora returned nothing | S24, S25 | NONE | contradicts (B1) | Weak: absence on HN, a mostly engineer room |
**Insight:** JTBD: the job is "know whether my AI feature is good enough to ship without waiting on engineering" (S13). The thing being fired is a spreadsheet plus ad-hoc Python. The evidence agrees, but rests on one voice. · **Belief:** B1 weakly confirms; verbatim volume is thin · **Also changes:** use S13's words, not vendor words, if P2 is chosen.

### 4 · Offerings, and evidence of use — approach: opened every pricing page; GitHub API for stars + last push
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Hamel/Shreya *AI Evals For Engineers & PMs*: $4,200, 4.7 (1,019 ratings), 50+ enrolled last week, 4,500+ students claimed | S2 | HIGH | contradicts (B2) | Also confirms B1 by behaviour: thousands pay $4,200 to fix measurement |
| 4.2 | TAI Labs *AI Evals for PMs*: $399, 8 ratings | S4 | HIGH | contradicts (B2) | The low-price PM slot is taken |
| 4.3 | Jules Boiteux *Build Your First AI Eval*: $499, Claude Code-based, positioned against $4,000 courses | S5 | HIGH | contradicts (B2) | Nearest direct competitor to a Claude Code-based PM eval layer |
| 4.4 | Product School *AI Evals Certification*: $2,999 | S6 | HIGH | contradicts (B2) | — |
| 4.5 | AI Product Academy *AI Evals for PMs Certification* (Marily Nika): 4.4 (21 ratings) | S7 | HIGH | contradicts (B2) | — |
| 4.6 | Braintrust Pro $249/mo, free Starter; Confident AI Starter $200/mo | S10, S11 | HIGH | contradicts (B2) | Price anchors for a paid evals layer: $200–249/mo team tools |
| 4.7 | pm-skills: 26,856 stars, pushed 2026-10-09; Product-Manager-Skills: 7,215 stars, pushed 2026-09-01 | S18, S19 | HIGH | unknown | P1 ("AI skills for PMs") faces free, active, far-larger repos |
| 4.8 | hamelsmu/evals-skills: 1,675 stars, pushed 2026-08-16, free companion to the $4,200 course | S20 | HIGH | contradicts (B2) | "Evals as skills" is taken by the category's best-known name |
| 4.9 | Small repos already pair PM skills with evals (/eval-plan, "eval-ready Agentic AI PRD"), each with 0–1 stars | S21 | HIGH | contradicts (B2) | Weak: no uptake, so the idea exists but nobody has won with it |
**Insight:** Through *Crossing the Chasm*: 4,500+ students and a $399–$4,200 price spread show the market is past visionaries. Pragmatists buy the whole product (method + tool + community), which Hamel already bundles (S2, S20). · **Belief:** contradicts (B2) · **Also changes:** paid-layer pricing should anchor against $200–249/mo tools and $399–499 starter courses.

### 5 · Method — the PM canon
| # | Framework · what it predicts here | What the evidence says | Agrees / disagrees | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|---|---|---|
| 5.1 | **Obviously Awesome (Dunford)**: positioning starts from competitive alternatives. If they exist, the frame must lead with an attribute only you have | Alternatives exist on both sides: courses and tools for P2 (2.1–4.6), large free repos for P1 (4.7) | agrees. Neither label is unique. The candidate attribute is "evals that run inside the PM's own Claude Code workflow, with memory"; Boiteux (4.3) and evals-skills (4.8) are its closest rivals | contradicts (B2) | The landing headline should name the attribute, not the category |
| 5.2 | **JTBD (Christensen)**: the real competitor is the current hire, e.g. a spreadsheet | S13: Sheets plus Python is the hire. S12: "a few prompts in a spreadsheet" | agrees, but on one user voice and one vendor | confirms (B1) | Copy should name the spreadsheet as the thing being replaced |
| 5.3 | **Crossing the Chasm (Moore)**: in a category with mass education, the pragmatist majority buys a whole product from the recognised leader | Hamel bundles course + skills + community (S2, S20); 50+ enrolments a week | agrees | contradicts (B2) | A beachhead narrower than "PMs" is needed, e.g. solo PMs without eval engineers (S13) |
| 5.4 | **Inspired, four risks (Cagan)**: value risk first | The paid layer's value risk is unretired: the market pays for eval *education* (4.1–4.5), and willingness to pay for a PM *eval layer in Claude Code* is unmeasured | n/a | unknown | — |
| 5.5 | **The Mom Test (Fitzpatrick)**: method only. Ask PMs about their last AI launch, not about the idea | Not run; it is the instrument for the gap in section 3 | n/a | unknown | Next step |
**Insight:** Dunford: B2 was the reason for P2, and it is gone. P2 survives only if B1 holds strongly enough to win on a unique attribute. · **Belief:** contradicts (B2) · **Also changes:** decision criterion.

### 6 · Cases — approach: course pages, repo history, shutdown notices · searched "Humanloop sunset", "evals course PM enrolment"
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Hamel/Shreya: course-first, then free skills repo; 4,500+ students in 15 months | S2, S20 | HIGH | contradicts (B2) | The model to copy (free skills → paid) is already being run in evals |
| 6.2 | Humanloop, a PM/SME-friendly eval platform, acquired by Anthropic; platform sunset Sep 2025 | S22 | MEDIUM | unknown | A standalone eval tool for non-engineers did not survive alone. Weak, secondary source |
**Insight:** Lean: the cheapest test of "free skills → paid evals" is already visible in Hamel's funnel, so no build is needed to see it work. · **Belief:** contradicts (B2) · **Also changes:** nothing further.

### 7 · Constraints — cut in section 0 (positioning copy has no regulatory or platform constraint); nothing searched.

### 8 · Distribution — approach: where the course and content traffic sits
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Lenny's paid guide "Beyond vibe checks: A PM's complete guide to evals" shows 580 likes, 48 comments | S15 | HIGH | confirms (B1) | Lenny's audience engages with PM evals content at scale. Educator content, not a user complaint |
| 8.2 | Maven's AI Evals category is a discovery surface where PMs browse to fix this | S27 | HIGH | unknown | Any P2 offer is compared side by side there with $399–$4,200 courses |
**Insight:** Crossing the Chasm: the rooms are owned by the category leaders (Lenny, Maven), so reach for P2 means renting their audience or out-specialising them. · **Belief:** unknown · **Also changes:** distribution plan.

## 3 · Verdict
**Rows labelled contradicts in section 2:** 2.1, 2.2, 2.3, 3.4, 3.8, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.8, 4.9, 5.1, 5.3, 6.1. Sweep by text: 3.1 and 3.3 are labelled confirms (B1), but their *Also changes* text names a PM-targeted seller, so they also count against B2. 4.7 (unknown) limits P1, not the belief.

**Belief:** **contradicted.** B2 is false; B1 is weakly confirmed. Three findings decided it: 4.1 (a $4,200 evals course for PMs with 50+ enrolments a week), 2.3 (an eval platform with a "For Product Managers" page), 4.8 (the "evals as Claude Code skills" spot is taken by Hamel's free repo). B1 holds only on behaviour (4.1, 3.6, 8.1) and one unprompted PM voice (3.1).
**Falsifier:** F2 **fired**: people already sell evals to PMs, as at least six courses and two tools. F1 **did not fire**, but it was not fully tested because Reddit was unreadable (3.7).
**Contradicting evidence:** B2: 2.1, 2.2, 2.3, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.8, 4.9, 5.1, 5.3, 6.1, plus the sweep-added 3.1 and 3.3. B1: 3.4 (weak), 3.8 (weak, an empty search).
**Top three, by impact on the goal:**
1. "Nobody sells it" is false. The P2 headline cannot rest on an empty category, and it sits next to $399–$4,200 courses on Maven (2.1, 4.1–4.5).
2. P1 is no safer: free PM-skills repos have 7k–27k stars and are active (4.7). Neither label is a unique attribute (5.1).
3. The job is real but thinly voiced: "replace my spreadsheet + Python without waiting on eng" (3.1, 5.2). If B1 holds in PMs' own words, the defensible angle is that narrower job, run inside Claude Code with memory.
**Dropped:** none.
**Next step:** one named gap: how many of 10 PMs who have shipped an AI feature name measurement as their main problem unprompted, when asked Mom Test-style about their last launch.
**Other gaps — not needed for this decision:** r/ProductManagement verbatim (archive APIs blocked; retry later or read manually) · Reforge and AI Product Academy prices (not in raw HTML) · the current visitor → signup baseline (S1) · willingness to pay for a Claude Code eval layer vs. a course · Humanloop shutdown details from a primary source (S22 is MEDIUM).

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 19:35 IST, before the first search (first SOURCES row came after) |
| 2 Every claim sourced and marked | 31 section-2 rows, each citing S# rows with HIGH/MEDIUM/ZERO/NONE/ASK |
| 3 No snippet-sourced HIGH | 21 HIGH rows, all with URL + date read; search-summary rows marked ZERO (S26) or MEDIUM (S22) |
| 4 Patterns need three | "People sell evals to PMs": 8 independent sellers (S2, S4–S11). B1 "PMs name it": 1 unprompted voice, labelled weak signal |
| 5 Empty angles reported | Angle 7 cut in section 0 and stated; NONE rows S24, S25; ZERO S23 |
| 6 Every insight states impact | Each angle insight carries a Belief + Also changes |
| 7 Verdict honest | 16 labelled contradicts rows + 2 sweep additions, all cited; Dropped: none |
| 8 Ends in a step | one named gap |
| 9 PM canon | 5 frameworks: Dunford, JTBD, Moore, Cagan, Mom Test, each with a prediction and agree/disagree |
| verify_quotes.py | `python3 verify_quotes.py run-05/SOURCES.md` → 29 quotes OK, "0 HIGH row(s) need fixing or downgrading" (first pass flagged 10 CUT + 1 MISMATCH; fixed with ellipses; the S21 search string un-quoted) |
