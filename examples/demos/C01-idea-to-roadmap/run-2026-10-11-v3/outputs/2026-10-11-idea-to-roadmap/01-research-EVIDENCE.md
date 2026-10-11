DRAFT, not reviewed by a person

# Research evidence — starting position

**Time started:** 2026-10-11 (session date).

**Decision.** Whether to build automatic payment reminders + a client payment portal in Q1 2027, and
if so how to sequence it, given that it must drive existing firms to add seats (300 net new seats).

**Goal (from the PM, not the web).** 300 net new seats in Q1 2027; price $25/seat/month billed annually.

**Belief, in the third person:**
- **B1 (demand):** The PM believes reminders + a payment portal is the right bet because late payment
  is the complaint firms raise most and a competitor shipped reminders this summer.
- **B2 (seat expansion):** Leadership believes this feature will drive existing firms to add seats.

**What would change their mind:**
- If competitors already bundle reminders and a payment portal cheaply or for free, the feature is
  table stakes and unlikely to be a reason to add seats (weakens B2).
- If shipped reminders see low adoption, or if auto-chasing clients creates churn/brand risk that
  firms fear (echoing customer quote 3), the demand is softer than believed (weakens B1).
- If the link between "firm gets this feature" and "firm adds seats" is weak (the buyer who adds seats
  is moving staff onto the product, not buying the feature per se), the seat-expansion logic is weak
  (weakens B2).

Sources follow in the table below (filled after reading pages).

## Sources
Format: `S# | exact quote | URL | how checked`

S1 | "In QuickBooks Online, you can set up automatic reminders that go out a few days before or after the due date." | https://quickbooks.intuit.com/learn-support/en-us/help-article/invoicing/send-invoice-reminders-automatically-manually/L84cQjpxo_US_en_US | second hand — read once via WebFetch but the quote-verifier re-fetch was blocked (bot wall); claim corroborated by the official help-article title and multiple search results

S2 | "Set up automatic invoice reminders in Xero to gently nudge your customers to pay on time." | https://www.xero.com/us/accounting-software/billing-and-invoicing/ | read on the page

S4 | "Compact costs $259 a month, or $233 a month billed annually, for companies under $5 million in revenue, with four users. Core is $779 a month ($700 annual) for companies under $13 million, with unlimited users. Complete is $1,169 a month ($1,050 annual) for larger companies, and above that pricing is custom." | https://accountsreceivable.ai/blog/chaser-pricing | read on a third-party page (Chaser's own pricing page returned 403; this is a review site, treat as second hand for the exact figures)

S5 | "A customer payment portal is a secure web page where your customers can see every open invoice, view statements, and pay one or more invoices at once, without emailing your team." | https://www.paidnice.com/blog/what-is-a-customer-payment-portal | read on the page (vendor blog; definitional)

S6 | "Customers cut their average wait for payment in half within 30 days" | https://www.paidnice.com/blog/what-is-a-customer-payment-portal | read on the page — vendor's own claim, not independent

S7 | Lite "$23/month"; Plus "$43/month"; Premium "$70/month" (FreshBooks plan prices) | https://tech.co/accounting-software/freshbooks-pricing | read on the page (prices only; the Tech.co page does not state portal inclusion, so no portal claim is drawn from it)

S11 | Chaser markets a standalone "customer billing portal" where clients monitor what they owe and pay | https://www.chaserhq.com/features/payment-portal | second hand — the phrase was read on the feature page via WebFetch, but the quote-verifier flagged it as a mid-sentence fragment, so it is used only as a paraphrased claim that the feature exists, not as a verbatim quote

S8 | "Standard Plan: Free, for up to 10 users with 5000 invoices chased per month." (Satago free tier for a standalone chasing tool) | https://www.getapp.com/finance-accounting-software/a/satago/pricing/ | second hand (search summary; page not opened)

S9 | "reminders that fire after payment … damages relationships" / "reminder fatigue" as a known failure mode of auto-reminders | https://www.aiwyn.ai/resources/articles/automated-payment-reminders-drive-cash-flow/ (and similar) | second hand (search summary of vendor/blog content)

S10 | Three verbatim customer quotes (office manager 9-seat; partner 4-seat; firm admin 15-seat) | examples/demos/C01-idea-to-roadmap/input/idea.md | from the PM (synthetic demo input)

## Sources that weaken the belief, and where they appear
- S1, S2, S3 (reminders + pay-online are built into Xero and QuickBooks): weaken B2 (seat expansion). Appear in the report finding "reminders are table stakes" and in "what you believed."
- S4, S8 (standalone chasing tools are priced per firm by revenue, or free): weaken B2 — the category is not monetised per seat, so a competitor parity feature does not obviously add seats. Appears in finding row 2 and the pricing note.
- S9 (auto-reminders have a known brand-risk failure mode): weakens B1's "slam dunk" framing and supports customer quote 3's caution. Appears in finding row 4 and in the roadmap guardrail.
- S6 (portal speeds payment) actually *supports* the belief; flagged as vendor claim, used only as a weak signal.

