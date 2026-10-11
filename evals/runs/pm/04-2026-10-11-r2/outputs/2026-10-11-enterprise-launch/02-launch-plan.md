# 02 · Launch plan and what to cut (C02) — DRAFT

**Decision it serves:** what to build and what to cut so the pilot launches 15 Nov 2026 without slipping.
**Metric the date serves:** the pilot customer's compliance review starts in December (Doc 2) — the audit log must be live and populating before then. Launching on time with a working audit log is what the date is *for*.

Because the SSO conflict decides the plan, here are both plans side by side. Capacity ≈ 6–7.6 engineer-weeks (file 01).

## Plan A — honour the PRD (SAML SSO is a must-have)
Must-haves: SSO SAML (3) + audit log (2) + admin roles (1) = **6 engineer-weeks**. Usage dashboard (2) is cut.

| Build | Weeks | Who |
|---|---|---|
| SSO with SAML | 3 | Eng 1 |
| Audit log | 2 | Eng 2 |
| Admin roles | 1 | Eng 2 (after audit log) |
| ~~Usage dashboard~~ | cut | — |

- **Cut:** usage dashboard (the only nice-to-have).
- **Fit:** 6 weeks of must-haves into ~6–7.6 engineer-weeks gross. It *fits on paper* but leaves little or no buffer for QA, integration, and launch prep before Fri 13 Nov.
- **Risk:** SSO SAML (3 weeks) is the longest and riskiest item and sits on the critical path. If it slips, the launch slips — which violates the CEO's hard constraint. You would be spending your only slack on a feature the customer said they do not need for the pilot.

## Plan B — honour the sales notes (SAML can wait) · RECOMMENDED
Cut SAML SSO; use Google login for the pilot (the customer's IT lead said this "is fine"). Must-haves become audit log (2) + admin roles (1) = **3 engineer-weeks**. Usage dashboard (2) now fits too.

| Build | Weeks | Who |
|---|---|---|
| Audit log | 2 | Eng 1 |
| Admin roles | 1 | Eng 2 |
| Usage dashboard (optional, if you want it) | 2 | Eng 2 (after admin roles), or Eng 1 |
| ~~SSO with SAML~~ | deferred to next year's company-wide rollout | — |

- **Cut / defer:** SSO with SAML → next year, when the customer rolls out company-wide (their words). Pilot uses Google login.
- **Fit:** 3 engineer-weeks of must-haves into ~6–7.6 engineer-weeks → comfortable. Audit log gets built early and has weeks to be tested before the December compliance review. The usage dashboard can be added and still leave buffer.
- **Risk:** you ship the pilot without SAML. Low risk for the pilot itself (customer approved Google login); the cost is only if the "next year" company-wide rollout arrives sooner than expected, at which point SAML becomes the first post-pilot item.

## Recommendation
**Take Plan B. Cut SAML SSO from the launch; build audit log first, then admin roles, and add the usage dashboard only if you want it.**

Three strongest reasons, with confidence:
1. The customer's own IT lead said Google login "is fine for the pilot" and SAML "can wait until we roll out to the whole company next year" (Doc 2). **HIGH** — quoted from the sales notes.
2. The customer "care most about the audit log, because their compliance review starts in December" (Doc 2). Audit log is the time-critical feature; Plan B gives it the most runway. **HIGH** — quoted.
3. The CEO's hard constraint is the *date*, not SAML (Doc 4 names no feature). Cutting the 3-week item is the cleanest way to guarantee the date with buffer — which is exactly what the CEO asked for. **HIGH** — quoted; the feature/ date distinction is an inference from the CEO text, labelled as such.

**What would reverse this call:** if the PRD's "must have" reflects a contractual or security commitment to the pilot customer that the sales notes missed, or if the company-wide rollout (and therefore SAML) is actually happening during the pilot window. Either makes SAML a must-have and pushes you to Plan A (and a very tight schedule).

## Sequencing note (applies to both plans)
Build the audit log first regardless of plan: it is the customer's top priority and the December compliance review is the real deadline behind the launch date. Admin roles (1 week) is small and low-risk. In Plan A, SSO SAML should start day one on its own engineer because it is the critical-path item.
