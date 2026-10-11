DRAFT, not reviewed by a person

# 01 · What actually shipped (Step 1: exclude anything not merged)

Source: `release-scope.md`. Rule from that file: "Anything not merged at code freeze is not in 4.2."

## In 4.2 (Merged at freeze)
| Ticket | What it does | Area |
|---|---|---|
| LED-501 | Send up to 50 draft invoices at once from the invoice list | Invoicing |
| LED-502 | Email the accountant who owns a client when that client pays an invoice (on by default; each user can turn it off in Settings → Notifications) | Notifications |
| LED-503 | Filter the client list to clients with overdue invoices | Clients |
| LED-504 | API: `amount` field in GET /v2/invoices and GET /v2/payments changes from a decimal string to an integer number of cents ("1250.00" → 125000). **Breaking.** No flag to keep old format. v1 endpoints unchanged | API |
| LED-505 | New firms start with a ready-to-use default invoice template again | Templates |
| LED-506 | Export payments to CSV for any date range (known issue below) | Reports |
| LED-509 | Fix: due dates shown one day early for firms in some time zones | Invoicing |

## NOT in 4.2 (Not merged at freeze — must not appear in any note)
| Ticket | What it was | Why excluded |
|---|---|---|
| LED-507 | Recurring invoices: pause and resume a series | Not merged at code freeze |
| LED-508 | Bank feed: match incoming payments to open invoices automatically | Not merged at code freeze |

Count: 7 merged, 2 not merged, 9 total.
