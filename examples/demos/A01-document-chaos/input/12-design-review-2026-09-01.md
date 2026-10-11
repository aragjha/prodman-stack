SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# Design review: recurring invoices setup flow, round 2
Date: 1 September 2026
Present: Lena (design lead), Sam (designer), Maya (PM), Noor (frontend), Felix (backend)

## Agreed
- Setup takes three steps: pick the client, pick the schedule, review the first invoice.
- Auto send on the billing date. No manual approval step by default.
- The preview email goes to the accountant who owns the client 3 days before send, so mistakes can be caught over a weekend.
- The upcoming invoices list shows the next 60 days, grouped by week.
- A paused series shows a banner on the client page, so nobody wonders why invoices stopped.

## Not agreed
- Custom recurrence rules need a rules builder. Sam's mock has 9 controls on one screen and tested badly with 2 internal users. Sam to try a simpler version.
- Bounced client emails: Felix says we retry once; Lena wants the accountant told the same day.

## Next review
15 September
