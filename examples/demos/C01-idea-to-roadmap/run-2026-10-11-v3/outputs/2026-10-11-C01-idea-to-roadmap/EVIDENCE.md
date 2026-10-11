DRAFT, not reviewed by a person

# EVIDENCE — Idea to roadmap research
Starting position written: 2026-10-11 (before any search).

**Decision:** Is payment reminders + a client payment portal the right Q1 2027 bet for Ledgerly, and
how should it be sequenced, given the goal of 300 net new seats in the quarter.

**Goal (from the PM, not the web):** "300 net new seats in the quarter" (Q1 2027). List price
"$25 per seat per month, billed annually." Base: 1,840 seats at end of Sep 2026.

**Belief (third person):**
- B1: The PM believes payment reminders + a client portal is a bet worth making because "Late payment
  is the complaint I hear most often from firms" and "A competitor shipped payment reminders this summer,
  and sales says it comes up in deals."
- B2: The PM (via leadership) believes this work can drive expansion revenue — firms adding seats.

**What would change their mind:**
- If reminders and pay-by-link portals are already a free, bundled commodity across the main
  competitors, the feature may be table stakes (stops losses) rather than a seat driver.
- If the money in this category is made on payment-processing fees (% per transaction) rather than per
  seat, the portal would not obviously move the seat metric.
- If there is no mechanism by which this work causes a firm to add seats, B2 fails.

## Sources
`S# | exact quote | URL | how checked`

S1 | "Xero invoice reminders are free, built into Xero and take about 10 minutes to set up." | https://trove.works/xero-invoice-reminders/ | read on the page

S2 | "You get up to five automatic emails per invoice, on one schedule that applies to every customer." | https://trove.works/xero-invoice-reminders/ | read on the page

S3 | "2.99%" (card) · "1%" (ACH bank payments) · "No monthly fees or minimums." | https://quickbooks.intuit.com/payments/invoicing/ | read on the page

S4 | Chaser Compact from $259 USD/month (4 users), Core $779 USD (unlimited users), Complete $1169 USD; tiered by annual revenue. | https://www.chaserhq.com/chaser-pricing | second hand (vendor pricing page via fetch tool; raw-HTML string match did not confirm the exact currency rendering)

S5 | BILL AR: Essentials $49, Team $65, Corporate $89 per user per month. | https://www.bill.com/product/pricing/ | second hand (vendor pricing page via fetch tool; raw-HTML string match did not confirm the exact rendering)

S6 | "Following up after payment lands can damage trust." · "Excellent customers should not receive aggressive cadences designed for chronic late payers." | https://www.chaserhq.com/blog/automated-payment-reminders | read on the page

S7 | "Every Friday I email the clients who haven't paid. If Ledgerly did that for me, I'd move our two new juniors onto Ledgerly instead of the spreadsheet." (office manager, 9 seat firm) | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

S8 | "My clients lose the invoice email and then ask me to resend it. I want one link where they can see everything they owe us and pay it." (partner, 4 seat firm) | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

S9 | "Reminders sound useful, but I'm nervous about a robot nagging my biggest clients. I'd need to control who gets chased and what it says." (firm admin, 15 seat firm) | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

S10 | "Seats: 1,760 at the end of June 2026 and 1,840 at the end of September 2026." | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

S11 | "Squad A has 5 engineers. About 30% of its time goes to bank feed maintenance, every quarter." · "Squad B has 4 engineers. It is finishing recurring invoices and is free from the first week of January." | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

S12 | "Card payments run through our existing payments partner. Fewer than 50 firms have turned card payments on." | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM

## Sources that weaken the belief, and where they land
- S1, S2 (reminders are free and built into a major competitor): weaken B1's "this is a wedge" framing →
  used in the report's call and in the "what changed" section. Reminders are table stakes; the differentiator
  is the per-customer control Xero lacks (S2) and that customer S9 asks for.
- S3 (pay-by-link monetised on transaction %, no per-seat charge): weakens B2 for the portal specifically →
  used in the call and the seat-mechanism discussion.
- S4, S5 (AR automation priced by revenue band or per user, not tied to the reminder feature driving new
  seats): context for pricing patterns → used in findings table.
- S6 (relationship-damage risk is real): supports the need for the control feature (S9) → used in the risks
  and in the reminders bet.
- None dropped.
