# Research map — Should the two engineers build AI meeting notes (auto-summary + action items into the booking record) or calendar-sync reliability? — 2026-10-09

## 0 · Ground truth (written 2026-10-09 19:35 IST, before the first search)
**Decision:** Next planning cycle, two engineers go to EITHER (a) AI meeting notes — auto-summary + action items pushed into the booking record — OR (b) the calendar-sync reliability work support keeps escalating. Build A vs build B.

**Goal it serves:** Q1 expansion-revenue target — something that makes an account *add seats* (per-seat pricing, ~400 paying mid-market ops accounts). Not retention. Baseline expansion revenue, target, and seats-per-account: *unknown — ASK (S1)*.

**Belief (split):**
- **B1** — The PM believes ops leads at mid-market B2B scheduling customers want an AI meeting-notes feature inside their scheduling tool (evidence held: three QBR mentions this quarter).
- **B2** — *(unconfirmed, drafted: implied by the decision + goal)* The PM believes shipping that feature would drive seat expansion more than the sync-reliability work would.

**Falsifier (user's own):**
- F1 — no ops people asking for this unprompted anywhere public; OR
- F2 — every tool that shipped it reports that nobody used it.
- F3 *(unconfirmed, drafted for B2)* — evidence that AI notes are now a bundled/commodity feature (free in Zoom/Teams/Meet/standalone notetakers) that does not drive per-seat expansion, or that sync unreliability is a documented churn/seat-loss driver in scheduling tools.

**Already known:** three QBR mentions this quarter (prompted context — a QBR is a vendor-run meeting); support escalations on calendar sync. Nothing else supplied.

**Prove-it note:** the PM wants to "walk into planning with evidence". The map contains what contradicts the belief in its own rows and in section 3; what goes on a slide is the PM's call.

### Angle map and search keys (written before searching; contradicting keys first)
| # | Angle | Keys (contradicting first) |
|---:|---|---|
| 1 | Goal | ASK: expansion baseline/target, seats per account, who pays per seat (ops lead vs. every booker), sync-escalation volume & churn tied to it |
| 2 | Lay of the land | "Calendly AI notes" · "Chili Piper AI meeting notes" · "scheduling tool AI notetaker launch" · "Zoom AI Companion free" · "Google Meet Gemini take notes" |
| 3 | Users' words | contradicting: "too many AI notetakers" · "AI meeting notes useless" · "calendar sync broken calendly" ; confirming: "scheduling tool meeting notes" ops · HN Algolia "meeting notes scheduling" |
| 4 | Offerings + evidence of use | "Calendly notetaker" · "Otter / Fireflies / Fathom pricing users" · "AI notetaker adoption rate" · "nobody used AI summary feature" |
| 5 | PM canon | FRAMEWORKS.md: JTBD, Kano, Mom Test, OST, Cagan four risks, RICE, Lean |
| 6 | Cases | "shut down AI meeting notes feature" · "Calendly acquires notetaker" · "Zoom AI Companion usage numbers" |
| 7 | Constraints | "AI notetaker consent recording law" · "Otter lawsuit" · Google/Microsoft calendar API sync limits |
| 8 | Distribution | in-product to existing 400 accounts; ops communities (r/sales, r/salesops, RevGenius) |

## 1 · The map
The category leader (Calendly) shipped exactly this feature on 2026-08-19 and sells it as a per-seat price add-on, not a seat driver (S3, S4). Notetakers are a crowded, consolidating category (S5, S6). No ops lead was found asking for AI notes inside a scheduling tool, unprompted, in the rooms searched (S14). The demand that does exist is adjacent (sales reps, engineers) and splits: the *write-back into the record* is wanted (S7); the summary itself is distrusted or ignored (S8, S9, S11). Sync failure is a public pain in the leader's own community (S10), but the scale of it for this product is only in the PM's support data (S2).

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Mid-market ops leads (target) | nothing found — searched r/salesops, r/revops, r/CustomerSuccess, web forums (S14) | unknown — ASK (S2) | public, unprompted demand | not located publicly (S25); reachable in-product |
| Sales reps (adjacent) | "The summary just sits there in its own siloed dashboard." (S7) · "Misses chunks of the conversation" (S8) | Gong/Clari-style notetakers pushed by RevOps (S7) | the write into the CRM record (S7) | r/sales |
| Engineers / knowledge workers (adjacent) | "…never … seen … anybody … in any situation, go back to them." (S9) | standalone notetakers | trust in accuracy; a reason to reread | Hacker News |
| Scheduling-tool users with sync failure | "Calendly doesn’t recognize that I have an appointment scheduled, overrides it…" (S10) | Calendly + Google/Outlook calendar | reliable busy-time detection | Calendly community |

**Cases to follow:**
- **Calendly Notetaker (Aug 2026)** — summary + action items + follow-up draft (S3); priced "$10 /seat/mo" add-on (S4). Good: positions on the post-meeting work, the same "push into the record" idea as yours. Bad: no public adoption number (S16). Ugly: entered "a litany of note-takers" (S5).
- **Superhuman acquires Fathom (Sep 2026)** — notes folded into a suite as context for an assistant (S6). Good: shows notes are valued as *input to other workflows*. Bad: price undisclosed; no usage numbers opened.
- **Otter class action (Aug 2025)** — notetaker joined without asking all participants (S12). Ugly: consent is now a build requirement, which Calendly designed around (S13).

## 2 · Angles

### 1 · Goal — read through North Star / input metrics · why: the decision is judged against Q1 seat expansion · searched: nothing; these numbers are the PM's
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | [B2] Expansion baseline, target, seats/account and who holds a seat are not supplied | S1 | ASK | unknown | The decision reverses on these — see section 3 next step |
| 1.2 | [B2] Sync-escalation volume and any seat loss/stall tied to sync are not supplied | S2 | ASK | unknown | If sync blocks wider rollout, sync is an *expansion* lever, not only retention |
| 1.3 | [B2] "Seat compression" (AI reducing seat counts in per-seat SaaS) — snippet-only, weak signal | S19 | ZERO | unknown | Do not cite on a slide |
**Insight:** Through North Star / input metrics, seats grow when more people need to *host* bookings (S4's seat rule); notes help people who already have a seat, so the input notes move is price per seat, not seat count — and the PM's own numbers to check that are missing. · **Belief:** unknown · **Also changes:** next step is a number, not a decision.

### 2 · Lay of the land — why: is this a gap or table stakes? · searched: "Calendly AI notetaker meeting notes launch", "Chili Piper AI meeting notes feature", "Zoom AI Companion included at no additional cost…"
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | [B1] Calendly shipped Notetaker 2026-08-19: summary, key points, action items, follow-up email | S3 | HIGH | unknown | A vendor launch is not buyer demand (Crossing the Chasm misuse); it does make the feature a category expectation |
| 2.2 | [B2] Calendly sells it as "$10 /seat/mo" on top of existing seats; seats belong to hosts, invitees need none | S4 | HIGH | contradicts | The leader monetises notes as ARPU per seat, not as a reason to add seats |
| 2.3 | [B2] TechCrunch: "the competition in this space is intense"; Calendly's CEO: "a litany of note-takers" | S5 | HIGH | contradicts | Customers likely already own a notetaker; you would be replacing, not adding |
| 2.4 | [B2] Zoom AI Companion summaries reportedly free with paid Zoom — not verified | S17 | ZERO | unknown | Verify before using as a pricing argument |
| 2.5 | [B2] Notetaker vendors (Avoma) now bundle scheduling plus CRM push — convergence from the other side | S18 | MEDIUM | unknown | Your competitor set includes notetakers moving into scheduling |
**Insight:** Through Kano (as a hypothesis to measure, not a classification): once the leader ships it, notes trend toward a basic — absence may cost in deals, presence earns little expansion. · **Belief:** contradicts (B2) · **Also changes:** if built, price as an add-on/tier, not as a seat driver.

### 3 · The users' words — why: F1 is about unprompted public asks · searched (contradicting first): "too many AI notetakers…", "meeting notes useless" (HN), Reddit archive API for notetaker/calendly/calendar sync/double booked across 8 subreddits
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | [B1] No ops lead found asking for AI notes inside a scheduling tool, unprompted | S14 | NONE | contradicts | F1 fires within the rooms searched; rooms were limited (see gaps) |
| 3.2 | [B1] Sales rep: summary "sits there in its own siloed dashboard"; they "manually copy-paste the Action Items … into the CRM notes" | S7 | HIGH · adjacent | confirms | The wanted part is the write into the record — your design — not the summary |
| 3.3 | [B1] "Misses chunks of the conversation, mixes up buyers/sellers" — 114 pts | S8 | HIGH · adjacent | contradicts | Accuracy is a usability risk the two engineers would own |
| 3.4 | [B1] HN: never seen anybody go back to AI meeting notes | S9 | HIGH · adjacent | contradicts | Usage risk after launch |
| 3.5 | [B2] Calendly user: calendar synced, still double-booked, "I am at a loss" | S10 | HIGH · weak signal (1 post, 124 views) | contradicts | Sync pain is public even at the category leader |
| 3.6 | [B2] Reddit search for sync/double-booking complaints in 4 subs — nothing relevant | S15 | NONE | unknown | Sync evidence must come from your own tickets (S2) |
**Insight:** Through JTBD, the job users describe is "get what was decided into the system of record without retyping" — notes are the means, and the only voices saying it are adjacent (sales), not ops leads. · **Belief:** contradicts (B1, weak — limited rooms, adjacent evidence on both sides) · **Also changes:** any build scope is the write-back, not the summary.

### 4 · Offerings, and evidence of use — why: F2 is about usage after shipping · searched: "AI meeting summaries feature low adoption…", Superhuman/Fathom, Calendly usage
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | [B1] Fathom is used by "hundreds of thousands of companies" (acquirer's claim) | S6 | HIGH | confirms | The job is real at scale — and largely served already by standalone tools |
| 4.2 | [B1] "Then nobody reads the summaries" — second-hand, on a notetaker vendor's blog | S11 | MEDIUM | contradicts | Weak; vendor-motivated |
| 4.3 | [B1] No tool that shipped notes publicly reports non-use; no adoption number verified either | S16 | ZERO | unknown | F2 is untested, not passed |
**Insight:** Through Cagan's value risk, usage at standalone tools (4.1) retires "does anyone want notes" but not "do *our* buyers want notes *from us*", which is the unretired risk. · **Belief:** unknown · **Also changes:** nothing on F2 — cannot be decided from public data.

### 5 · Method — the PM canon (from FRAMEWORKS.md)
| # | Framework · what it predicts here | What the evidence says | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|---|:--:|---|---|
| 5.1 | [B1] **JTBD** — the job is closing the loop after a booked meeting; the real competitor is the notetaker they already have plus copy-paste | Agrees: S7 (copy-paste), S5/S6 (incumbents) | S20 | MEDIUM | confirms | Competing alternative = existing notetaker; differentiation is only the booking-record write |
| 5.2 | [B2] **Kano** — cannot be classified from Calendly shipping it; needs customers' functional/dysfunctional answers | Evidence has none from your customers | S21 | MEDIUM | unknown | A 2-question Kano pair can go into the interviews below |
| 5.3 | [B2] **Cagan four risks** — notes: value + feasibility (accuracy S8, consent S12) unretired; sync: value retired by escalations, business risk (does it expand?) unretired | Agrees: S8, S12, S2 | S22 | MEDIUM | unknown | Notes carries more open risk for the same two engineers |
| 5.4 | [B1] **The Mom Test** (method) — QBR mentions are vendor-hosted, likely prompted; "it would be nice" is not data | Three QBR anecdotes are the only direct evidence; no unprompted public ask (S14) | S23 | MEDIUM | contradicts | Ask the 3 QBR accounts what they did with notes from their last five booked meetings |
| 5.5 | [B2] **RICE** — Confidence for notes is low (3 prompted mentions), for sync high (escalations); Reach and Impact on seats unknown for both | Evidence cannot fill Reach/Impact (S1, S2 are ASK) | S24 | MEDIUM | unknown | Don't present a RICE score until S1/S2 exist |
**Insight:** Through the opportunity solution tree, notes is a solution picked from three QBRs before the opportunity "accounts add hosts" was mapped; the canon points at testing the expansion assumption first. · **Belief:** contradicts (B1, method-level) · **Also changes:** the next step.

### 6 · Cases — why: who did this, what happened · searched: "Superhuman acquires Fathom notetaker 2026", "AI meeting summaries feature low adoption…"
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | [B2] Notes are being absorbed into suites as context for assistants (Superhuman/Fathom) | S6 | HIGH | contradicts | Inference: notes trend toward a bundled input, not a standalone reason to buy seats |
| 6.2 | [B2] Calendly case: shipped, priced as add-on, no public outcome yet | S3, S4, S16 | HIGH | unknown | Watch Calendly's next earnings/changelog for adoption |
| 6.3 | [B1] No "we shut down our AI notes feature" post found | S16 | ZERO | unknown | F2 neither fired nor passed |
**Insight:** Through Crossing the Chasm (used only to avoid its misuse), vendor launches and acquisitions are supply signals, not buyer adoption; none of these cases shows seat growth from notes. · **Belief:** contradicts (B2, weak) · **Also changes:** nothing to copy on expansion.

### 7 · Constraints — why: changes Effort for two engineers · searched: "Otter.ai class action lawsuit recording without consent notetaker"
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | [B2] Otter sued: notetaker "does not by default ask all the other participants" | S12 | HIGH | unknown | Consent flows are mandatory scope — raises Effort |
| 7.2 | [B2] Calendly built recording disclosure into its notetaker | S13 | HIGH | unknown | This is now table-stakes compliance scope |
**Insight:** Through RICE, consent + recording infrastructure enlarge Effort for notes before any summary work, lowering its score against sync. · **Belief:** unknown · **Also changes:** build estimate.

### 8 · Distribution — why: where would ops leads hear of it · searched: same rooms as S14
| # | Finding ([B1]/[B2] = which belief it judges) | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | [B1] nothing found — no public room where mid-market ops leads discuss scheduling tools was located, searched 2026-10-09 | S25 | NONE | unknown | Distribution is in-product to the 400 accounts; interview them there |
**Insight:** Through the Mom Test, the only reachable sample is the existing customers, so evidence comes from them. · **Belief:** unknown · **Also changes:** next step.

## 3 · Verdict
**Rows labelled contradicts in section 2 (listed first):** 2.2, 2.3, 3.1, 3.3, 3.4, 3.5, 4.2, 5.4, 6.1.

**Belief:** B1 (ops leads want notes) — **still unknown, leaning contradicted**: no unprompted public ask from ops leads (3.1), and the adjacent demand splits — write-back wanted (3.2, 5.1) but the summary is distrusted or ignored (3.3, 3.4). B2 (notes would drive seat expansion more than sync) — **contradicted, weak**: the category leader monetises notes per existing seat, with seats tied to hosts (2.2), in an intense, consolidating market (2.3, 6.1).
**Falsifier:** F1 fired within the rooms searched (3.1). F2 did not fire — untested, no usage data either way (4.3, 6.3). F3 partly fired (2.2, 2.3, 3.5).
**Contradicting evidence:** 2.2 per-seat add-on pricing; 2.3 crowded market; 3.1 no ops ask found; 3.3 accuracy complaints; 3.4 notes not reread; 3.5 public sync double-booking; 4.2 summary fatigue (weak, vendor); 5.4 QBR evidence is prompted; 6.1 notes absorbed into suites.
**Top three, by impact on the goal:** 1. Seats belong to hosts, and the leader charges for notes on existing seats (2.2) — notes is an ARPU play, not a seat play. 2. If sync failures are stalling wider rollout, sync is the expansion lever (1.2, 3.5). 3. Any notes build is worth it only as the booking-record write-back (3.2, 5.1), at extra consent/accuracy Effort (7.1, 3.3).
**Dropped:** none — all nine cited above.
**Next step:** one named gap — the share of the last two quarters' stalled or declined seat expansions in which calendar-sync failures were cited, pulled from support tickets joined to CRM expansion opportunities.
**Other gaps — not needed for this decision:** whether the 3 QBR mentions were unprompted (S2); Zoom bundling (S17); Calendly Notetaker adoption (S16); ops-lead communities beyond Reddit (S25); Kano pair answers from customers.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09 19:35 IST; first SOURCES row read after |
| 2 Every finding sourced and marked | 28 rows, each cites S1–S25 with a mark |
| 3 No snippet-sourced HIGH | 10 HIGH SOURCES rows, all with URL + date; verify_quotes.py: 0 HIGH rows need fixing (S18 MEDIUM UNREACHABLE) |
| 4 Patterns need three | "crowded market" cites S5, S6, S18; single-post findings labelled weak signal (3.5, 4.2) |
| 5 Empty angles reported | 8/8 angles have rows; NONE rows S14, S15, S25 |
| verify_quotes.py | first run: 6 HIGH CUT → ellipses added; second run: all OK, exit 0 |
