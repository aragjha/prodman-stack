DRAFT, not reviewed by a person

# 02 · Deduplicated requirements, with sources

Every requirement below merges duplicates across documents. "Current status" = per PRD v2 (#02, 28 Aug), the current spec, with later refinements from the design review (#12, 1 Sep). Duplicates in the merged list (#13) are mapped to their canonical requirement.

| ID | Requirement (merged) | Current status (PRD v2) | Sources |
|---|---|---|---|
| R1 | Create, schedule and email each invoice in a series on its date (auto-send, no manual approval by default) | **Must — launch** | #09 R1, #02 R1, #13 (items 1, "auto send on billing date"), #12 (agreed), #06 (3w) |
| R3 | Firm admins see all scheduled invoices in one list | **Must — launch; 60 days** (was 30 in v1) | #09 R3 (30d), #02 R3 (60d), #13 (item 4 "next two months"), #12 (60d, grouped by week), #06 (1w) |
| R4 | Pause a series and resume later without losing settings | **Must — launch** | #09 R4, #02 R4, #13 (items 3, 11), #12 (paused banner), #06 (0.5w) |
| R5 | Preview email to the accountant who owns the client before send | **Must — launch** (v1 had it as Should; v2 Must). Timing: v2 says 24h, #12 says **3 days** | #09 R5 (Should, 24h), #02 R5 (Must, 24h), #13 (item 5), #12 (3 days), #06 (1w) |
| R6 | Editing a series changes future invoices only, never ones already sent | **Must — launch** | #09 R6, #02 R6, #13 (items 2, 8), #03 (office manager, Jan fee change), #06 (1.5w) |
| R7 | Custom recurrence rules (e.g. every 2nd Tuesday, last working day) | **Should — launch** (lowest priority) | #09 R7 (Should), #02 R7 (Should), #13 (item 6), #12 (not agreed; builder tested badly), #04 (Kwame questions need), #06 (2w) |
| R2 | Autopay: charge saved card automatically when invoice issues | **Out of launch → phase 2 (Q1 2027)**; needs security review | #14 (Rosa: must be in v1), #09 R2 (Must), #02 (non-goal, phase 2), #13 (item 7), #01 (Q1 2027), #06 (5w + security review) |
| X1 | Automatic payment reminders for overdue invoices | **Non-goal / parked** ("separate initiative, not planned this year") | #02 (non-goal), #05 (31 tickets), #08, #03, #11, #04, #01 (parked), #06 (2w, reuses scheduler) |
| X2 | Multi-currency recurring invoices (EUR as well as USD) | **Non-goal — launch** | #02 (non-goal), #03 (sales committed at launch), #13 (item 9), #04 (Kwame: ~2w), #06 (2w) |

## Launch scope agreed in the current spec (PRD v2)
**R1, R3, R4, R5, R6 (all Must) + R7 (Should).** Non-goals: autopay, multi-currency, automatic reminders.

## Requirements with thin or contested evidence
- **R7 (custom recurrence rules):** no customer asked for it in the inputs. The one interview (#08) says "Everyone is billed on the first. Four or five clients are quarterly. That's it." Design (#12) couldn't agree a usable builder. Kwame (#04) questions whether anyone needs it. It is the only launch item with evidence *against* it, and at 2 weeks it is the largest optional cost. Flagged, not cut — your call (see conflicts C6).
