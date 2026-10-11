# 05 · Go-live checklist — DRAFT

Release 4.2 · planned Tuesday 20 October 2026 · release manager Kwame · PM Maya.
Everything below is a draft action for a human; nothing here has been done.

## Must resolve before release
- [ ] **Partner-notice obligation (LED-504).** The ≥14-day notice deadline was 6 Oct 2026; notice is
      not sent. Decide one of: (a) delay the `amount` change to a release ≥14 days after notice is
      sent; (b) get Jonas's written agreement to the shorter notice; (c) ship 4.2 on 20 Oct
      **without** LED-504 and release the `amount` change separately once 14 days' notice has run.
      **Owner: Maya + partner-agreement owner.**
- [ ] Set the `[GO-LIVE DATE]` in the changelog and the Jonas email to match whatever (a)/(b)/(c)
      decides. Do not send with the placeholder in place.

## Approvals before anything leaves the machine
- [ ] Maya approves the admin email and "What's new" panel copy.
- [ ] Maya approves the accountant "What's new" panel copy.
- [ ] Partner-agreement owner approves the changelog entry and the Jonas email.

## Publish / send (only after approval)
- [ ] Publish the "What's new" panel (admins + accountants).
- [ ] Send the monthly product email to firm admins.
- [ ] Publish the API changelog entry.
- [ ] Send the breaking-change email to Jonas and get his acknowledgement.

## Verify after release
- [ ] Confirm LED-507 and LED-508 are **not** referenced anywhere as shipped (they didn't merge).
- [ ] Confirm the LED-506 known-issue note (10,000-row timeout + workaround) is in the admin and
      accountant copy.
- [ ] Confirm LED-502's opt-out path (Settings → Notifications) is stated for admins.

## Notes
- No Slack or Jira connector was used; nothing was posted, sent, or changed in any tracker.
- The new-firm default template (LED-505) was intentionally left out of the firm-facing messages
  because it only affects new firms.
