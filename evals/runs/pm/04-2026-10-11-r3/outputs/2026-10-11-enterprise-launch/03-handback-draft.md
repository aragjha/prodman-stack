DRAFT, not reviewed by a person

# Hand-back draft

RESULT  The full scope does not fit the runway, so something is cut regardless; cut the usage dashboard outright, and — recommended — defer SSO SAML (the customer says it can wait), shipping Google login + audit log + admin roles with ~12 days of buffer. Plan: outputs/2026-10-11-enterprise-launch/02-launch-plan.md

ROUTE  A01 (document chaos to product clarity), then C02 (evidence based prioritisation) — because the four documents conflict and must be reconciled before the cut can be ranked against the date. Skills run: pm only (both workflows are pm-only). No outside skills, no fallbacks used.

STEPS
- A01.1 inventory documents — done (01-inventory-conflicts.md, requirements table)
- A01.2 extract requirements — done (01, requirements table)
- A01.3 merge duplicates — done (01; none to merge, 4 distinct items)
- A01.4 contradictions side by side — done (01, conflict table: PRD vs sales on SAML/audit)
- A01.5 mark requirements with no evidence — done (01; usage dashboard has no recorded demand, noted in 02)
- A01.6 themes in 3+ documents — skipped (only 4 short docs, one per role; theme-counting not meaningful at this size)
- A01.7 rank what to build first — done (02, Plan A/B and cut list)
- A01.8 check + needs-human list — done (04-check.md; this hand-back)
- C02.1 restate goal/metric — done (00-frame.md; 02 success measures)
- C02.2 attach evidence + confidence — done (01, 02)
- C02.3 score on impact/confidence/effort — done (02 side-by-side; effort from Doc 3)
- C02.4 rank + closest calls + what flips them — done (02; the SAML conflict is the flip)
- C02.5 check ranking — done (04-check.md)

CHECKS  see 04-check.md — rows, corrected, removed below; checked by independent subagent pass.

NEEDS YOUR JUDGMENT
1. SAML conflict: PRD v2 lists SSO SAML as a pilot must-have; the pilot customer (sales notes) says Google login is fine for the pilot and SAML can wait until next year's company-wide rollout. Deferring it is the recommended cut but overrides a PRD must-have — your call, and ideally the CEO's, before 20 Oct.
2. Estimate parallelism: the plan assumes each estimate is one engineer's effort so two items run in parallel. Confirm with engineering; if an item needs both engineers, the math changes.
3. Launch date is a Sunday (2026-11-15). Confirm that is intended, or whether the real target is the Friday before (13 Nov) or Monday after.
4. If you keep SAML (Plan A), accept ~3 business days of buffer against a "do not slip" mandate, or ask engineering for a de-risked SAML estimate.

NEXT ACTIONS
1. Decide SAML in-or-deferred before 20 Oct — owner: you (with CEO/PRD owner).
2. Confirm the parallel-tracks assumption with engineering — owner: eng lead.
3. If Plan B, tell the pilot customer SAML lands with the company-wide rollout and audit log ships for their December review — owner: sales (draft only; do not send without approval).

ASSUMPTIONS
- Each eng estimate = one engineer's weeks (parallelisable across the two engineers).
- Estimates carry no buffer; taken at face value.
- No product context file exists (templates only), so product voice and prior decisions are unknown.
- Success metrics are proposed, not stated in any source.

CONFIDENCE  Medium — the recommendation rests on the sales notes reflecting the customer's real position; if that call was partial or outdated, the SAML cut is wrong.
