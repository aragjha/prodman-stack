SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# PRD: Recurring invoices (v1, fragment)
Owner: Maya (PM). Date: 15 July 2026. Status: draft.

## Problem
Most firms bill their clients a fixed monthly retainer. Today an accountant copies last month's invoice for every client by hand.

## Goal
A firm sets up a client's billing once, and Ledgerly sends the invoices on schedule.

## Requirements for launch
| # | Requirement | Priority |
|---|---|---|
| R1 | Ledgerly creates and emails each invoice in a series on its scheduled date | Must |
| R2 | Autopay: charge the client's saved card automatically when a recurring invoice is issued | Must |
| R3 | Firm admins see all scheduled invoices for the next 30 days in one list | Must |
| R4 | Pause a series and resume it later without losing its settings | Must |
| R5 | The accountant who owns the client gets a preview email 24 hours before an invoice is sent | Should |
| R6 | Changing a series updates future invoices only, never invoices already sent | Must |
| R7 | Custom recurrence rules, for example every second Tuesday or the last working day of the month | Should |

## Launch
Target: end of October 2026.

## Open questions
- Which card processor stores client cards for autopay?
- Do we need a security review before we store cards?
