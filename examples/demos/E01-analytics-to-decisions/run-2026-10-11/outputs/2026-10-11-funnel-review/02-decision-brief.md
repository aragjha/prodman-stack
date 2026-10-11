# Decision brief — Funnel review for Tuesday 2026-10-13 leadership review · DRAFT

> Data is SYNTHETIC (ProdMan.AI demo). Period: 2026-06-01 to 2026-09-14. Source files in
> `examples/demos/E01-analytics-to-decisions/input/`. Full working in `01-diagnosis.md`.

**Decision this serves:** What to do about the funnel before Tuesday, and whether to keep crediting
bulk invite with seat growth.

## The call
**One thing broke, and it isn't the one leadership is about to celebrate.**
New-firm **activation halved** — from ~62% to ~41% — the week release **4.0 (invoice template editor
rebuild)** shipped, and it has stayed there for 6 weeks. Meanwhile the **seat "growth" is not real
growth**: it's a metric-definition change that landed the same week as bulk invite. Recommend:
**treat the 4.0 editor as the lead cause and run the cheap test below; do not report bulk invite as
a seat driver.**

## The three strongest pieces of evidence
1. **Activation broke on the release week and stuck.** ~62% through the week of 2026-07-20 → 41.9%
   the week of 2026-07-27 (release 4.0 shipped Tue 2026-07-28), and ~41% every week since.
   **Confidence: HIGH** (numbers quoted directly from `metrics-weekly.md`).
2. **Only new firms are hit.** Signups (61–66/wk) and invoices-sent (~7,845–8,042) stay healthy;
   activation is first-invoice-within-7-days, which the rebuilt editor directly gates. The signup-page
   change (3.9) is ruled out — activation held for two weeks after it. **Confidence: MEDIUM-HIGH.**
3. **The seat jump is a definition change, not seats.** "Seats added" started counting free-trial
   firms the week of 2026-08-24; Felix's both-ways recount: 61 = 29 paying + 32 free trial. Paying-only
   seats (29) vs the ~27/wk baseline = flat. **Confidence: HIGH** (quoted from `events-definitions.md`).

## What would reverse the call
- If an event-level first-invoice funnel for post-2026-07-28 signups shows **no** new drop-off inside
  the rebuilt editor → the 4.0 editor is **not** the cause; look upstream (e.g. the 3.9 signup form
  changing who signs up) or at an unmeasured external factor.
- If a bulk-invited-vs-manual seat breakdown shows bulk invite **adding paying seats above the ~27/wk
  baseline** → bulk invite *is* contributing and the "flat" read is wrong.

## Risks
- Correlation with a release is a lead, not proof — acting before the test could fix the wrong thing.
- Activation counts first invoice *within 7 days*; a slower-but-not-lost cohort would understate true
  activation. The test must separate "lost" from "delayed."
- Small weekly churn/seat counts; don't over-read single weeks.

## The cheapest test (confirm or kill the lead cause) — step 5
**Primary test — first-invoice funnel, before vs after 4.0.** Using existing `invoice_sent` + editor
events (no new build), chart the first-invoice funnel for new firms: *editor opened → draft saved →
first invoice sent*, for cohorts signed up **before** and **after 2026-07-28**. If the drop-off
concentrates at a specific new step in the rebuilt editor, cause confirmed.
- **Primary metric:** 7-day activation rate (first invoice sent within 7 days of signup).
- **Guardrail:** invoices-sent by existing firms (must not fall — don't "fix" onboarding by
  destabilising the editor for everyone).
- **Stopping rule:** read after 2 full signup cohorts (~2 weeks) have 7 days of maturity; if activation
  for the fixed/holdback cohort is not ≥50% (halfway back toward the 62% baseline), stop and escalate.
- **Cost:** analysis-only on existing events; ~1 analyst-day. No code if we only instrument-and-read.

**Secondary (answers the seat question) — split the seat metric.** Report "Seats added" on the
**paying-only** basis alongside the new all-firms basis, and tag each seat by **bulk-invite vs manual**
flow going forward. This is the only way to credit (or clear) bulk invite.
- **Primary metric:** paying-firm seats added per week (consistent definition).
- **Guardrail:** free-trial-to-paid conversion of bulk-invited seats (trial seats aren't revenue yet).

## Needs your judgment
1. **How to present seats to leadership** — lead with the honest "reporting change, flat on a
   consistent basis" line, or show both bases side by side? Recommend the latter.
2. **Whether to prioritise the 4.0 editor fix now** vs wait for the test — a ~21-pt activation loss for
   6 weeks is expensive; you may choose to start a fix in parallel with the confirming analysis.
3. **Confirm the mechanism assumption** — that activation is gated by the invoice editor (not, say, a
   billing or email-delivery step). One sentence from Felix/Kwame settles it.

## Next step · owner · date
Run the first-invoice funnel analysis (owner: PM + analyst, with Felix on events) **before Tue
2026-10-13**; bring both the activation finding and the two-basis seat view to the review.

---
Status: **DRAFT** — nothing sent, posted, or entered in any tracker. Numbers verified in `03-check.md`.
