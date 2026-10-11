DRAFT, not reviewed by a person

# Go-live checklist (step 5 of G01)

Nothing below has been done. Everything stops here for your approval (PM.md §10: stop before you
post, share, or edit a real tracker). I also have no Slack or Jira connector, so I could not take
these actions even if they were approved — they are yours to run.

## Before you post
- [ ] Confirm all five tickets are actually merged/shipped (I was given titles only, no status).
- [ ] Confirm the release date to put on the notes (none was given).
- [ ] Fill the two how-to gaps in [02-release-notes.md](02-release-notes.md): the CSV export button
      label and where admins set the default payment term.
- [ ] Confirm there are no known issues to list.

## Action 1 — post to #product-updates (NOT done)
Paste-ready message for the channel (same content as [02-release-notes.md](02-release-notes.md),
minus the synthetic/date caveats):

```text
:tada: Invoicing & payments updates

New
• Export invoices as CSV from the invoice list (PAY-412)
• Payment reminder emails now include a "pay now" link (PAY-418)
• Admins can set a default payment term per client (PAY-420)

Fixed
• Due dates now show in the firm's time zone instead of UTC (PAY-415)
• Invoice search now matches client names with accents (PAY-421)
```

## Action 2 — close the five tickets in Jira (NOT done)
To transition to Done once the notes are posted: PAY-412, PAY-415, PAY-418, PAY-420, PAY-421.

I will not post or close anything. Tell me "approved" after you have checked the notes and I will
hand you the final text to post and close yourself, or guide you through it.
