# 01 · What actually shipped in 4.2

Rule: anything not merged at code freeze (Friday 9 October 2026) is not in 4.2.

## In 4.2 (merged at freeze)
| Ticket | What it does | Area | Notes that affect comms |
|---|---|---|---|
| LED-501 | Send up to 50 draft invoices at once from the invoice list | Invoicing | — |
| LED-502 | Email the accountant who owns a client when that client pays an invoice | Notifications | On by default; each user can turn it off in Settings → Notifications |
| LED-503 | Filter the client list to clients with overdue invoices | Clients | — |
| LED-504 | API: `amount` in `GET /v2/invoices` and `GET /v2/payments` changes from a decimal string to an integer number of cents (`"1250.00"` → `125000`) | API | **Breaking change.** No flag to keep the old format. v1 endpoints unchanged |
| LED-505 | New firms start with a ready-to-use default invoice template again | Templates | Affects **new firms only** |
| LED-506 | Export payments to CSV for any date range | Reports | **Known issue:** exports over 10,000 rows time out. Workaround: shorter date range. Fix planned for 4.2.1 |
| LED-509 | Fix: due dates shown one day early for firms in some time zones | Invoicing | — |

## NOT in 4.2 (not merged at freeze — must not appear as shipped)
| Ticket | What it was | Why excluded |
|---|---|---|
| LED-507 | Recurring invoices: pause and resume a series | Not merged at freeze |
| LED-508 | Bank feed: match incoming payments to open invoices automatically | Not merged at freeze |

## Flags that drive the messages
1. **LED-504 is a breaking change** and only the API partner is affected. Admins and accountants
   don't see API content (accountants don't know what an API is — `audience.md`).
2. **Partner-notice obligation:** agreement requires ≥14 days' written notice before a breaking API
   change. 14 days before 20 Oct = **6 Oct 2026**. The notice is **not yet sent**. Sending today
   (11 Oct) gives only **9 days**. See the judgment list in the handback — this is a decision, not
   a drafting problem.
3. **LED-506 ships with a known issue** — list it for admins/accountants with the workaround.
4. **LED-505 affects new firms only** — low relevance to the existing ~300 firms; keep it minor.
5. **LED-502 is on by default** and changes what a team receives — admins need the opt-out path.
