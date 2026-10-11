DRAFT, not reviewed by a person

# 02 · Enterprise pilot launch plan — and what to cut

**Decision this serves:** what to ship on 2026-11-15 and what to cut, so the date does not slip.
All inputs are SYNTHETIC.

## The bottom line

- The full scope (8 engineer-weeks) does not fit the runway (~7.4 engineer-weeks, 2 engineers, 20 Oct → 15 Nov). Something is cut no matter what.
- **Cut now, no debate: the usage dashboard** (nice-to-have in the PRD, 2 weeks, no customer demand recorded). This alone is not enough to create safety.
- **The real lever is SSO with SAML (3 weeks — the biggest item).** The PRD calls it a must-have; the pilot customer says it can wait. How you resolve that conflict decides whether the date has 3 business days of buffer or 12 calendar days.

Because the PRD and the customer disagree, the plan is shown **both ways**. The recommendation follows.

---

## Plan A — Keep SAML (follow the PRD literally)

Ship all three PRD must-haves; cut only the usage dashboard.

| Track | Engineer | Work | Weeks | Finishes |
|---|---|---|---|---|
| 1 | Eng A | SSO SAML | 3 | ~Tue 2026-11-10 |
| 2 | Eng B | Audit log → Admin roles | 2 + 1 | ~Tue 2026-11-10 |

- **Cut:** usage dashboard.
- **Buffer to 15 Nov:** ~5 calendar days (≈3 business days).
- **Risk: HIGH.** Zero slack in the estimates and the longest, least-certain item (SAML, 3 wks) sits on the critical path. Any slip on SAML slips the launch — directly against the CEO's "Do not slip the date." (Doc 4). It also builds SAML the customer said they don't need for the pilot (Doc 2).

## Plan B — Defer SAML (follow the customer) · RECOMMENDED

Ship Google login (customer says it is fine for the pilot) + audit log + admin roles. Defer SAML to next year's company-wide rollout, when the customer actually needs it.

| Track | Engineer | Work | Weeks | Finishes |
|---|---|---|---|---|
| 1 | Eng A | Audit log | 2 | ~Tue 2026-11-03 |
| 2 | Eng B | Admin roles | 1 | ~Tue 2026-10-27 |

- **Cut from the 15 Nov launch:** SSO SAML (deferred, not dropped) **and** usage dashboard.
- **Buffer to 15 Nov:** ~12 calendar days on the critical path (audit log).
- **Risk: LOW.** The audit log — the customer's stated top priority for their December compliance review — lands with room to harden and test it. The CEO's date is protected with real slack. The freed capacity could optionally pull in the usage dashboard or start SAML early, but do not commit that until the must-haves are verified done.

---

## Side-by-side

| | Plan A (keep SAML) | Plan B (defer SAML) — recommended |
|---|---|---|
| Ships 15 Nov | SAML, audit log, admin roles | Google login, audit log, admin roles |
| Cut | Usage dashboard | SAML (deferred to next year), usage dashboard |
| Buffer | ~5 cal days (~3 biz days) | ~12 cal days |
| Matches customer's stated need | Partly (builds SAML they said can wait) | Yes (audit log first; Google login accepted) |
| Protects "do not slip" (CEO) | Weakly — no slack | Strongly — real slack |

## Why Plan B is recommended
1. The pilot customer's IT lead said Google login is fine for the pilot and SAML "can wait until we roll out to the whole company next year" (Doc 2). Deferring SAML removes the biggest, riskiest item without hurting the pilot.
2. It protects what the customer cares most about — the audit log for their December compliance review (Doc 2) — by giving it slack to be done well, not just done.
3. It is the surest way to honour the CEO's instruction to launch the pilot on 15 November and not slip the date (Doc 4): ~12 days of buffer vs ~3 business days.
4. SAML is not dropped — it is scheduled for when the customer said they need it (company-wide rollout next year).

## What this plan cannot settle
- The PRD calls SAML a must-have for the pilot; the customer (via sales) says it can wait. A person must reconcile that before 20 October. The recommendation is to defer, but the PRD owner / CEO must agree, because overriding a PRD must-have is hard to reverse.

## Success measures to attach (baselines unknown — propose cheapest way to get them)
- **Primary:** pilot customer accepts the audit log for their December compliance review (yes/no by December). Baseline: n/a (new). [metric proposed, not in source]
- **Guardrail:** no launch slip past 2026-11-15. [from Doc 4]
- **Leading:** both must-haves code-complete and tested by the track finish dates above.
Mark these as proposed; the source documents do not state success metrics.
