# 01 · Diagnosis (E01 steps 2–4)

> Data is SYNTHETIC (ProdMan.AI demo). "Activation rate" = activated firms ÷ signups that week —
> the share of new firms that send their first invoice within 7 days of signing up.

## Step 2 — Definitions first: did any metric change meaning in the period?

**Yes — one, and it is the whole seat story.** From `events-definitions.md` change log:

> "2 March 2026 · Churned firms · Firms that cancel during the free trial are no longer counted as churned" — before the period, ignore.
>
> "24 August 2026 · Seats added · Now counts seats added in firms on a free trial as well as in paying firms. Before this, it counted paying firms only. Applies from the week of 24 August. The event change shipped with release 4.1"

So **"Seats added" means two different things before and after the week of 2026-08-24.** Any
before/after comparison of that column is comparing two definitions, not two periods.

Felix's own both-ways recount for the week of 24 August (quoted from `events-definitions.md`):

> "61 seats added under the new definition, of which 29 were in paying firms and 32 in firms on a free trial."

No definition change touches Signups, Activated firms, Invoices sent, or Paid within 30 days in the
period. Those are comparable throughout.

## Step 3 — When did the real movement start, and is it seasonal?

| Metric | June → mid-July | From week of 2026-07-27 | Read |
|---|---|---|---|
| Signups | 53–64/wk | 61–66/wk | Healthy, slightly up. No problem. |
| **Activation rate** | **~62%** (61.1–63.6%) | **~41%** (39.3–42.4%) | **This is the real drop.** |
| Invoices sent | ~7,500–7,810 | ~7,845–8,042 | Stable / rising. |
| Paid within 30 days | ~4,300–4,600 | ~4,470–4,602 | Stable. |
| Seats added (as reported) | ~25–29 | 26 → **61** at 2026-08-24 | Jump is a definition change (see step 2). |

**The one thing that actually moved on a like-for-like basis: activation.** It fell from ~62% to
~41% — about a 21-point drop — and the break is sharp between the week of **2026-07-20** (62.5%) and
the week of **2026-07-27** (41.9%). It has stayed at ~41% every week since (6 straight weeks).

Seasonal/one-off ruled out:
- The week of 2026-06-29 (41 signups, 25 activated) is a volume dip, not a rate dip — activation
  rate that week was 61.0%, in line with its neighbours. It matches the release log's code freeze
  for the public holiday on Friday 2026-07-03. Not the drop we care about.
- The activation drop is a **rate** change that persists for 6 weeks across varying signup volumes —
  not seasonal noise.

Signups are fine and existing firms keep sending invoices (invoices-sent stable). The damage is
narrow: **new firms are no longer sending their first invoice inside the 7-day window.**

## Step 4 — Line the movement up against releases

From `release-log.md` (releases ship Tuesdays):

| Date | Release | Fits the activation break? |
|---|---|---|
| Tue 2026-07-14 | 3.9 New signup page: 5 fields instead of 9 | Activation was still ~62% for two weeks after (07-13, 07-20). A shorter signup form did **not** hurt activation. |
| **Tue 2026-07-28** | **4.0 Invoice template editor rebuilt (drag-and-drop); existing templates migrated; legacy default template retired** | **Exact fit.** Activation breaks the very next signup week (07-27 onward). Activation = sending the *first invoice*, which is exactly what the rebuilt editor gates. |
| Tue 2026-08-04 | 4.0.1 Fix: PDF margins in new editor | Follow-on fix to 4.0 — consistent with 4.0 having first-use problems. |
| Tue 2026-08-25 | 4.1 Bulk invite (+ the seat definition change shipped here) | After the activation break; explains the seat *number*, not activation. |

### Candidate causes, ranked

1. **The 4.0 invoice template editor rebuild broke first-invoice completion for new firms.**
   Confidence: **MEDIUM-HIGH.** Timing is tight to the week; the mechanism is direct (activation is
   literally "sent first invoice"); existing firms (already past onboarding) are unaffected, which is
   why invoices-sent stays flat while *new-firm* activation halves; and a margin-fix (4.0.1) followed.
   Not yet proof — correlation with a release is a lead, not causation (per E01 limits).
2. **The 3.9 signup-page change.** Confidence: **LOW / effectively ruled out** — activation held at
   ~62% for two weeks after it shipped.
3. **Unmeasured external/seasonal factor.** Confidence: **LOW** — a 21-point rate break landing
   exactly on a release week, persisting 6 weeks, is not a smooth seasonal curve.

## The bulk-invite / seat question (the straight answer leadership will ask)

**Is bulk invite driving seat growth? On the evidence: no — not that we can show.**

- The headline jump (26 → 61 seats, week of 2026-08-24) is a **measurement change**, not growth.
  The "Seats added" metric started counting free-trial firms that same week.
- On a **like-for-like (paying-firms-only) basis**, Felix's recount shows **29** paying-firm seats
  that week vs a ~27/week baseline over Jul 06–Aug 17 — essentially **flat**.
- Worse, the two changes are **confounded**: the seat-definition change *shipped inside release 4.1*,
  the same release as bulk invite, in the same week. Even the 32 free-trial seats can't be attributed
  to bulk invite — we have no breakdown of bulk-invited vs manually-added seats.

So the honest line for leadership: **"The seat jump is a reporting change, not new seats. On a
consistent definition seats are flat, and we have no instrumentation yet to credit bulk invite with
any of it."**
