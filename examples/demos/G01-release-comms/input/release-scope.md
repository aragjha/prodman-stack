SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# Release 4.2: scope at code freeze
Release manager: Kwame (eng lead). PM: Maya.
Code freeze: Friday 9 October 2026. Planned release: Tuesday 20 October 2026.
Anything not merged at code freeze is not in 4.2.

| Ticket | Description | Area | Status at freeze | Notes |
|---|---|---|---|---|
| LED-501 | Send up to 50 draft invoices at once from the invoice list | Invoicing | Merged | |
| LED-502 | Email the accountant who owns a client when that client pays an invoice | Notifications | Merged | On by default. Each user can turn it off in Settings, Notifications |
| LED-503 | Filter the client list to clients with overdue invoices | Clients | Merged | |
| LED-504 | API: the `amount` field in GET /v2/invoices and GET /v2/payments changes from a decimal string to an integer number of cents, so "1250.00" becomes 125000 | API | Merged | Breaking change for API integrations. There is no flag to keep the old format. v1 endpoints do not change |
| LED-505 | New firms start with a ready to use default invoice template again | Templates | Merged | |
| LED-506 | Export payments to CSV for any date range | Reports | Merged | Known issue: exports over 10,000 rows time out. Workaround: export a shorter date range. Fix planned for 4.2.1 |
| LED-507 | Recurring invoices: pause and resume a series | Recurring invoices | Not merged | |
| LED-508 | Bank feed: match incoming payments to open invoices automatically | Bank feeds | Not merged | |
| LED-509 | Fix: due dates shown one day early for firms in some time zones | Invoicing | Merged | |

Partner notice for LED-504: not sent yet.
