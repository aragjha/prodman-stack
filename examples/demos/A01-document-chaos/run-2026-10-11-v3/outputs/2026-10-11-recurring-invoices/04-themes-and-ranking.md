DRAFT, not reviewed by a person

# 04 · Themes and what to build first

## Themes appearing in 3+ independent documents
| Theme | Independent sources | Count | Signal |
|---|---|---|---|
| Chasing late payers by hand is the top pain | #05 support, #08 interview, #03 sales, #11 competitor, #04 Slack | 5 | **Strong** |
| Copying last month's invoice by hand (the recurring-invoices problem) | #09/#02 PRD, #05 support (12 tickets), #08 interview, #14 kickoff | 4 | **Strong** |
| Want to preview / keep control before an invoice sends | #08 interview, #02 R5, #12 design review | 3 | Present |
| Autopay demand is real but limited; card trust is the blocker | #14 kickoff (Rosa for), #08 interview ("most would never give us their card"), #02/#06 (deferred, needs security review) | 3 | Mixed |

Note the tension: the **strongest** theme in the evidence (chasing) is a launch non-goal, while the build (recurring invoices) is the **second** strongest. That is the strategy conflict C3/C4, for leadership.

## What to build first — ranking against the decision (ship the Q4 recurring-invoices launch)
This ranks the *current launch scope* (PRD v2) by evidence and sequencing. Effort is Kwame's (#06); confidence tags per PM.md §3 (HIGH = source opened and quoted; MEDIUM = one source/summary; ZERO = inferred).

| Rank | Build | Effort (#06) | Why first | Confidence |
|---|---|---|---|---|
| 1 | **R1 series engine** (create, schedule, send) | 3w | The core; nothing else works without it. Reminders/autopay/multi-currency all reuse this scheduler (#06). Direct pain in #05, #08, #14. | **HIGH** |
| 2 | **R6 edit future only** | 1.5w | Named by a prospect (#03, Jan fee change) and workshop (#13); protects already-sent invoices. Low effort. | **HIGH** |
| 3 | **R4 pause / resume** | 0.5w | Interview #08 (summer pauses), cheapest item. | **HIGH** |
| 4 | **R5 preview email** | 1w | Interview #08 wants a look before send; now a Must in v2. Settle 24h vs 3-day timing (C7). | **HIGH** |
| 5 | **R3 upcoming-invoices list (60d)** | 1w | Managing partner wants cash-planning view (#03); interview context. | MEDIUM |
| 6 | **R7 custom recurrence rules** | 2w | **Cut candidate.** No customer asked; design unresolved; eng questions it (C6). Only item with evidence against it. | **ZERO** (no demand evidence) |
| — | QA & release hardening | 1w | Fixed cost. | HIGH |

### The one lever you control
Cutting **R7** removes 2 weeks (10w → 8w; full-scope GA Mon 30 Nov → ~16 Nov) and the least-justified item. It does **not** reach the CEO's 31 Oct (that needs ~5.7 weeks total; impossible per #06). Use the saved 2 weeks either to pull GA earlier or to start the 2-week **reminders** fast-follow (which can only begin after R1, per #06).

### Fast-follow to consider (not launch)
**Automatic payment reminders** — 2 weeks, reuses the series scheduler so it starts once R1 lands (#06). It is the strongest demand signal (5 sources) and the clearest competitive gap vs Falcon (#11). Whether it belongs in Q4 is C4, a leadership call tied to the 18%/43% discrepancy (C3).
