SYNTHETIC: written for a ProdMan.AI demo on 2026-10-11. No real company, person or customer.

# PRD: Client payment portal
Owner: Maya (PM). Date: 9 October 2026. Status: draft v0.2. Squad A, design by Lena.

## Problem
Our firms' clients lose invoice emails, ask for copies and pay late. Firms spend hours each week resending invoices and chasing payments. Clients pay by whatever method the PDF shows, and accountants mark invoices paid by hand.

## Goals
1. A client can see and pay everything they owe a firm from one link.
2. Fewer "please resend the invoice" requests to firms.
3. Invoices get paid sooner.

## Non goals
- Client accounts with passwords
- Saved cards and autopay
- Automatic payment reminders (separate initiative)
- A mobile app

## Users
| User | Who they are | What they need |
|---|---|---|
| Client | Owner or bookkeeper of a small business that pays the firm. No Ledgerly login. Often reads the invoice email on a phone | See what they owe, pay it, keep a copy |
| Accountant | Staff member who owns the client relationship | Know when a client viewed or paid an invoice |
| Firm admin | Runs the firm's Ledgerly account | Turn the portal on, pick payment methods, add branding |

## Context
- Firms can issue invoices in USD, CAD, EUR and GBP, and a client's invoices can be in any of these.
- Card payments run on our existing payments partner's hosted page. Fewer than 50 firms have card payments turned on.

## Requirements
| # | Requirement | Acceptance criteria |
|---|---|---|
| R1 | Every invoice email includes a link to the client's portal | Opens the portal without a password. Expires after 30 days. On an expired link, the client can request a new one by email |
| R2 | The portal lists the client's invoices from this firm | Open invoices first, by due date. Paid invoices from the last 12 months below. Each row shows number, issue date, due date, amount and status |
| R3 | The top of the portal shows the total amount the client owes the firm | The total equals the sum of all open invoices |
| R4 | The client can pay one invoice by card | Runs on the partner's hosted page. On success the invoice is marked paid within 1 minute and the client is emailed a receipt |
| R5 | The client can select several open invoices and pay them in one card payment | The total of the selected invoices is shown before payment. One payment marks every selected invoice paid |
| R6 | The client can pay by bank transfer | |
| R7 | The client can download any invoice as a PDF | Identical to the PDF attached to the invoice email |
| R8 | The client can pay part of an invoice when the firm allows it | The client can enter an amount lower than the invoice total |
| R9 | The accountant sees when a client viewed an invoice in the portal | The invoice list in Ledgerly shows "Viewed" with the date and time |
| R10 | The portal shows the firm's logo and brand colours | |

## Success metrics
- Primary: median days from invoice sent to paid, for invoices with a portal link. Baseline: 34 days (August 2026, all firms). Target: 25 days by the end of March 2027.
- Guardrail: support tickets about payments, per 100 firms per month. Baseline: unknown.
- Leading: share of invoice emails where the client opens the portal.

## Rollout
Beta with 10 firms that already use card payments, then every firm with card payments on.

## Risks
- Clients may not trust a link in an email and phone the firm instead.
- Firms without card payments can only offer bank transfer, so they get less value.

## Open questions
1. Should the portal show invoices from other Ledgerly firms? Proposed: no.
2. Do we notify the accountant when a client pays, or is the "Paid" status enough?
