# Research map — Should we build AI meeting notes into the booking record, or spend the two engineers on calendar-sync reliability? — 2026-10-09

## 0 · Ground truth (written 2026-10-09T10:35:19Z, before the first search)
**Decision:** Build (AI meeting notes: auto-summary + action items pushed into the booking record) vs. allocate the same two engineers to calendar-sync reliability work, for the next planning cycle.
· **Goal it serves:** Q1 expansion-revenue target. The feature must make an account *add seats*, not just reduce churn (user's own framing; the target number itself is not yet given — ASK).
· **Belief:** Ops leads at mid-market B2B scheduling customers want an AI meeting-notes feature in the scheduling product (evidence so far: it came up in three QBRs this quarter).
  - **B1 (demand):** ops leads at this kind of customer want it, and say so unprompted.
  - **B2 (expansion, drafted — *unconfirmed*):** building it would drive seat expansion (the goal the user named). The user did not state this as a belief; it is implied by the goal and is judged separately.
· **Falsifier (user's own):** (a) no ops people asking for this unprompted anywhere public; or (b) every tool that shipped it reports nobody used it.
  - Drafted addition (*unconfirmed*): B2 is falsified if comparable tools gate/price notes in a way that does not tie to seat count, or if the sync-reliability problem shows evidence of driving churn/contraction that would offset expansion.
· **Already known:** Three QBR mentions this quarter (unprompted vs. prompted unknown). ~400 paying accounts, per-seat pricing, mid-market ops teams. Support repeatedly escalates calendar-sync reliability issues.

### Angle map and search keys (shown before searching; nothing cut — angle 1 needs the user's numbers)
| # | Angle | Search keys (problem phrase + platform + company + angle word) |
|---:|---|---|
| 1 | Goal | ASK: Q1 expansion target, seats/account, sync-ticket volume, churn reasons |
| 2 | Lay of the land | "Calendly AI notetaker", "Chili Piper / Cal.com / Zoom Scheduler / HubSpot meetings AI notes", "Calendly acquires", pricing pages |
| 3 | Users' words | HN Algolia "meeting notes scheduling", Reddit "calendly sync issue", "double booked calendly", "ai notetaker useless", Quora |
| 4 | Offerings + use | Otter/Fireflies/Fathom/Read pricing pages, open-source notetakers on GitHub (stars + last commit), Calendly notetaker adoption |
| 5 | PM canon | JTBD, Kano, Mom Test, Opportunity Solution Tree, RICE, Escaping the Build Trap |
| 6 | Cases | "Calendly Notetaker launch", "Zoom AI Companion usage", "AI notetaker adoption low", shut-down posts |
| 7 | Constraints | recording consent laws (two-party consent), Google/Microsoft calendar API limits, bot-join policies, LLM cost per meeting |
| 8 | Distribution | where ops leads gather: r/RevOps, r/sysadmin, RevOps Co-op, Pavilion, newsletters |

> All eight angles kept (the run is non-interactive; cut any that don't bear on planning). Each row's Finding starts with the sub-belief it judges: [B1] demand · [B2] seat expansion.

## 1 · The map
| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| RevOps / ops leads (direct) | "Meetings logged with notes can be automated using an AI notetaker like Fathom.ai … automatically create tasks … based on the action items" (S12) | Fathom, Fireflies piped into HubSpot (S11, S12) | Nothing found asking for notes *inside the scheduler* (S31) | r/RevOps; RevOps Co-op, 21k members (S33) |
| Mid-market Google/Zoom shops (direct) | "If a meeting was scheduled with Google Calendar, the notes are also attached to the meeting." (S9) | Gemini notes on Business Standard+ (S9); ZoomMate (S8) | Push into a *booking record* (vs. calendar event / CRM) | Their admin console, already bought |
| Scheduling-tool users hit by sync (adjacent: SMB/coaches, plus one r/Calendly team) | "…stopped the whole double/ghost event mess for us" (S20); "Seen coaches lose bookings…" (S19) | Calendly, Acuity, switching tools (S18, S20) | Reliable two-way sync; even Calendly staff say they are "working on" it (S21) | r/Calendly, r/smallbusiness, HN |
| Meeting guests / external participants | "'AI Notetaker' is the same as 'I secretly recorded this'" (S16) | Nothing — they're the ones being recorded | Consent every time (S24) | Your customers' customers |

**Cases to follow**
1. **Calendly Notetaker (Aug 2026).** Did: shipped recaps linked to contact + event type, bundled into "Plus" tiers at +$8/seat (S3, S5, S6). Good: 100k beta recordings, "highest satisfaction" (vendor claim, S3). Bad: it's an all-or-nothing tier, so 4 of 12 users wanting recaps means paying for 12 (S6). Ugly: a bot joined a confidential meeting the user "Never turned it on" for (S23). Copy the **post-meeting workflow** idea (S4), not the bundling.
2. **Cal.com 6.7 (Jul 2026).** Auto summaries "saved alongside transcripts" (S7). The second scheduling competitor with notes, so this is parity now, not a differentiator.
3. **Google Meet "Take notes for me".** Notes already attached to the calendar event on Business Standard+ (S9). This is the free alternative your buyers already pay for, and the test any build has to beat.

## 2 · Angles

### 1 · Goal — approach: ask, never substitute the web's numbers
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | [B2] Q1 expansion target, baseline and seats-per-expansion are not in hand | S1 | ASK | unknown | Without it nothing can be sized, so it decides the next step |
| 1.2 | [B1] Were the 3 QBR mentions unprompted? And how much contraction ARR sits on sync-escalating accounts? | S2 | ASK | unknown | If sync accounts are contracting, the "retention, not expansion" framing breaks |
**Insight:** Through North Star logic, the goal is seats added. Neither option has been tied to that number yet. · **Belief:** unknown · **Also changes:** the next step (section 3).

### 2 · Lay of the land — approach: competitor launches, pricing, platform bundles · searched Calendly/Cal.com/Chili Piper/Zoom/Google notes launches
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | [B1] Calendly, the category leader, shipped Notetaker on 2026-08-19 with recaps linked to contact + event type | S3 | HIGH | confirms | The feature is now parity, so not shipping it may become a gap within a year |
| 2.2 | [B2] Calendly's CEO: "There's a litany of note-takers, and all of them do a great job…". Differentiation is post-meeting work | S4 | HIGH | contradicts | Commodity, so a plain summary won't move seats. Only the booking-record workflow could |
| 2.3 | [B1] Cal.com 6.7 added auto summaries (Jul 2026) | S7 | MEDIUM | confirms | Two scheduling competitors have it (weak signal: 2 sources, not 3) |
| 2.4 | [B2] Google Workspace Business Standard+ attaches Gemini notes to the calendar event | S9 | HIGH | contradicts | Many mid-market buyers already own the feature. Build = substitution |
| 2.5 | [B2] Zoom gives free summaries (3 meetings/mo) and unlimited on paid | S8 | HIGH | contradicts | Same: bundled by platforms buyers already pay for |
| 2.6 | [B1] Chili Piper: no AI meeting-notes launch found | S34 | NONE | unknown | Not every sales-scheduling tool has followed, so parity pressure is uneven |
**Insight:** Through Kano (S28), meeting notes are moving from delighter to basic as Calendly, Cal.com, Google and Zoom bundle them. A basic earns no expansion. · **Belief:** contradicts (B2) · **Also changes:** if built, it must be scoped as parity at minimum cost (buy transcription, e.g. Recall.ai per S6), not as the expansion bet.

### 3 · The users' words — approach: HN Algolia, Reddit archive APIs (pullpush, arctic-shift); verbatim only · searched "AI notetaker", "calendly sync", "calendly double booked", r/RevOps "notetaker", r/Calendly "sync"/"notes"
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | [B1] RevOps people pipe Fathom summaries + action items into HubSpot tasks | S12 | HIGH | confirms | The job (outcomes into the system of record) is real and already served by a separate tool |
| 3.2 | [B1] RevOps use Fireflies/Fathom to confirm attendance / no-shows | S11, S13 | HIGH | confirms | An adjacent job: no-show detection is a *scheduling* job notes could serve |
| 3.3 | [B1] HN user: notetaker "allowed me to focus on the person" (adjacent: not ops) | S14 | HIGH | confirms | — |
| 3.4 | [B1] HN: doctor dropped it, "They weren't his notes, and there was too much extraneous detail" (adjacent: clinical) | S15 | HIGH | contradicts | Output quality decides retention of the feature |
| 3.5 | [B1] No ops lead found asking unprompted for notes *inside a scheduling/booking product* | S31 | NONE | contradicts | User's falsifier (a) fires for the specific placement (searches partly rate-limited, so the search was incomplete) |
| 3.6 | [B1] Sync pain: team switched tools to stop "the whole double/ghost event mess" | S20 | HIGH | unknown | Sync failure is a switching trigger, which is churn risk |
| 3.7 | [B1] Calendly staff: still "working on" two-way Google sync (Dec 2025) | S21 | HIGH | unknown | Even the leader hasn't solved it. Reliability could position you |
| 3.8 | [B1] Double-booking pain recurs across independent SMB/coach threads (adjacent segment) | S17, S18, S19, S22 | HIGH | unknown | Pattern (≥3 sources) but **adjacent** (SMB, not mid-market ops) |
**Insight:** Through JTBD (S30), the job ops people hire for is "get meeting outcomes into the system of record". They hire Fathom/Fireflies for it today and point it at the CRM, not the scheduler. Unprompted pain about *sync* is more visible than unprompted demand for *notes in the scheduler*. · **Belief:** contradicts (B1, placement) · **Also changes:** if notes ship, the target is "CRM/booking-record write-back", not "summary".

### 4 · Offerings, and evidence of use — approach: pricing pages, GitHub, adoption stats
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | [B2] Calendly monetises Notetaker via "Plus" tiers, not in Free. It's a per-seat **price uplift**, not more seats | S5 | HIGH | contradicts | Expansion would come from ARPU, not seat count. Ask whether Q1 target counts ARPU |
| 4.2 | [B2] +$8/seat flat; "twelve-person team where four people actually want meeting recaps" pays for 12 | S6 | MEDIUM | contradicts | Only a minority of seats may want it, so a seat-based uplift gets resisted |
| 4.3 | [B1] Calendly beta: 100k+ recordings, "highest satisfaction score" (vendor claim, unaudited) | S3 | HIGH | confirms | User's falsifier (b) does **not** fire: a shipper reports use |
| 4.4 | [B2] Open-source Meetily: 31.6k stars, local transcription + summarisation (last commit unverified) | S10 | HIGH | unknown | The tech is cheap and commodity. Build cost is integration, not AI |
| 4.5 | [B1] "41% … actively use AI meeting features at least monthly": snippet only | S27 | ZERO | unknown | Not used for anything |
**Insight:** Through Kano + pricing, notes earn money as a tier uplift on seats you already have (Calendly), not by adding seats. · **Belief:** contradicts (B2) · **Also changes:** reframe the build as an ARPU test if built at all.

### 5 · Method — the PM canon (never cut)
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | [B2] **Kano** predicts: once a feature is bundled everywhere it becomes must-be. Its absence costs, its presence earns nothing. Sync reliability is a must-be: "when done poorly, customers are very dissatisfied." Evidence agrees: 2.2, 2.4, 2.5 (notes going basic), 3.6, 3.7 (sync failure causes switching) | S28 | HIGH | contradicts | Notes ≠ expansion lever. Sync is a churn guard, and churn guards don't hit an expansion target directly |
| 5.2 | [B1] **The Mom Test** predicts: QBR mentions are opinions about a hypothetical future, inflated because "everyone is lying to you". Only past behaviour and money count. Evidence: can't judge. Whether the QBRs were prompted is unknown (1.2) | S29 | HIGH | unknown | The cheapest test: ask the 3 QBR accounts what they use and pay for notes *today* |
| 5.3 | [B1] **JTBD** (*Competing Against Luck*) predicts: the job, not the feature, decides. The competitor is Fathom/Gemini already hired. Evidence agrees: 3.1, 3.2, 2.4 | S30 | ZERO | confirms | The job is real, but your product wins only where the booking record is where ops acts next |
**Insight:** All three frameworks point the same way. The job is real (JTBD), the feature is becoming basic (Kano), and the QBR signal is untested (Mom Test). · **Belief:** contradicts (B2), unknown (B1) · **Also changes:** next step is a Mom Test check, not a build.

### 6 · Cases — good, bad, ugly · searched Calendly/Cal.com launches; "sunset/shutting down AI meeting notes" (S32)
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | [B1] Ugly: Calendly Notetaker showed up in a confidential meeting; user "Never turned it on" | S23 | HIGH | unknown | Spec: default-off, per-meeting opt-in, visible consent |
| 6.2 | [B1] No post-mortem found of a scheduling tool killing notes for low usage | S32 | NONE | unknown | Falsifier (b) unsupported either way beyond S3 |
**Insight:** Through *Escaping the Build Trap* (outcomes over output), the only public case with numbers is a vendor's own launch claim. There's no independent usage evidence either way. · **Belief:** unknown · **Also changes:** consent design is a must-have in any spec.

### 7 · Constraints — approach: legal commentary, consent survey
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | [B2] Otter.ai class action under ECPA, CFAA, CIPA. Counsel: "Obtain consent from all participants, including external parties" | S24 | HIGH | unknown | Consent flows + legal review add scope to the "two engineers" estimate |
| 7.2 | [B2] 65.3% say notetaker consent is inconsistent or missing (survey, n=500) | S25 | MEDIUM | unknown | Guests (your customers' customers) are a trust risk |
| 7.3 | [B2] NPR coverage of the suit, not read (timeout) | S26 | ZERO | unknown | — |
| 7.4 | [B2] Calendly pays OpenAI + Recall.ai per meeting, unmetered | S6 | MEDIUM | unknown | Per-meeting COGS reduces margin on a flat per-seat price |
**Insight:** Through RICE, the constraints cut *Effort* and *Confidence*. Consent + recording infra makes notes larger than "two engineers, one cycle". · **Belief:** unknown · **Also changes:** effort estimate for the notes option.

### 8 · Distribution — approach: rooms from angle 3 + one community search
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | [B1] RevOps people talk notetaker→CRM workflows in r/RevOps | S11, S12, S13 | HIGH | unknown | Where to recruit Mom Test interviews beyond your base |
| 8.2 | [B1] RevOps Co-op: 21k members, private Slack, newsletter | S33 | HIGH | unknown | Second room. Newsletters/events beyond this one were not searched |
**Insight:** Through *Crossing the Chasm*, you don't need new distribution for this decision. Your 400 accounts are the beachhead to test with. · **Belief:** unknown · **Also changes:** nothing in the decision.

## 3 · Verdict
**Contradicting rows labelled in section 2 (listed first):** 2.2, 2.4, 2.5, 3.4, 3.5, 4.1, 4.2, 5.1.

**Belief:**
- **B1 (ops leads want it): unknown.** The *job* is confirmed (3.1, 3.2 — they already pipe Fathom/Fireflies notes into the CRM), a leader shipped it and reports use (2.1, 4.3). But no one was found asking for it *inside a scheduler* (3.5), and the 3 QBRs are untested against the Mom Test (5.2).
- **B2 (it drives seat expansion, drafted/unconfirmed): contradicted.** The best comparable monetises it as a per-seat price uplift, not added seats (4.1, 4.2). Google and Zoom bundle it for buyers who already pay them (2.4, 2.5). Calendly's CEO calls it a "litany" (2.2). Kano predicts a basic earns nothing (5.1).

**Falsifier:** (a) **fired, weakly.** No unprompted public ask for notes inside a scheduling product (3.5), though the searches were partly blocked. (b) **did not fire.** Calendly reports 100k+ beta recordings (4.3, vendor claim).

**Contradicting evidence:** 2.2 (commoditised, says the CEO who shipped it) · 2.4 (Google attaches notes to the event already) · 2.5 (Zoom bundles summaries) · 3.4 (adjacent: notes dropped for quality) · 3.5 (no unprompted placement demand found) · 4.1 (monetised as price uplift, not seats) · 4.2 (only 4 of 12 seats may want it) · 5.1 (Kano: basic, earns nothing). None dropped.

**Top three, by impact on the Q1 expansion goal:**
1. **Notes don't add seats; at best they raise price per seat** (4.1, 4.2). If Q1 counts only seat adds, notes miss the goal by design.
2. **Your buyers likely already own a substitute** (2.4, 2.5, 3.1). The build is a substitution sale against Gemini/Zoom/Fathom, so expansion depends on how many accounts *don't* have one.
3. **Sync is a Kano must-be and a switching trigger** (3.6, 3.7, 5.1). Like notes, it doesn't add seats. But it protects the base you'd be expanding, and the leader hasn't solved it.

**Next step — one named gap:** *what share of your expansion-candidate accounts already have a meeting-notes tool* (Google Workspace Business Standard+ with Gemini notes, paid Zoom AI, Fathom/Fireflies/Gong), and what the 3 QBR accounts use and pay for notes today. Where to look: your CRM's tech-stack/firmographic fields plus three 20-minute Mom Test calls with the QBR accounts ("Walk me through what happened to the notes from your last ops review"). If most already own a substitute, the decision goes to sync. If not, spec notes as a priced tier and test it as ARPU.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09T10:35:19Z, before the first search. SOURCES rows all dated 2026-10-09 (row times not stamped) |
| 2 Every claim sourced and marked | All 32 rows cite an S# with a mark |
| 3 No snippet-sourced HIGH | Every HIGH has a URL + date read. Snippet-only claims (S27) and unread pages (S26, S30) are ZERO |
| 4 Patterns need three | 3.8 cites 4 sources, labelled adjacent. 2.3 (2 competitors) labelled weak signal |
| 5 Empty angles reported | All 8 angles have rows. Empty searches are S31, S32 (NONE) |
| 6 Every insight states impact | Yes. Each insight carries Belief + Also changes |
| 7 Verdict honest | 8 contradicting rows labelled, 8 cited in section 3, none dropped |
| 8 Ends in a decidable step | One named gap: substitute-tool share among expansion candidates + 3 QBR Mom Test calls |
| 9 PM canon | Kano, Mom Test, JTBD with predictions vs evidence. Build Trap, RICE, Crossing the Chasm used in insights |
