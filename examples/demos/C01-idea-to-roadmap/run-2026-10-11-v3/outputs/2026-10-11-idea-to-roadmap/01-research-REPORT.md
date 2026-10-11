DRAFT, not reviewed by a person

# Is payment reminders + a client payment portal the right bet for Q1 2027, and will it drive firms to add seats?

## The call
Build it, but do not sell it as "reminders." Automatic reminders are now a built-in feature of
the big accounting platforms ([Xero](https://www.xero.com/us/accounting-software/billing-and-invoicing/),
[QuickBooks Online](https://quickbooks.intuit.com/learn-support/en-us/help-article/invoicing/send-invoice-reminders-automatically-manually/L84cQjpxo_US_en_US)),
so reminders on their own are table stakes and a weak reason to add seats. The part that is both
differentiated and tied to seat growth is the portal plus the behaviour one customer described:
moving manual chasing work *onto* Ledgerly. Evidence for demand is medium; evidence that it drives
seat expansion is weak (one firm said so, verbatim). Confidence: **medium**.

## What would change this call
The idea rests on firms having enough late invoices for reminders to matter, and `idea.md` lists
"how many of our firms' invoices are paid late today" as unknown. **Test:** pull the share of invoices
paid after the due date across the ~300 firms. If the median firm has few overdue invoices, reminders
will not change behaviour and the bet should shrink to the portal. The data is in Ledgerly's own
database; this is a one-query check, not research.

## What you believed, and what happened to it
- **B1 — reminders + portal is the right bet because late payment is the top complaint:** mostly
  **held**, but softened. Demand is real, yet reminders are a commodity and auto-chasing carries a
  known brand-risk failure mode (reminders firing after payment, "reminder fatigue"). This matches
  your own customer 3, who is "nervous about a robot nagging my biggest clients."
- **B2 — it will drive existing firms to add seats:** **largely did not hold on the evidence.** No
  competitor monetises this per seat; standalone tools charge the firm by revenue band or give it away.
  The only seat-expansion evidence is one quote (customer 1). The lever is not the feature, it is
  making Ledgerly the place staff do the work.

## What we found
| What we found | The evidence | How sure |
|---|---|---|
| Reminders are built into Xero and QuickBooks and included in their plans | Xero: "Set up automatic invoice reminders in Xero to gently nudge your customers to pay on time" ([Xero](https://www.xero.com/us/accounting-software/billing-and-invoicing/)); QuickBooks: automatic reminders "a few days before or after the due date" ([QBO](https://quickbooks.intuit.com/learn-support/en-us/help-article/invoicing/send-invoice-reminders-automatically-manually/L84cQjpxo_US_en_US)) | Xero checked on the page; QuickBooks read then re-fetch blocked, so second hand |
| The portal is the more differentiated half: see and pay several invoices at once from one place | portal lets customers "can see every open invoice, view statements, and pay one or more invoices at once" ([Paidnice](https://www.paidnice.com/blog/what-is-a-customer-payment-portal)); Chaser sells a standalone customer billing/payment portal as a paid feature ([Chaser](https://www.chaserhq.com/features/payment-portal)) | Paidnice checked on the page; Chaser feature paraphrased |
| Standalone chasing tools are priced per firm by revenue, or free, never per seat | Chaser Compact "$259 a month … under $5 million" to Complete "$1,169 a month" ([review](https://accountsreceivable.ai/blog/chaser-pricing)); Satago has a free tier ([GetApp](https://www.getapp.com/finance-accounting-software/a/satago/pricing/)) | one review site (Chaser's own page blocked); Satago second hand |
| Auto-reminders have a real brand-risk failure mode firms fear | reminders "that fire after payment … damage relationships" and "reminder fatigue" ([Aiwyn](https://www.aiwyn.ai/resources/articles/automated-payment-reminders-drive-cash-flow/)); your customer 3 says the same | one source + your interview |
| Portals plausibly speed payment (weak, vendor claim) | "Customers cut their average wait for payment in half within 30 days" ([Paidnice](https://www.paidnice.com/blog/what-is-a-customer-payment-portal)) | vendor's own claim, not independent |

**What it changes:** Reminders must ship, because their absence is now conspicuous, but they will not
by themselves earn seats. The portal is the thing clients touch and the thing rivals charge for.
Seat growth has to be engineered into the product, by making Ledgerly the system of record for chasing
and collection so firms put more staff on it (customer 1's exact logic). Control over who gets chased
is not optional polish; it is the price of entry for the firms with big clients (customer 3).

## What the PM books predict
- **Jobs to be Done (Christensen):** predicts the job is getting paid without the awkward weekly
  chase, which the portal and reminders serve together; the evidence agreed (customers 1 and 2).
- **Kano:** predicts reminders are now a "must-be" (their absence annoys, their presence delights no
  one) while a good portal can still be a "performance" feature; the competitor evidence agreed.
- **The four big risks (Cagan):** value and usability look addressable; **viability** is the open risk,
  because the per-seat business model is not how this category is monetised. The evidence flagged it.

## What we could not check
- How many of your firms' invoices are actually paid late (no data provided; your own DB can answer).
- Whether your <50 card-enabled firms is a supply problem (your payments partner) or a demand one.
- Chaser's exact live prices (their pricing page blocked a read; figures are from a review site).
- US vs non-US pricing and plan inclusions for each rival; checked at a feature level, not plan-by-plan.

## Next step
Run the "share of invoices paid late" query this week; it decides how big the reminders bet should be
before a line of code is written.
