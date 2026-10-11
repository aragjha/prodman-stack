DRAFT, not reviewed by a person

# Release notes — invoicing & payments

> SYNTHETIC — built from test ticket titles in [00-request.md](00-request.md). Not a real release.
> Date unknown (no release date was given).

## What changed

**New**
- **Export invoices as CSV.** You can now export invoices as a CSV file from the invoice list. *(PAY-412)*
- **"Pay now" link in reminder emails.** Payment reminder emails now include a "pay now" link. *(PAY-418)*
- **Default payment term per client.** Admins can set a default payment term for each client. *(PAY-420)*

**Fixed**
- **Due dates now use your time zone.** Due dates showed in UTC instead of the firm's time zone; they now show in the firm's time zone. *(PAY-415)*
- **Search handles accented client names.** Invoice search ignored client names with accents; it now matches them. *(PAY-421)*

## Who it is for
- Anyone who works with the invoice list (export, search, due dates).
- Admins (default payment term per client).
- Your clients, indirectly: they get a "pay now" link in reminder emails.

## How to use it
- **CSV export:** open the invoice list and export to CSV. *(Exact button label not in the ticket.)*
- **Default payment term:** an admin sets a default term per client. *(Where in settings is not in the ticket.)*
- **"Pay now" link, time-zone fix, accent search:** nothing to do.

## Known issues
None provided with these tickets.
