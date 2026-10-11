DRAFT, not reviewed by a person

# 03 · Release 4.2 notes — one message per audience

Planned release: Tuesday 20 October 2026 (see go-live checklist and the notice conflict for LED-504).
House style applied: plain words; **no ticket numbers in the firm-admin or accountant messages**.
Ticket numbers are kept only in the partner/API material, where engineers use them.

Audiences are the three defined in `audience.md`: firm admins, accountants, API partner. (The G01
description in `workflows/INDEX.md` says "four audiences need four different messages"; our input
defines three distinct reader groups.)

---

## A · Master release notes (internal reference — not published as-is)

Shape per PM.md §5: what changed · who it is for · how to use it · known issues.

| What changed | Who it's for | How to use it | Known issues |
|---|---|---|---|
| Send up to 50 draft invoices at once from the invoice list | Accountants | Select drafts in the invoice list, send together | — |
| You get an email when a client you own pays an invoice | Accountants (on by default) | Turn it off in Settings → Notifications | — |
| Filter the client list to clients with overdue invoices | Accountants | Use the overdue filter on the client list | — |
| Export payments to CSV for any date range | Firm admins, accountants | Choose a date range and export | Exports over 10,000 rows time out; export a shorter range; fix planned for 4.2.1 |
| New firms start with a ready-to-use default invoice template again | New firms | Automatic for new firms | — |
| Fix: due dates no longer shown one day early in some time zones | Accountants | Automatic | — |
| API: `amount` in `GET /v2/invoices` and `GET /v2/payments` now an integer of cents | API partner | See partner changelog below | Breaking; 14-day notice not yet met (see §02) |

Not in 4.2 (not merged at freeze): pause/resume recurring invoices; automatic bank-feed matching.
Do not mention these anywhere.

---

## B · Firm admins — monthly product email + "What's new" panel (DRAFT)

**Subject: What's new in Ledgerly 4.2**

Hi there,

Ledgerly 4.2 is rolling out on 20 October. Here's what changes for your firm. Nothing here needs you
to act, with one thing to know about notifications.

- **Pay-received emails are now on.** When a client pays an invoice, the accountant who owns that
  client gets an email. This is on for everyone by default. Anyone on your team who doesn't want it can
  turn it off in **Settings → Notifications**.
- **Send up to 50 draft invoices at once.** Your team can select a batch of drafts and send them in one
  go from the invoice list.
- **Filter clients by overdue invoices.** A new filter shows just the clients who have an overdue
  invoice.
- **Export payments to CSV for any date range.** Useful for reconciling or reporting. One known issue:
  exports of more than 10,000 rows currently time out — export a shorter date range for now. A fix is
  planned for the next update.
- **Due-date display fix.** Due dates were showing a day early for firms in some time zones. That's
  fixed.

If you onboard a new firm, it again starts with a ready-to-use default invoice template.

Questions? Just reply to this email.

---

## C · Accountants — "What's new" panel (DRAFT)

Each entry is a headline plus one line (most accountants read only the headline and first line).

**Send up to 50 drafts at once**
Select draft invoices in the list and send them together — no more one at a time.

**Know the moment a client pays**
You'll get an email when a client you own pays an invoice. Don't want it? Settings → Notifications.

**Find overdue clients fast**
New filter on the client list shows only clients with an overdue invoice.

**Due dates are correct again**
Due dates were showing a day early in some time zones. Fixed.

**Export payments to CSV**
Export payments for any date range. (Very large exports — over 10,000 rows — time out for now; use a
shorter range.)

---

## D · API partner — changelog entry + email to Jonas (DRAFT)

### D1 · API changelog entry

**Ledgerly API v2 — breaking change to `amount` (LED-504)**

- **Go live:** [SHIP DATE — to confirm; see conflict below. Must be ≥14 days after the notice email.]
- **Endpoints affected:** `GET /v2/invoices`, `GET /v2/payments`.
- **Change:** the `amount` field changes from a **decimal string** to an **integer number of cents**.
- **Before / after:**
  - Before: `"amount": "1250.00"`
  - After: `"amount": 125000`
- **What you must change:** read `amount` as an integer and divide by 100 to get the currency value
  (e.g. `125000 / 100 = 1250.00`). Stop parsing it as a decimal string.
- **No compatibility flag:** there is no option to keep the old format.
- **v1 unchanged:** `v1` endpoints are not affected.

### D2 · Email to Jonas (DRAFT — do not send until the ship date is settled; see §02)

**To:** Jonas (integration lead)
**Subject: Breaking change to the Ledgerly v2 API `amount` field — action needed**

Hi Jonas,

We have a breaking change to the v2 API in our next release that affects your nightly integration, so
I want to give you the details early.

**What's changing:** in `GET /v2/invoices` and `GET /v2/payments`, the `amount` field changes from a
decimal string to an integer number of cents.

- Before: `"amount": "1250.00"`
- After: `"amount": 125000`

**What you need to do:** read `amount` as an integer and divide by 100 to get the value. There is no
flag to keep the old format. The `v1` endpoints are unchanged, so if you ever need more time you could
read from v1 in the meantime.

**When it goes live:** [DATE — to confirm]. Per our agreement we give at least 14 days' written notice
before a breaking change, so the go-live date will be at least 14 days after this email.

Please confirm you've received this and let me know if the timing is a problem on your side.

Thanks,
Maya
