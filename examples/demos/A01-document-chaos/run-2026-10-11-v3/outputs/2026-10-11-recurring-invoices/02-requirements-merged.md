DRAFT, not reviewed by a person

# 02 · Requirements, extracted and merged (A01 steps 2–3)

Current launch scope is PRD v2 (02, 28 Aug), which supersedes v1. Below: each v2 launch requirement, every other document that states the same thing (merged), and its source trail. Duplicate phrasings from the raw workshop list (13) and design review (12) are folded in.

| v2 # | Requirement (v2 wording) | Priority (v2) | Also appears in | Eng estimate (06) |
|---|---|---|---|---|
| R1 | Ledgerly creates and emails each invoice in a series on its scheduled date | Must | 09 R1; 13 #1; 12 "auto send on the billing date"; 08 "copy last month's invoice… sixty times"; 14 | 3 wks |
| R3 | Firm admins see every scheduled invoice for the next 60 days in one list | Must | 09 R3 (30 days); 13 #4 ("next two months"); 12 "next 60 days, grouped by week"; 03 "next month's billing in one place" | 1 wk |
| R4 | Pause a series and resume it later without losing its settings | Must | 09 R4; 13 #3, #11; 12 "paused series shows a banner"; 08 "clients stop their retainer over the summer" | 0.5 wk |
| R5 | The accountant who owns the client gets a preview email 24 hours before an invoice is sent | Must | 09 R5 (Should); 13 #5; 12 "preview email… 3 days before send"; 08 "I'd still want to look at them before they go out" | 1 wk |
| R6 | Changing a series updates future invoices only, never invoices already sent | Must | 09 R6; 13 #2, #8; 03 "a fee change never alters invoices already sent"; 08 (fees up every January, via 03) | 1.5 wks |
| R7 | Custom recurrence rules (e.g. every second Tuesday, last working day of the month) | Should | 09 R7; 13 #6; 12 "needs a rules builder" | 2 wks |
| — | QA and release hardening | — | — | 1 wk |
| | **Total (v2 scope)** | | | **10 wks** |

**Dropped from v1 → v2:** R2 Autopay (was Must in v1 09). v2 moves it out of launch to phase 2 / Q1 2027 (02; roadmap 01). Resolved by the newer PRD — not a live conflict.

## Requirements asked for but NOT in v2 launch scope
| Item | Where asked | v2 status |
|---|---|---|
| Automatic payment reminders for overdue invoices | 05 (31 tickets); 08; 03; 04; 11; 13 #10 | Non-goal "separate initiative, not planned this year" (02) |
| Multi-currency recurring invoices (EUR) | 03 (prospect, promised by sales); 13 #9 | Non-goal "any currency other than the firm's default" (02) |
| Autopay | 09 R2; 14; 13 #7; 08 (mixed) | Phase 2 / Q1 2027 (02, 01) |

These three are the contested scope. Reminders and multi-currency carry live contradictions — see [03-conflicts.md](03-conflicts.md).
