# Run pm-golden-04-r2

| Field | Value |
|---|---|
| Wall clock | 191 s |
| Turns | 13 |
| Tokens (all, incl. cache) | 488,764 |
| Cost reported by the CLI | 0.930269 |
| Error | False |

## Final message, unedited

All files written and checked. Here's the handback.

```
RESULT   Cut SAML SSO from the pilot (use Google login, which the customer approved); build audit log first, then admin roles, add the usage dashboard only if wanted — this hits 15 Nov with buffer. Plan: outputs/2026-10-11-enterprise-launch/02-launch-plan.md

ROUTE    A01 (document chaos to product clarity) → C02 (evidence-based prioritisation) · skill run: pm · no outside skills, no connectors · no fallbacks · steps skipped: none (A01 "themes across 3+ docs" not applicable — 4 docs, one launch)

CHECKS   21 claims checked, 0 removed, 0 fixed (all held) · outputs/2026-10-11-enterprise-launch/03-check.md
         Clarity | pass | "Take Plan B. Cut SAML SSO..."
         Visual | pass | side-by-side Plan A / Plan B tables, bold call
         Concise | pass | one-page plan
         Decision | pass | names the call + "What would reverse this call"
         Honesty | pass | SSO conflict shown both ways, confidence tags, inferences labelled
         Accuracy | pass | all quotes/numbers match inputs; sums recomputed (8, 6, 3 eng-weeks)
```

**The core finding:** You have **8 engineer-weeks of work** (SSO 3 + audit 2 + admin 1 + dashboard 2) and only **~6–7.6 engineer-weeks of capacity** (2 engineers, 20 Oct Tue → 15 Nov, 19 working days). So you must cut *something* regardless. The only scope conflict is PRD ("SSO SAML = must have") vs the customer's own IT lead ("Google login is fine for the pilot; SAML can wait until… next year"). The CEO fixed the **date**, not SAML.

**Cut SAML SSO.** It's the biggest item (3 weeks), it's on the critical path, and it's the one the customer explicitly said they don't need for the pilot. Dropping it turns a tight, risky schedule into a comfortable one and gives the **audit log** — the feature the customer cares most about, needed for their **December compliance review** — weeks of runway before launch.

NEEDS YOUR JUDGMENT
1. **The SSO conflict (resolve this first).** PRD says must-have; the customer's IT lead says can-wait. Confirm the PRD "must have" isn't a *contractual or security* commitment the sales notes missed. If it is, you're in Plan A and the schedule is very tight.
2. **Is the company-wide rollout really "next year"?** If it slips into the pilot window, SAML becomes a must-have again.
3. **15 Nov is a Sunday; engineers start Tue 20 Oct.** Confirm whether "launch" means a weekend go-live or the business day around it, and that 20 Oct is a real full start (not a part week).
4. **Usage dashboard:** optional in Plan B — decide whether you want it in the pilot or held back as buffer insurance.

NEXT ACTIONS
1. PM: get the SSO must-have-vs-can-wait call from sales + CEO by ~17 Oct (before engineers start). — owner: you
2. PM: once decided, lock scope and brief the two engineers to start on the audit log 20 Oct. — owner: you
3. Eng lead: confirm the 1-week QA/launch buffer before Fri 13 Nov is realistic for the chosen scope. — owner: engineering

ASSUMPTIONS
- The four documents are the complete and current picture (none dated; none marked superseding another).
- Estimates are serial per engineer and roughly parallelisable across two engineers; ~1 week held back for QA/integration/launch prep.
- No contractual SAML commitment beyond what the PRD states.

CONFIDENCE  Medium — the recommendation is well-evidenced, but it hinges on #1: whether the PRD's "must have" is a hard commitment the sales notes don't see. Nothing has been sent, posted, or committed; all outputs are local drafts in `outputs/2026-10-11-enterprise-launch/`.
