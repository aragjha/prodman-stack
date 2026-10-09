# Research map — "AI skills for PMs" vs "the eval layer for PMs shipping AI features" — 2026-10-09

## 0 · Ground truth (written 2026-10-09 16:06 IST, before the first search)
**Decision:** Position the free PM-skills repo's landing page as **(A) "AI skills for PMs"** or **(B) "the eval layer for PMs shipping AI features"**. Copy ships this week. · **Goal it serves:** email signups from the page, target 50 in week 1 (user's number; current baseline unknown — ASK). · **Belief:** B converts better than A because it names a pain A does not. Split: **B1** PMs describe evals as *their own* problem, in their own words (the pain exists and is PM-owned). **B2** no free repo/resource already owns the "evals for PMs" angle (the slot is open). · **Falsifier:** (F1) nobody in the lane describes evals as their problem unprompted, or (F2) a free repo already owns that angle. · **Already known:** the user's own repo (not inspected in this run); nothing else stated. The claim that B "converts better" cannot be tested from public data; the map can only test B1/B2, and the conversion number is the user's (ASK).

**Search keys (problem phrase + platform + company + angle word):**
- A2 lay of land: "AI evals course product managers" · "PM skills claude code github" · "evals for PMs" Lenny / Aakash Gupta / Hamel Husain
- A3 users' words: HN Algolia "product manager evals" · "evals PM" · Reddit r/ProductManagement "evals" (archive API)
- A4 offerings: GitHub "product manager skills" stars + last commit · GitHub "evals product managers"
- A5 canon: Obviously Awesome (positioning), JTBD, Crossing the Chasm (beachhead), Mom Test
- A6 cases: Maven "AI Evals for Engineers & PMs" · Lenny "beginner's guide to AI evals"
- A7 constraints: platform / skill format limits
- A8 distribution: newsletters, communities where PMs discuss evals

Angles cut by the user: none stated. Angle 1 (Goal) = ASK only.

## 1 · The map
| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| New AI PMs shipping a first AI feature | "Is there a simple way to go about this?" (S3) · "A lot of the material I read online is higher level explaining why evals are important…" (S6) | Spreadsheets, LLM-as-judge, threads, paywalled guides (S17, S18) | A simple, worked, real example they can copy, framed for a PM | r/ProductManagement threads (S3–S6), Lenny, Product Compass |
| PMs who already own AI quality | "This is really a PM responsibility and can be the hardest part." (S7) · "intuition IS an eval… it doesn't scale" (S2) | $4,200 course (S16), vendor tools pitched at PMs (S21), Hamel's engineer-framed skills (S15) | A free, PM-framed eval toolkit; the free one that exists is built for coding agents | Maven, vendor content, HN |
| Generalist PMs adopting Claude Code | (no users'-words data retrieved — S24) | Dean Peters' free 7.2k-star repo, "the obvious starting point" (S11, S12); pm-skills (S13) | Not much: the generic slot is filled for free | GitHub, Aakash/Lenny newsletters |
| Senior PMs wary of AI-course hype (counter-segment) | "No, I don't want to enrol on your $2k course on why I should be using evals as a PM" (S9, 338 score) · "gatekeep something that's pretty darn basic" (S10) | Nothing; they resist the category | Proof without hype | r/ProductManagement (largest engagement in the sample) |

**Cases to follow**
- **Hamel Husain: free `evals-skills` repo feeding a $4,200 course** (S15, S16). *Good:* the free repo is the funnel (1.7k stars, explicitly tied to "Engineers & PMs"). *Bad:* it's written for coding agents building LLM evals, so a PM is a guest in it. *Ugly:* "evals as a PM" courses are what r/PM calls grift (S9).
- **Dean Peters: Product-Manager-Skills** (S11, S12). *Good:* 7.2k stars with no company behind it, and a named differentiator ("Always Be Coaching"). *Bad:* it has no evals skill (S11). *Ugly:* it sets the "free" bar every generic PM-skills repo is judged against (S12).
- **Teresa Torres: evals for her Interview Coach** (S19). *Good:* a PM-canon author treats evals as discovery work ("a new discovery habit"). *Bad/ugly:* none found. It is a case study, not a toolkit.

## 2 · Angles

### 1 Goal — approach: the user's own numbers only
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Target is 50 signups in week 1. Visitor volume, baseline signup rate and traffic source are not known | S1 | ASK | unknown | We can't judge whether 50 is reachable under either headline until the traffic number is in |
**Insight:** through North Star thinking, the metric is signups per visitor *by headline*, and the map has no number for it. · **Belief:** unknown · **Also changes:** the next step (section 3).

### 2 Lay of the land — approach: who already sells "AI for PMs" and "evals for PMs", and at what price
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | A free generic PM-skills leader exists and is called "the obvious starting point" for PM craft in Claude Code | S11, S12 | HIGH / MEDIUM | confirms | Under headline A, the repo reads as "another one". (Judges the belief's premise that A names no distinct pain) |
| 2.2 | Evals-for-PMs content is mostly paid or gated: a $4,200 course, a paywalled Lenny guide, gated Product Compass templates | S16, S17, S18 | HIGH | confirms | B2: the *free, PM-framed* slot looks open. Price anchor: free vs $4,200 |
| 2.3 | Vendors already market eval tooling to PMs: "a non-engineer can actually own AI quality week to week" | S21 | HIGH (vendor) | confirms | B1, with vendor framing rather than user words. "Eval layer" is vendor/infra vocabulary |
| 2.4 | Kevin Weil "core skill for PMs" quote: snippet only | S25 | ZERO | unknown | Can't go on the page as a quote |
**Insight:** through *Obviously Awesome*, A's competitive alternative is free and dominant, while B's alternatives are expensive or engineer-framed, so B has a reference set A lacks. · **Belief:** confirms · **Also changes:** B's copy can anchor "free" against "$4,200".

### 3 The users' words — approach: r/ProductManagement via the Arctic Shift archive API, plus HN via Algolia. Searched "evals" in posts and comments; "claude" and "skills" failed
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | PMs ask unprompted how to do evals for their own product (4 independent posts, Feb–Aug 2026) | S3, S4, S5, S6 | HIGH | confirms | B1. Their ask is *simple* and *real example*, not "layer" |
| 3.2 | PMs claim evals as *their* responsibility, in their own words (3 independent writers) | S2, S7, S8 | HIGH | confirms | B1. F1 does not fire |
| 3.3 | Engagement on eval threads is small: 1–12 score, ≤21 comments | S3–S6 | HIGH | unknown | The pain is real but low-volume, so the B audience is narrow. Week-1 traffic matters more (1.1) |
| 3.4 | The single highest-engagement eval mention (338 score) calls "evals as a PM" courses grift | S9 | HIGH, weak signal (1 source) | contradicts | "Eval layer" copy risks reading as hype to senior PMs. Copy must be free, plain and proof-first |
| 3.5 | Top comment on the evals-for-MVP thread: evals are "pretty darn basic" and the field is gatekeeping | S10 | HIGH, weak signal (1 source) | contradicts | If evals read as basic, "layer" oversells. Lead with "simple" |
| 3.6 | No users'-words data retrieved for the generic "AI skills for PMs" framing (API 422) | S24 | NONE | unknown | Comparative pain intensity A vs B is not measured |
**Insight:** through JTBD, the job is "know whether my AI feature is good enough, simply". The pain is PM-owned and in their words (B1), but small and hype-sensitive. · **Belief:** confirms (B1), with two weak contradicting signals on framing · **Also changes:** headline wording.

### 4 Offerings, and evidence of use — approach: opened GitHub repo pages for stars, last commit and skill list
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | The two main free PM-skills repos (7.2k stars, last commit 2026-08-10; and 715 stars) have no dedicated AI-evals skill | S11, S13 | HIGH | confirms | B2: the generic leaders don't own evals |
| 4.2 | A free MIT evals repo exists (1.7k stars) and names PMs in its subtitle ("AI Evals For Engineers & PMs"), but it's written for "AI coding agents to help you build LLM evaluations" | S15 | HIGH | contradicts | B2 / F2 partly fires: the free *evals* slot is taken, but the *PM-framed* one isn't. B must say "for PMs" and mean it |
| 4.3 | alirezarezvani/claude-skills may route "AI evals" inside a product lane; the opened page didn't confirm | S14 | ZERO | unknown | Check before shipping copy that claims "the only" |
| 4.4 | kalyvask "pm-evaluation-framework": snippet only, and the name may mean evaluating PMs | S28 | ZERO | unknown | Same check |
| 4.5 | HN launches of PM-skills repos get ~2 pts, and the PM-evals launch (Beval) got 2 pts | S22, S23 | HIGH | unknown | HN isn't the room for either angle |
**Insight:** through Kano, generic PM skills are now a *basic*: free everywhere, so their presence earns no signups. Evals for PMs is still a *performance* attribute with no free PM-native owner. · **Belief:** confirms (B2) with one contradicting row (4.2) · **Also changes:** copy must not claim "first/only" until 4.3 and 4.4 are checked.

### 5 Method — the PM canon *(never cut)*
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | **Obviously Awesome (Dunford):** positioning starts from competitive alternatives. It predicts A loses to a free incumbent and B wins on "free + PM-framed". Evidence agrees | S11, S12, S15, S16 | HIGH | confirms | Hero line should name the alternative it beats (the $4,200 course or the engineer repo) |
| 5.2 | **Crossing the Chasm (Moore):** a narrow beachhead with a compelling reason wins. It predicts higher conversion per visitor for B, from a smaller pool. Evidence: pain present (3.1, 3.2), volume small (3.3) | S3–S8 | HIGH | confirms | Pool size is the risk to the 50 target, not conversion |
| 5.3 | **JTBD (*Competing Against Luck*):** name the job, not the category. It predicts "eval layer" underperforms "know if your AI feature is good enough". Users ask for "simple" and a "real example" | S3, S6 | HIGH | confirms | Changes copy: B's *angle*, but in user words, not "layer" |
| 5.4 | **The Mom Test (Fitzpatrick):** questions aren't commitments. It predicts the Reddit asks overstate action. The only payment signal is a vendor claim ("50+ enrolled last week", $4,200) | S16 | HIGH (vendor claim) | unknown | The email signup *is* the commitment test, so measure it per headline |
| 5.5 | **Continuous Discovery Habits (Torres):** "evals a new discovery habit". This lets B sit inside PM craft rather than engineering, which predicts less "grift" reading (3.4). The "new chapter" quote didn't verify | S19, S20 | HIGH / ZERO | confirms | Cite S19, never S20 |
**Insight:** four of five frameworks predict B. The Mom Test says none of this is conversion evidence yet. · **Belief:** confirms (direction), unknown (magnitude) · **Also changes:** next step = measure.

### 6 Cases — good, bad, ugly
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Hamel/Shreya: free evals repo plus a $4,200 course with 1,017 reviews, explicitly selling to PMs | S15, S16 | HIGH | confirms | B1: PMs pay for evals. Model: free repo → paid |
| 6.2 | Dean Peters: the generic PM-skills angle drew 7.2k stars in ~8 months, about 4× the evals repo | S11, S15 | HIGH, adjacent (stars ≠ signups) | contradicts | The generic angle has the larger *proven* audience, which is a real risk to a 50-signup target |
| 6.3 | Torres built evals herself for a PM-facing AI product | S19 | HIGH | confirms | Proof a PM-native eval story exists to borrow from |
| 6.4 | Free "Evals for AI PMs" webinar (Aug 2026): snippet only | S29 | ZERO | unknown | Possible competitor in the free slot. Unverified |
**Insight:** through *Escaping the Build Trap*, the outcome is signups, not stars. 6.2 says A's pool is bigger, and 6.1 says B's pool pays. · **Belief:** confirms, with one contradicting case (6.2) · **Also changes:** the risk is reach, not resonance.

### 7 Constraints — approach: platform rules for the rooms in angle 8
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Two eval-promo posts in r/ProductManagement were removed ("Stop Writing PRDs… Start Writing Evals.") | S26 | HIGH | unknown | Distribution: link-drops get removed, so lead with the answer in-thread |
| 7.2 | Sub rules (free version required, Friday Show and Tell): mirror snippet only, and the official page wasn't opened | S27, S30 | ZERO / NONE | unknown | Read the sidebar before posting |
**Insight:** through Shreyas's LNO, this is an O-task: read the rules once, don't research further. · **Belief:** unknown · **Also changes:** distribution plan only.

### 8 Distribution
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | The PM eval conversation lives in r/PM threads (S3–S8), Lenny (S17), Product Compass (S18) and Product Talk (S19). The newsletters gate the practical part | S3–S8, S17, S18, S19 | HIGH | confirms | B2: the free practical version is the gap. Answering threads like 1vh6af2 with the repo is the week-1 reach |
| 8.2 | HN is cold for both angles (~2 pts) | S22, S23 | HIGH | unknown | Drop HN from week-1 |
**Insight:** through the Crossing the Chasm beachhead, B's room is small but findable by thread. · **Belief:** confirms · **Also changes:** where the 50 come from.

## 3 · Verdict
**Contradicts rows in section 2 (listed first):** 3.4 · 3.5 · 4.2 · 6.2

**Belief:** unknown overall. The "converts better" part can't be tested from public pages. B1 is **confirmed** (3.1, 3.2, 6.1: PMs name evals as their own problem, unprompted, and pay $4,200 to learn it). B2 is **partly contradicted** (4.2).
**Falsifier:** F1 did not fire (3.1, 3.2). F2 **partly fired**: a free evals repo exists that names PMs (S15), but it's written for coding agents. No free PM-skills repo has an evals skill (4.1).
**Contradicting evidence:**
- 3.4: the highest-engagement eval mention calls "evals as a PM" courses grift (weak signal).
- 3.5: evals are "pretty darn basic" and the field is gatekeeping (weak signal).
- 4.2: Hamel's free evals repo already names PMs.
- 6.2: the generic angle has a ~4× larger proven audience (adjacent: stars, not signups).

None was dropped.
**Top three, by impact on the goal:**
1. Headline A puts the repo head-on against a free 7.2k-star incumbent that a roundup calls "the obvious starting point" (2.1, 4.1). A gives a visitor no reason to sign up here.
2. B's pain is real and PM-owned, but it's low-volume and hype-sensitive (3.3, 3.4, 3.5). The copy wins on the *job* in user words ("simple", "real example", "know if it's good enough"), free, proof-first. "Eval layer" is vendor vocabulary (2.3, 5.3).
3. The open slot is *free + PM-framed*. The nearest free owner is engineer-framed and feeds a $4,200 course (4.2, 6.1). B's copy must say "for PMs" and mean it, and can't claim "only" until 4.3 and 4.4 are checked.

**Next step — one named gap:** the signup rate per visitor of headline A vs headline B, on the same week-1 traffic. The decision reverses on this number and the map doesn't have it (1.1, 5.4). Where to look: the user's own landing page, with the two hero headlines split 50/50 from day 1, plus S1's visitor baseline to know when the split has enough visitors to read.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09 16:06 IST. All 30 SOURCES rows read afterwards |
| 2 Every claim sourced and marked | 29 section-2 rows, each cites S#; every S# has a mark |
| 3 No snippet-sourced HIGH | 20 HIGH rows, all with URL + date read. 6 snippets marked ZERO (S14, S20, S25, S27, S28, S29); 2 NONE (S24, S30) |
| 4 Patterns need three | 3.1 = 4 sources, 3.2 = 3, 2.2 = 3. Single-source claims 3.4 and 3.5 labelled weak signal |
| 5 Empty angles reported | 8/8 present. Empty searches shown as S24, S30 |
| 9 Canon | 7 named: Obviously Awesome, Crossing the Chasm, JTBD, Mom Test, Continuous Discovery Habits, Kano, Escaping the Build Trap (+ LNO, North Star in insights) |
