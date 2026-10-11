RESULT        Release notes for the five PAY tickets are drafted and ready; posting to Slack and closing Jira are staged for you, not done. · outputs/2026-10-11-pay-release-notes/02-release-notes.md
ROUTE         G01 Release and product communication, because a release is ready and needs notes plus publication · skills run: pm → deidentify (inline pass) · fallbacks: deidentify run inline by the author, not a separate session
STEPS         1 Confirm what shipped (done, 01-shipped.md) · 2 Breaking changes & known issues (done, 01-shipped.md) · 3 Write release notes (done, 02-release-notes.md) · 4 Deidentify anything public (done, 03-deidentify.md) · 5 Go-live checklist, stop for approval (done, 04-go-live-checklist.md)
CHECKS        {{CHECKS}}
NEEDS YOUR JUDGMENT
              1. Merge status — I was given five ticket titles only, no status field. I trusted them as shipped. Confirm all five are merged before anything goes out; if not, name which to drop.
              2. Posting to #product-updates — NOT done. This is your call and your action; I have no Slack connector. Approve the text in 04-go-live-checklist.md and post it yourself.
              3. Closing the five tickets in Jira — NOT done. Editing a real tracker is a human checkpoint; I have no Jira connector. Close them yourself after the notes are posted.
              4. Two how-to gaps — the CSV export button label and where admins set the default payment term are not in the tickets. Fill them or I will leave them generic.
              5. Release date and known issues — neither was given. The notes carry no date and an empty known-issues line until you supply them.
NEXT ACTIONS  1. You: confirm merge status + release date (owner: you). 2. You: post the approved message to #product-updates (owner: you). 3. You: close PAY-412/415/418/420/421 in Jira (owner: you).
ASSUMPTIONS   The five titles are the only input; merge state is not stated. The audience is an internal Slack channel, so ticket IDs are fine to keep. No breaking changes or known issues exist beyond what the titles state.
CONFIDENCE    medium — the notes are faithful to the titles, but I have no ticket bodies, no status, and no release date, so completeness depends on your confirmation.
