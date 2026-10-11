# Run demo3b-A01-document-chaos

| Field | Value |
|---|---|
| Wall clock | 536 s |
| Turns | 30 |
| Tokens (all, incl. cache) | 920,116 |
| Cost reported by the CLI | 2.6928642499999995 |
| Error | False |

## Final message, unedited

All eight A01 steps are done, saved, and independently checked. Here's the handback.

---

**RESULT** — 15 documents reconciled. Current launch scope is **PRD v2** (R1, R3, R4, R5, R6, R7). **5 live contradictions**; 4 others already settled by newer documents. Build the **series engine (R1) first**. The single best-evidenced customer pain — **automatic payment reminders — is parked**, and that is the main thing for the CEO to decide. Full files in `outputs/2026-10-11-recurring-invoices/`.

**ROUTE** — A01 (document chaos to product clarity), because 15 documents from different authors and dates must be reconciled before a plan can be ranked. Skill run: `pm`. No outside skills, fallbacks or connectors.

**CHECKS** — 125 rows, 1 corrected, 0 removed · checked by an **independent subagent** (saw only your 15 input files + the artifacts) · [`07-check.md`](outputs/2026-10-11-recurring-invoices/07-check.md). The one fix: a PRD-v2 quote in C1 was missing an ellipsis; corrected. Effort totals, ticket counts, the 18%/43% figures, dates, and all quotes verified against source.

---

### Which documents you can stop reading
Four are superseded — keep only for provenance:
- **07 pricing-note** → replaced by **15** (add-on and 0.5% autopay fee both withdrawn)
- **09 PRD v1** → replaced by **02**
- **13 requirements-list-merged** (Noor's own note: "haven't merged duplicates") → folded into 02
- **14 kickoff-notes** → scope overtaken by 02/01/06

Everything else is live: the plan (01, 02, 06, 15), current design/eng facts (12), and the evidence base (03, 04, 05, 08, 10, 11).

### What you actually agreed (current scope, in build order)
| # | Requirement | Effort (Kwame, 06) | Evidence |
|---|---|---|---|
| 1 | R1 Series engine | 3 wks | HIGH — everything depends on it; reminders reuse it |
| 2 | R6 Edit future invoices only | 1.5 wks | HIGH |
| 3 | R4 Pause / resume | 0.5 wk | HIGH |
| 4 | R3 Upcoming list, 60 days | 1 wk | MEDIUM |
| 5 | R5 Preview email | 1 wk | HIGH |
| 6 | R7 Custom recurrence rules | 2 wks | **ZERO/weak — first cut candidate** |

10 weeks from a 21 Sep start → GA 30 November. Autopay is settled as phase 2 / Q1 2027.

### NEEDS YOUR JUDGMENT
1. **Launch date (C1).** CEO told the board **31 October** (9 Sep); newest estimate and roadmap say **30 November** (12 & 16 Sep) on a 10-week build. ~4-week gap — move the date or cut scope. *Owner: Daniel + eng.*
2. **Reminders + the number behind the call (C2).** CEO: "Only 18% of our invoices are paid late" → "nice to have." Support dashboard: "43% of invoices… paid after their due date." Reminders are the **strongest demand (6 sources), top churn reason, and the competitive gap vs Falcon** — yet parked. Reconcile 18% vs 43%, then decide. *Owner: leadership + finance.*
3. **EUR commitment (C3).** Sales promised a 40-seat prospect multi-currency "at launch" **in writing**; PRD v2 excludes it. Decide before the proposal goes out (close target end of Sept). *Owner: you + sales.*
4. **Cut R7? (C5).** Origin unknown (Maya), one interviewed customer doesn't need it, tested badly, costs 2 weeks — cleanest lever toward 31 Oct. *Owner: you.*
5. **Preview timing (C4).** PRD v2 says 24 hours; design review says 3 days. *Owner: you.*

### NEXT ACTIONS
1. Put **C1 (date)** and **C2 (reminders + the 18%/43% number)** on one page for the CEO — these two decide the Q4 story. *(you)*
2. Settle the 43%-vs-18% figure with finance/support so the meeting runs on one number. *(you → finance)*
3. **Hold the prospect proposal** until the EUR commitment is confirmed or corrected. *(you → sales)*

**ASSUMPTIONS** — "Current" = newest document per topic, except explicit supersedes (02>09, 15>07). Effort weeks are Kwame's, carried as given. No `context/PRODUCT.md`, `DECISIONS.md` or `CORRECTIONS.md` exist (templates only), so metrics/decisions come only from these 15 files.

**CONFIDENCE** — Medium. The conflicts are clear, but this is one PM's folder: a single customer interview, one support period, and two load-bearing numbers (launch date, % paid late) openly disagree between documents.

Nothing was sent, posted, or shared — all outputs are local drafts marked DRAFT. Want me to turn this into the one-page decision brief for the CEO (C1 + C2 front and centre), or draft the message correcting the EUR commitment to the prospect?
