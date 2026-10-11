# 02 · Requirements, conflicts, and capacity math

> Run A01 · 2026-10-11 · **SYNTHETIC inputs — labelled synthetic on every page.**

## Requirements extracted (one line each, with source and confidence)

| Item | Status in PRD | Source | Confidence |
|---|---|---|---|
| SSO with SAML (for the pilot customer) | Must have | Doc 1, PRD v2 | HIGH (quoted) |
| Audit log | Must have | Doc 1, PRD v2 | HIGH (quoted) |
| Admin roles | Must have | Doc 1, PRD v2 | HIGH (quoted) |
| Usage dashboard | Nice to have | Doc 1, PRD v2 | HIGH (quoted) |
| Target launch date | 15 November | Doc 1 + Doc 4 | HIGH (quoted, both agree) |

Quoted — PRD (Doc 1): *"Must have: SSO with SAML for the pilot customer, audit log, admin roles. Nice
to have: usage dashboard. Target launch: 15 November."*

## Conflicts (shown side by side, not silently resolved)

### Conflict 1 — Is SAML SSO needed for the pilot? (the decision hinges here)

| Source | What it says | Confidence |
|---|---|---|
| Doc 1 (Product, PRD v2) | SAML SSO is a **must have** "for the pilot customer" | HIGH (quoted) |
| Doc 2 (Sales, customer's own IT lead) | "Google login is fine for the pilot"; SAML SSO "can wait until we roll out to the whole company next year" | HIGH (quoted) |

The two newest-looking sources disagree. The tie-breaker is **whose voice it is**: Doc 2 quotes the
*pilot customer's own IT lead* — the person who would actually use SAML SSO — saying they don't need it
for the pilot. The PRD states an internal assumption about the customer; the sales note is the customer
correcting it. **Owner of this call: you (PM) / product owner.** This is not resolved automatically — but
the evidence points one way.

### Conflict 2 — What matters most to the customer? (no conflict; reinforces a priority)

| Source | What it says | Confidence |
|---|---|---|
| Doc 2 (Sales) | "They care most about the audit log, because their compliance review starts in December" | HIGH (quoted) |
| Doc 1 (Product) | Audit log listed as a must have | HIGH (quoted) |

These agree. The audit log is both a PRD must-have and the customer's #1, with a real deadline behind
it (compliance review in December). It should be the thing most protected from any cut, and ideally
finished with time to spare before December.

### The CEO message is a constraint, not a scope input
Doc 4: *"We launch the pilot on 15 November no matter what. Do not slip the date."* This fixes the date;
it says nothing about scope. With the date fixed and capacity short (below), scope is the only lever —
so something must be cut.

## Capacity math (INFERENCE / calculation — not from any document)

**Window:** engineers start 20 October (Doc 3); launch 15 November (Docs 1 & 4).

- 15 November 2026 falls on a **Sunday** → last working day before launch is **Friday 13 November**.
- Working days per engineer, Tue 20 Oct → Fri 13 Nov = **19 days**.
- Two engineers (Doc 3) → **38 engineer-days** of capacity (≈ 7.6 engineer-weeks).

**Effort required** (Doc 3, converted at 5 days/week):

| Item | Estimate | Engineer-days |
|---|---|---|
| SSO with SAML | 3 weeks | 15 |
| Audit log | 2 weeks | 10 |
| Admin roles | 1 week | 5 |
| Usage dashboard | 2 weeks | 10 |
| **Total (full scope)** | **8 weeks** | **40** |

**Full scope needs 40 engineer-days; only 38 are available — before any time for QA, code review,
integration, or the Sunday launch.** Full scope does not fit. The CEO's "do not slip" is therefore
only achievable by cutting.

### Scenarios

| Plan | Scope | Eng-days needed | vs 38 available | Verdict |
|---|---|---|---|---|
| A — ship everything | SSO + audit + roles + dashboard | 40 | over by 2, 0 buffer | ✗ will slip |
| B — cut SSO | audit + roles + dashboard | 25 | 66% used, 13-day buffer | ✓ fits |
| C — cut SSO + dashboard | audit + roles | 15 | 39% used, large buffer | ✓✓ safest |

Cutting **SAML SSO removes 15 engineer-days** — the single biggest item — and by itself turns an
impossible plan into a comfortable one. It is also the one item the customer explicitly said they do
not need for the pilot (Conflict 1).

**Key assumption behind all three plans:** "Google login is fine for the pilot" (Doc 2) means Google
login **already works** and needs zero engineering. If Google login must still be built, that is
unestimated work and the math changes — flagged for you to confirm.
