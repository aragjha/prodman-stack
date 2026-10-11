DRAFT, not reviewed by a person

# 01 · Definitions check (did any metric change meaning in the period?)

E01 step 2: check definitions before reading any movement as a trend.

The change log in `events-definitions.md` has two entries. One falls inside this period and it is
the single most important fact in the whole analysis:

- **Seats added — definition changed 24 August 2026.** "Now counts seats added in firms on a free
  trial as well as in paying firms. Before this, it counted paying firms only. Applies from the week
  of 24 August. The event change shipped with release 4.1." So the seats column means one thing
  through 17 August and a *different, broader* thing from the week of 24 August onward. The two
  halves are not comparable.
- **Felix's check run (quoted):** "Felix counted the week of 24 August both ways: 61 seats added
  under the new definition, of which 29 were in paying firms and 32 in firms on a free trial." This
  lets us decompose exactly one week back onto the old definition: **29 paying-firm seats.**
- Churned firms changed on 2 March 2026 (free-trial cancels no longer counted) — before this period,
  no effect here.
- **Activated firms, Signups, Invoices sent, Paid within 30 days: no definition change in the period.**
  Movements in these are real, not definitional.

**Consequence.** The seats number must be read in two segments. The activation drop must be read as real.

**Data is final, not truncated.** Activated firms is "counted against the signup week... final 7 days
after the week ends." The export was Monday 28 September 2026; the last week shown (14 Sep, ends
20 Sep) finalised 27 Sep. So every activation figure in the table is final, not still filling in.
