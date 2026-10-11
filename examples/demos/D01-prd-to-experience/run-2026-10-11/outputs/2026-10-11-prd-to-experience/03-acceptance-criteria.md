# 03 · Acceptance criteria

The PRD already has testable criteria for R1–R5, R7, R9. This file (a) fills the two blanks (R6,
R10) and (b) adds criteria for the edge/error states the flows surfaced. **Proposed criteria are
marked [proposed]** — they are suggestions for Maya to confirm, not added scope. Each is written so
a tester can pass or fail it.

## Criteria to fill the blanks
| # | Requirement | Acceptance criteria [proposed] |
|---|---|---|
| R6 | Pay by bank transfer | On an invoice the firm has bank transfer enabled for, the portal shows the firm's bank details and a payment reference tied to the invoice. The invoice moves to **Payment pending** and is **not** auto-marked paid. It becomes **Paid** only when the firm reconciles it in Ledgerly. The client sees text explaining the firm will confirm once the transfer arrives. *(Open: is a receipt emailed for bank transfer? R4's receipt is card-only.)* |
| R10 | Firm logo and brand colours | The portal header shows the firm's logo and applies the firm's two brand colours (primary, accent) set in Ledgerly admin. If a firm has set none, a neutral default theme renders. Applied brand colours must meet a minimum text contrast ratio of **4.5:1**; if a chosen colour fails, the portal substitutes a legible fallback and the admin is warned. *(Contrast floor is a [proposed] addition — see 01-D.)* |

## Proposed criteria for the edge, empty and error states
| State / behaviour | Acceptance criteria [proposed] | From |
|---|---|---|
| Multi-currency total (R3) | The portal shows **one subtotal per currency** for open invoices; it never sums across currencies into a single figure. | gap B |
| Multi-pay same currency (R5) | Selecting invoices is limited to one currency per payment; selecting a second currency is prevented with a visible message. | gap B |
| Card declined (R4) | The invoice remains **Open**, no status change, and the client is offered a retry. | Flow 1 |
| Partner page unreachable / timeout (R4) | The invoice remains **Open**; the client returns to a message that payment couldn't be completed and can retry. | Flow 1 |
| Tab closed mid-payment (R4) | The invoice stays **Open** (or **Payment pending** if a charge is in flight) until the partner confirms; on confirmation it becomes **Paid** and the receipt fires. No duplicate charge is created on retry. | Flow 1 |
| Invoice already paid (R4/R5) | If an invoice is paid by any route, the pay action for it is disabled and it shows **Paid**; it drops out of any active multi-select with a notice and the running total recomputes. | Flows 1–2 |
| Partial payment (R8) | The partial-pay control appears only when the firm has enabled it for that invoice. Entered amount must be > 0 and < the remaining balance. After payment the invoice is **Partially paid**, the remaining balance is shown, and that balance still counts toward the owed total and stays payable. | Flow 4 |
| Expired link (R1) | Links older than 30 days show the **Link expired** screen with a working "email me a new link" action that confirms on screen. | Flow 5 |
| Revoked / invalid link | A malformed link, or a portal the firm has turned off, shows a distinct "this link isn't available" screen directing the client to contact the firm. | Flow 5 |
| PDF download (R7) | The downloaded PDF is byte-identical to the one attached to the invoice email (this is in R7). *(Open: is download allowed on an expired link?)* | R7 / gap C |
| Empty state (nothing owed) | When no invoices are open, the portal shows an "all paid up" state with paid history and PDF downloads, not a blank list. | Flow 6 |
| Bank-transfer-only firm | For firms without card payments, no card or multi-select pay controls render; only the bank transfer path is offered. | gap F |
| Accessibility baseline | The pay flow is operable on a phone one-handed, by keyboard, and with a screen reader; amounts and currencies are announced; interactive controls have labels and visible focus. *(Starting point, not an audit.)* | gap D |

Everything marked [proposed] needs Maya's yes/no before it becomes a build commitment.
