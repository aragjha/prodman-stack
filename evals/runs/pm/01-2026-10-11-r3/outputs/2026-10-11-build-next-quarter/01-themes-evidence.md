DRAFT, not reviewed by a person

# 01 · Themes and evidence (C02 steps 1–2)

All evidence is from `inputs/interview-notes.md` (SYNTHETIC, written for this test). n = 6
interviews out of ~300 firms, self-selected, not a representative sample.

## Candidate builds, with every firm that touches them

### Candidate 1 — Automatic payment reminders
**Explicitly asked for by 3 of 6 firms (A, E, F):**
- Firm A (4 seats): "We chase clients for payment by email, one by one." + "Asked twice whether reminders could be automatic."
- Firm E (9 seats): "Automatic reminders would save my junior a day a month."
- Firm F (15 seats): "Uses a separate tool just to send payment reminders and pays for it. Would drop it if we had reminders built in."

**Pain it would reduce, named by 2 more firms (B, C) — supporting, not a direct ask:**
- Firm B (11 seats): "two clients paid late in September 'because they lost the invoice email'." (A reminder re-surfaces the invoice; B's own ask was dark mode.)
- Firm C (6 seats): "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." (Chasing is the shared pain; C's literal ask is status tracking, see Candidate 2.)

So: the **late-payment / manual-chasing problem touches 5 of 6 firms (A, B, C, E, F)**; only Firm D
(price) does not. **Automatic reminders is named explicitly by 3 of 6.** A theme needs three
independent data points (PM.md §3) — this clears it; the two supporting firms strengthen it.

Seat weight of the 3 explicit firms: A(4) + E(9) + F(15) = 28 seats.

### Candidate 2 — Payment-status dashboard / reconciliation of who-owes-what
- Firm C (6 seats): "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." + "Would pay more for that to go away." (HIGH willingness to pay signal, but **1 firm** = weak signal.)
- Partially overlaps the chasing pain in A and C. Could be built as part of, or instead of, reminders.

### Candidate 3 — Bank reconciliation
- Firm E (9 seats): "Also wants bank reconciliation, called it 'nice to have'." (**1 firm, self-labelled nice-to-have** = weak signal.)

### Candidate 4 — Dark mode
- Firm B (11 seats): "Wants a dark mode." (**1 firm**, from an otherwise-happy customer = weak signal.)

### Candidate 5 — Lower price per seat (pricing decision, not a build)
- Firm D (2 seats): "Considering leaving for a cheaper tool. Main complaint: price per seat." (**1 firm**, smallest account at 2 seats. This is a pricing/packaging decision, not an engineering build; flagged separately.)

## Confidence note
Quote accuracy is HIGH (lines are the user's own notes, quoted verbatim). But **signal strength is
limited**: 6 self-selected interviews out of ~300 firms is not representative, and there is no
usage, revenue or churn data to confirm any theme. So "3 of 6 asked for reminders" is a real
pattern in this sample, not a measured share of the base.

## Argue-against-yourself (PM.md §3)
What would make reminders the *wrong* pick:
- If the firms that actually churn leave over **price** (Firm D's complaint), reminders won't save
  them — and D is the only firm actively considering leaving.
- If most of the ~300 firms already have a workaround they're content with, the 3 asks may be a
  vocal minority.
- Firm F already pays for an external reminder tool — proof the job can be done today, so building
  it is consolidation value, not an unmet need. That could lower urgency.
These are carried into the brief's "what would reverse the call" and the judgment list.
