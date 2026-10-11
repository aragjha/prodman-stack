DRAFT, not reviewed by a person

# 05 · Go-live checklist — Release 4.2

Nothing below has been done by this skill. It drafts; a person posts, sends and decides.

## Must decide first (blocks the API part of the release)
- [ ] **LED-504 ship date vs 14-day notice.** The latest date to send 14-day notice for a 20 Oct
      release was **6 Oct** (past). Notice is not yet sent. Choose one, with Kwame:
      - Hold LED-504 for a later release (e.g. 4.2.1), ship the rest on 20 Oct, remove §D from this
        batch; **or**
      - Send the partner notice now and move the LED-504 go-live to **≥14 days after the notice email**
        (earliest 25 Oct if sent 11 Oct); **or**
      - Get written agreement from the partner to waive/shorten the 14-day notice, recorded in writing.

## Content review (human)
- [ ] Review and approve §B firm-admin email, §C accountant panel, §D1 changelog, §D2 partner email.
- [ ] Confirm sender name/sign-off on the partner email.
- [ ] Confirm "What's new" panel wording fits the panel's length limits.

## Publish / send (only after approval)
- [ ] Set the final LED-504 go-live date in §D1 and §D2.
- [ ] Send partner notice email to Jonas (per the decision above) — starts the notice clock.
- [ ] Publish firm-admin monthly email.
- [ ] Publish accountant "What's new" panel entries.
- [ ] Publish API changelog entry.

## Day-of (20 Oct, or chosen date)
- [ ] Confirm all 7 merged items are in the build; confirm LED-507 and LED-508 are NOT.
- [ ] Watch for CSV export timeouts (>10,000 rows, LED-506 known issue); keep the 4.2.1 fix tracked.
