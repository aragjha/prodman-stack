SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# PRD: Recurring invoices (v2, fragment)
Owner: Maya (PM). Date: 28 August 2026. Status: in review. Supersedes v1 (15 July).

## What changed from v1
- Autopay is out of launch and moves to phase 2 (Q1 2027). Storing client cards needs a security review we cannot finish this quarter.
- The upcoming invoices list now covers 60 days instead of 30.
- Launch target moves to late November, pending Kwame's estimate.

## Requirements for launch
| # | Requirement | Priority |
|---|---|---|
| R1 | Ledgerly creates and emails each invoice in a series on its scheduled date | Must |
| R3 | Firm admins see every scheduled invoice for the next 60 days in one list | Must |
| R4 | Pause a series and resume it later without losing its settings | Must |
| R5 | The accountant who owns the client gets a preview email 24 hours before an invoice is sent | Must |
| R6 | Changing a series updates future invoices only, never invoices already sent | Must |
| R7 | Custom recurrence rules, for example every second Tuesday or the last working day of the month | Should |

## Non goals for launch
- Autopay (phase 2)
- Recurring invoices in any currency other than the firm's default currency
- Automatic payment reminders for overdue invoices (separate initiative, not planned this year)

## Success metric
30% of active firms have at least one live series 60 days after launch. Baseline: 0, new feature.
