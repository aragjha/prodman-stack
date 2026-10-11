DRAFT, not reviewed by a person

# Decision brief — Funnel review, June–mid-September 2026
*For Tuesday 13 October 2026 leadership review. Source: `examples/demos/E01-analytics-to-decisions/input/` (labelled SYNTHETIC). Rates are derived; raw counts are quoted exactly.*

## Decision
Does the funnel need an intervention and where — and should we credit bulk invite for seat growth?

## Recommendation
**Fix activation; don't credit bulk invite for seats yet.** One thing genuinely broke in this period:
**activation fell by about a third, from ~62% to ~42%, starting the week of 27 July**, the week release 4.0
rebuilt the invoice editor and retired the default template. The seat "doubling" leadership will ask
about is mostly a **metric-definition change on 24 August**, not the bulk-invite release. Run a
free cohort check this week to confirm the activation cause, then test a one-click default template.

## The three strongest pieces of evidence
1. **Activation dropped ~20 points and stayed down.** ~62% (June–20 Jul) → ~42% (27 Jul–14 Sep),
   while signups held at 61–66/week — a conversion problem, not a traffic one. **HIGH** (arithmetic on the input table).
2. **The drop lines up with release 4.0, not the signup page.** The two signup cohorts after the new
   signup page (weeks of 13 Jul, 20 Jul) still activated at ~62% (61.9% and 62.5%); the collapse begins the week
   of 27 Jul, with 4.0 shipping Tuesday 28 Jul ("legacy default template is retired"). **MEDIUM**
   (timing + mechanism; a release correlation is a lead, not proof).
3. **Seat growth is mostly definitional.** Seats jumped from ~26 to ~60/week from 24 Aug — the exact
   week the metric started counting free-trial seats. Felix's dual count for 24 Aug: "61 seats added
   under the new definition, of which 29 were in paying firms and 32 in firms on a free trial." 29
   paying seats is inside the prior paying-seat range of 25–29 (17 in the one holiday week of 29 Jun).
   **HIGH** for that one week.

## The straight answer on bulk invite → seat growth
**Not proven, and most likely no — on the evidence we have.** Two things landed in the same week:
release 4.1 (bulk invite, Tuesday 25 Aug) and the seats definition change (applies from the week of
24 Aug). They are **fully confounded** — we cannot separate them from the weekly totals alone. The
one week we *can* decompose shows paying-firm seats flat at 29. So the headline jump is explained by
newly-counted free-trial seats, not by more paid seats. Honest line for the room: *"Seats look like
they doubled, but that's mostly a definition change; on the one week we can split, paid seats were
flat. We can't yet credit bulk invite — here's the one-week read that would."*

## What would reverse each call
- **Activation:** if the free cohort read shows the drop is spread across the whole journey (not at
  invoice creation), 4.0 is not the cause — look at signup quality or tracking instead.
- **Bulk invite:** if a paying-vs-trial split for the weeks of 31 Aug–14 Sep shows paying seats
  clearly above the ~25–29 non-holiday baseline, then bulk invite *is* adding paid seats and deserves credit.

## Risks
- Reading the seat number at face value in the room overstates growth and could misdirect investment.
- The activation cause is MEDIUM confidence; shipping a fix before the cohort read risks fixing the
  wrong step.
- Small denominators on churn (0–2/week) — don't over-read week-to-week churn moves.

## Next step, owner, date
Run the free pre/post-4.0 cohort read and pull the paying-vs-trial seat split for 31 Aug–14 Sep —
**owner: PM + Felix (events) — before Tuesday 13 Oct** so both answers are evidence-backed in the room.
