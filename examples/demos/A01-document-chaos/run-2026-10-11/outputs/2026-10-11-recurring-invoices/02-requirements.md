# 02 · Deduplicated requirements (launch scope)

Source of truth: **PRD v2 (28 Aug, #02)**, cross-referenced to every other doc that states the same
thing. Duplicates from the merged list (#13) and design review (#12) are folded in, sources kept.

| ID | Requirement (PRD v2 wording) | Priority (v2) | Also appears in | Confidence |
|---|---|---|---|---|
| R1 | Ledgerly creates and emails each invoice in a series on its scheduled date | Must | v1 R1; #13 wkshp 1; #12 "auto send on billing date"; interview #08; kickoff #14 | HIGH |
| R3 | Firm admins see every scheduled invoice for the next 60 days in one list | Must | v1 R3 (was **30 days**); #13 wkshp 4 ("next two months"); #12 (60 days, by week); sales #03 ("next month's billing in one place") | HIGH |
| R4 | Pause a series and resume it later without losing its settings | Must | v1 R4; #13 wkshp 3 & 11; #12 (paused banner); interview #08 ("stop over summer… remember to start again") | HIGH |
| R5 | The owning accountant gets a preview email 24h before an invoice is sent | Must (was Should in v1) | v1 R5; #13 wkshp 5; #12 (**3 days** before — conflict, see 03); interview #08 ("I'd still want to look at them") | HIGH |
| R6 | Changing a series updates future invoices only, never invoices already sent | Must | v1 R6; #13 wkshp 2 & 8; sales #03 (fee change must not alter sent invoices) | HIGH |
| R7 | Custom recurrence rules (e.g. every 2nd Tuesday, last working day) | Should | v1 R7; #13 wkshp 6 | **ZERO customer demand** — see note |

## Dropped from launch (were in v1 or raised, now non-goals in PRD v2)
| Item | Status per current docs | Source |
|---|---|---|
| Autopay (v1 R2, Must) | Non-goal → phase 2 / Q1 2027; needs a security review that can't finish this quarter | PRD v2 #02; estimate #06 (5 wks + 3–4 wk review) |
| Multi-currency recurring (EUR) | Non-goal for launch | PRD v2 #02 — but sales committed it verbally (conflict, see 03) |
| Automatic payment reminders | Non-goal "this year" | PRD v2 #02; CEO parked it #10 (conflict with evidence, see 03) |

## Requirements with thin or no evidence
- **R7 custom recurrence rules**: no customer asked for it. The one interview (#08) says "Everyone is
  billed on the first. Four or five clients are quarterly. That's it." Design (#12) tested a 9-control
  rules builder that "tested badly with 2 internal users." Kwame (#04): "does anyone actually need every
  second Tuesday? custom rules are the gnarliest part of the build" — 2 weeks of the 10. **Candidate to cut.**
