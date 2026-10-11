# Run pm-golden-04

| Field | Value |
|---|---|
| Wall clock | 185 s |
| Turns | 8 |
| Tokens (all, incl. cache) | 367,762 |
| Cost reported by the CLI | 1.055439 |
| Error | False |

## Final message, unedited

Done. Here's the handback.

```text
RESULT   Cut SAML SSO from the pilot; ship audit log + admin roles on Google login, dashboard as
         stretch — the only scope that fits 2 engineers by 15 Nov.
         · outputs/2026-10-11-A01/03-launch-plan.md
ROUTE    A01 (Document chaos to product clarity) · skill: pm · no fallbacks · C02 not chained
         (A01's ranking step already delivers the cut list)
```

**The core finding:** Full scope needs **40 engineer-days**; you have **38** (2 engineers × 19 working days, Tue 20 Oct → Fri 13 Nov — 15 Nov is a Sunday) — and that's *before* any QA or integration time. So the CEO's "don't slip the date" is only reachable by cutting.

**What to cut:** **SAML SSO (3 weeks / 15 engineer-days).** It's the biggest item, and it's the one thing the pilot customer explicitly said they don't need — their IT lead said *"Google login is fine for the pilot"* and SAML *"can wait until we roll out to the whole company next year."* Cutting it alone turns an impossible plan into a comfortable one.

**What ships:** Audit log (customer's #1, compliance review in December) + admin roles. That's 3 engineer-weeks against 7.6 available — large buffer to harden the audit log before December. The usage dashboard (nice-to-have) fits the math but is the natural drop if anything slips.

| Check | Result |
|---|---|
| Decision stated first | pass |
| Route named (A01) | pass |
| Prerequisites surfaced (Google-login dependency) | pass |
| Steps saved under outputs/ | pass (4 files) |
| Conflicts shown side by side | pass |
| Nothing invented (quotes exact; math labelled inference) | pass |

**NEEDS YOUR JUDGMENT**
1. **Confirm the SSO cut** — it reverses a written PRD must-have. Evidence favours cutting, but it's your call with the product owner.
2. **Confirm Google login already exists** and needs zero build. The entire plan rests on this; if it must be built, the math breaks and we re-plan.
3. **Dashboard in or out?** It fits as a stretch item but is the first thing to drop if anything slips.

**NEXT ACTIONS**
- You: confirm 1–3 above, especially the Google-login status (blocks everything).
- Eng: Audit log first (Eng A), admin roles + verify Google login (Eng B); reserve 9–13 Nov for QA and a dry run.

**ASSUMPTIONS**
- Google login already works for the pilot tenant (no engineering).
- Engineering estimates exclude QA/integration/review (raw feature estimates), so buffer matters.
- Both engineers available full-time, no PTO, across the whole window.

**CONFIDENCE:** Medium — the quotes and capacity math are solid, but the plan's feasibility hinges on one unconfirmed fact (whether Google login already exists).

Everything is a local DRAFT; nothing was sent, posted, or shared. Note the inputs are synthetic, as marked on every page.
