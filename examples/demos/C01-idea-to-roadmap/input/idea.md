SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# Idea: Ledgerly chases late payments for firms, and clients pay in one place
Author: Maya (PM). Date: 5 October 2026. Status: rough idea, not reviewed by anyone yet.

## The idea
Two parts that might be one product:
1. Automatic payment reminders. When a client's invoice is overdue, Ledgerly emails the client on a schedule the firm sets, until the invoice is paid.
2. A client payment portal. Each of the firm's clients gets one link where they can see every invoice from that firm and pay by card or bank transfer.

Today firms chase late payers by hand, and their clients pay outside Ledgerly. Accountants then mark each invoice as paid themselves.

## Why I think it matters
- Late payment is the complaint I hear most often from firms.
- A competitor shipped payment reminders this summer, and sales says it comes up in deals.

## Business context
- About 300 paying firms, billed per seat. List price for new firms is $25 per seat per month, billed annually.
- Seats: 1,760 at the end of June 2026 and 1,840 at the end of September 2026.
- The goal for Q1 2027 (January to March) is expansion revenue: existing firms adding seats. Leadership has asked for 300 net new seats in the quarter.
- Team: 9 engineers in two squads, 2 designers, and me as the only PM.
- Squad A has 5 engineers. About 30% of its time goes to bank feed maintenance, every quarter.
- Squad B has 4 engineers. It is finishing recurring invoices and is free from the first week of January.
- Card payments run through our existing payments partner. Fewer than 50 firms have turned card payments on.
- We have one quarter. Whatever we commit to must ship by 31 March 2027.

## Three things customers told me (verbatim, from calls in September)
1. Office manager, 9 seat firm: "Every Friday I email the clients who haven't paid. If Ledgerly did that for me, I'd move our two new juniors onto Ledgerly instead of the spreadsheet."
2. Partner, 4 seat firm: "My clients lose the invoice email and then ask me to resend it. I want one link where they can see everything they owe us and pay it."
3. Firm admin, 15 seat firm: "Reminders sound useful, but I'm nervous about a robot nagging my biggest clients. I'd need to control who gets chased and what it says."

## What I don't know yet
- What competitors offer here and what they charge for it.
- How many of our firms' invoices are paid late today.
- How long either part would take to build. Nobody has estimated it.
