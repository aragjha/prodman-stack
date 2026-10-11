DRAFT, not reviewed by a person

# 06 · Handback (draft)

```text
RESULT   15 documents reconciled: current scope is PRD v2 (R1,R3,R4,R5,R6,R7); 5 live
         contradictions found, 4 already resolved by newer documents; build the series
         engine (R1) first; the strongest-evidenced customer pain (payment reminders) is
         parked, which is the main thing for the CEO to decide.
         Files: outputs/2026-10-11-recurring-invoices/ (01-inventory, 02-requirements-merged,
         03-conflicts, 04-themes, 05-build-first).
ROUTE    A01 (document chaos to product clarity), because there are 15 documents from
         different authors/dates that must be reconciled before a plan can be ranked.
         Skill run: pm. No outside skills, no fallbacks, no connectors.
STEPS    1 Inventory, superseded marked — 01-inventory.md
         2 Extract requirements/claims with sources — 02-requirements-merged.md
         3 Merge duplicates, keeping sources — 02-requirements-merged.md
         4 Contradictions side by side with owners — 03-conflicts.md
         5 Requirements with no evidence marked — 03-conflicts.md (C5, R7) + 04-themes.md
         6 Themes in 3+ documents — 04-themes.md
         7 Rank what to build first with confidence — 05-build-first.md
         8 Check + needs-human list — 07-check.md + this handback
CHECKS   see 07-check.md (independent pass)

NEEDS YOUR JUDGMENT
1. Launch date (C1). CEO told the board 31 October (10, 9 Sep); the newest estimate and
   roadmap say 30 November (06, 12 Sep; 01, 16 Sep) on a 10-week build from 21 Sep.
   ~4-week gap. Decide: move the date, or cut scope. Owner: Daniel + eng.
2. Reminders priority + the number behind it (C2). CEO: "Only 18% of our invoices are paid
   late" → "nice to have" (10). Support dashboard: "43% of invoices… paid after their due
   date" (05). Reminders are the strongest demand in the set (6 sources, T1), the top churn
   reason (04), and a competitive gap (11). Reconcile the number, then decide if reminders
   stay parked. Owner: leadership + finance.
3. EUR multi-currency commitment (C3). Sales promised a 40-seat prospect EUR "at launch"
   in writing (03); PRD v2 makes it a non-goal. Decide before the proposal is sent (close
   target end of Sept). Owner: you + sales/leadership.
4. Cut R7? (C5). Custom recurrence rules: origin unknown (Maya, 04), one customer doesn't
   need it (08), tested badly (12), costs 2 weeks (06). Cleanest scope cut toward 31 Oct.
   Owner: you.
5. Preview-email timing (C4). PRD v2 says 24 hours (02); design review says 3 days (12).
   Confirm which the team builds. Owner: you.

NEXT ACTIONS
1. Before the CEO meeting, put C1 (date) and C2 (reminders + the 18%/43% number) on one
   page — these two decide the Q4 story. Owner: you.
2. Get the 43%-vs-18% figure settled with finance/support so the meeting runs on one
   number. Owner: you → finance.
3. Hold the prospect proposal (C3) until the EUR commitment is confirmed or corrected.
   Owner: you → sales.

ASSUMPTIONS
- "Current" = the newest document on each topic, except where a doc explicitly supersedes
  another (02 supersedes 09; 15 replaces 07).
- Effort weeks are Kwame's (06), carried as given; not re-estimated.
- No context/PRODUCT.md, DECISIONS.md or CORRECTIONS.md exist (templates only), so product
  metrics and prior decisions come only from these 15 files.

CONFIDENCE  Medium. The documents are internally rich and the conflicts are clear, but the
            whole set is one PM's folder: only one customer interview (08), one support
            period (05), and two of the key numbers (launch date, % paid late) openly
            disagree between documents.
```
