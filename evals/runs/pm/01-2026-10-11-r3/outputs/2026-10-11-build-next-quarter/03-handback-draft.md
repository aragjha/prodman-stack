DRAFT, not reviewed by a person

# Decision brief — what to build next quarter

*Evidence is six SYNTHETIC interview notes (written for this test), n = 6 of ~300 firms (how the
firms were chosen is not recorded). Quotes verbatim from `inputs/interview-notes.md`.*

**Decision.** Pick the one thing to build next quarter.

**Recommendation.** Build **automatic payment reminders.** It is the only theme that clears the
three-independent-sources bar, and it serves retention and seat growth better than any alternative
in the notes.

**The three strongest pieces of evidence**
1. **Named explicitly by 3 of 6 firms** — Firm A asked *twice* "whether reminders could be
   automatic"; Firm E: "Automatic reminders would save my junior a day a month"; Firm F "uses a
   separate tool just to send payment reminders and pays for it. Would drop it if we had reminders
   built in." — **confidence MEDIUM** (real pattern in a small, self-selected sample; no usage data).
2. **The underlying pain — late payment / chasing by hand — touches 5 of 6 firms** (A, B, C, E, F);
   only Firm D (price) does not. Firm B lost two September payments "because they lost the invoice
   email"; Firm C spends "Friday afternoons copying payment status into a spreadsheet so I know who
   to chase." — **confidence MEDIUM.**
3. **It defends revenue two ways** — Firm F would drop a paid rival tool (a reason to stay), and
   Firm C "would pay more for that to go away." — **confidence MEDIUM.**

**How sure can you be?** Medium. The direction is well-supported for the firms you talked to:
reminders is the one idea three independent firms raised, and the pain spans five of six.
What keeps it from high: six interviews are not the ~300-firm base, and you have no
usage, revenue or churn data to confirm it. Treat "3 of 6" as a pattern in this sample, not a
measured share.

**What would reverse the call**
- Your watched metric is really **logo churn on price**, not retention/expansion. Firm D — your
  smallest account (2 seats) — is the only firm actively considering leaving, and reminders won't
  fix price. If the base is churning on price, a pricing/packaging move protects more revenue.
- When you check the base, firms say the real job is *knowing* payment status, not *sending*
  reminders — then lead with a payment-status view (Firm C) and add reminders on top.
- Reminders turn out expensive to build well (deliverability, scheduling, opt-outs) relative to the
  quarter — get an engineering estimate before committing; effort is currently unknown.

**Risks**
- Vocal-minority risk: 3 asks out of 6 interviews may not represent 300 firms.
- Build-vs-consolidate: Firm F already solves this with an external tool, so part of the value is
  consolidation, not an unmet need — may lower urgency for some firms.
- No baseline for the success metric (see next step).

**Success measure (propose, don't assume)**
- Primary: share of invoices paid on/before due date, or days-sales-outstanding, before vs after.
  **Baseline: unknown** — cheapest way to get it is to pull current on-time-payment rate from your
  own invoice data before building.
- Guardrail: logo churn and support load.
- Leading signal this quarter: reminder adoption (firms turning it on) and Firm F dropping its
  external tool.

**Next step, owner, date.** Before planning (~2026-10-25): (you) pull on-time-payment rate and
price-related churn reasons from existing data to confirm the metric and the counter-case; (you +
eng lead) get a rough effort estimate for reminders. Then make the call at planning.
