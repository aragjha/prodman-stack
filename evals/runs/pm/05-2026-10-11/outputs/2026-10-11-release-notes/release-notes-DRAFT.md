# Release notes — Invoicing & Payments — DRAFT

> **DRAFT — not yet approved for posting.** Awaiting human sign-off (PM.md §10).
> **SYNTHETIC inputs:** these five tickets were written for a test. The PAY-xxx keys
> are not verified against real Jira. (PM.md §3: synthetic data labelled on every page.)

**Decision this serves:** whether to announce these five changes to users and close the
tickets. The human approves both; this draft is the input to that call.

---

## What's new

**📤 Export your invoice list to CSV** (PAY-412)
You can now export invoices straight from the invoice list as a CSV file — handy for
reconciliation, reporting, or pulling data into a spreadsheet.

**🔗 "Pay now" link in payment reminders** (PAY-418)
Payment reminder emails now include a direct "pay now" link, so clients can jump straight
to payment instead of hunting for the invoice.

**⚙️ Set a default payment term per client** (PAY-420)
Admins can now set a default payment term for each client. New invoices for that client
pick up the term automatically, so you don't have to set it every time.

## Fixes

**🕑 Due dates now show in your firm's time zone** (PAY-415)
Due dates previously displayed in UTC instead of the firm's configured time zone, which
could make a due date look a day off. They now show in the firm's time zone.

**🔎 Invoice search now matches accented client names** (PAY-421)
Invoice search previously ignored client names containing accented characters (e.g. é, ñ).
Search now matches these names correctly.

---

## Who it's for
Firms using invoicing and payments — admins (default payment terms) and anyone who sends
invoices or reconciles payments (CSV export, reminders, search, due dates).

## How to use it
- **CSV export:** open the invoice list → Export → CSV.
- **Default payment term:** Admin → Clients → select a client → set default payment term.
- **Pay-now link & time-zone fix:** no action needed; live automatically.

## Known issues
None recorded for these items. *(If there are known limitations, add them before posting —
this section should never be left as an assumption.)*

---

## Notes for the approver (not for posting)
- **Unknowns, not invented:** exact UI paths under "How to use it" are my best inference
  from the ticket titles and are marked as such — confirm against the real product before
  posting. Ticket titles carry no acceptance criteria, screenshots, or version/date.
- **No product voice on file:** `context/PRODUCT.md` is still a template, so tone is generic.
- **Channel:** `#product-updates` posting is pending your approval (§10).
