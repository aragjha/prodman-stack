SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# Funnel metric definitions
Owner: Felix (backend engineer, owns the analytics events)
Last updated: 2 September 2026

| Metric | Definition | Source event |
|---|---|---|
| Signups | Firms that completed signup and started the 14 day free trial during the week | firm_signed_up |
| Activated firms | Firms from that week's signups that sent their first invoice within 7 days of signing up. Counted against the signup week, so a week's number is final 7 days after the week ends | invoice_sent, first one per firm |
| Invoices sent | Invoices emailed to a client for the first time during the week. Resends are not counted | invoice_sent |
| Paid within 30 days | Invoices marked paid during the week whose paid date is no more than 30 days after the invoice was first sent | invoice_marked_paid |
| Seats added | Seats added to existing firm accounts during the week. A firm's first seat is not counted. Which firms are counted changed in August 2026, see the change log | seat_added |
| Churned firms | Paying firms whose subscription ended during the week | subscription_ended |

## Change log
| Date | Metric | Change |
|---|---|---|
| 2 March 2026 | Churned firms | Firms that cancel during the free trial are no longer counted as churned |
| 24 August 2026 | Seats added | Now counts seats added in firms on a free trial as well as in paying firms. Before this, it counted paying firms only. Applies from the week of 24 August. The event change shipped with release 4.1 |

## Check run for the 24 August change
Felix counted the week of 24 August both ways: 61 seats added under the new definition, of which 29 were in paying firms and 32 in firms on a free trial.
