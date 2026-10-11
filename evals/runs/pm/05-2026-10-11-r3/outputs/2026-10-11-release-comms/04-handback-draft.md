DRAFT, not reviewed by a person

RESULT        Release notes for the five payment tickets are drafted and ready to post; nothing was posted to Slack or closed in Jira — both are human-checkpoint actions handed back to you. · outputs/2026-10-11-release-comms/01-release-notes.md (Slack block: 02-slack-post.md)

ROUTE         G01 (Release and product communication), because this writes audience-facing notes from tickets and ends in a post — exactly G01's problem · skills run: pm → deidentify (inline pass) · no fallbacks

STEPS (G01)
  1. Confirm what shipped — done (01-release-notes.md header): no merge status was provided; the five are treated as the release on your framing, and that assumption is flagged.
  2. Breaking changes & known issues first — done (03-go-live-checklist.md): none were provided; checklist asks you to confirm before posting.
  3. Write release notes, then per-audience message — release notes + one #product-updates message done (01, 02). Other audiences (end users, API partners) not written: no audience list beyond #product-updates was given — flagged, not invented.
  4. Deidentify anything public — done (02-slack-post.md): no identifying data found; content is synthetic and generic.
  5. Go-live checklist + stop for approval — done (03-go-live-checklist.md); stopped before posting and closing.

CHECKS        28 rows / 2 corrected / 0 removed · checked by subagent (fresh pass) · link: 05-check.md
              Clarity | pass | each item is one line, new vs fixed split
              Visual | pass | New/Fixed headings; key point readable in under 60s
              Concise | pass | one line per ticket, nothing padded
              Decision | n/a→pass | this is a comms artifact; the "call" is what to post and the stop before posting
              Honesty | pass | missing merge status, audiences, and known issues all named, not filled
              Accuracy | pass after 1 fix | the PAY-420 line had overstated its ticket ("so new invoices start with the right term"); removed. Every feature line now traces to its ticket (see 05-check.md)

NEEDS YOUR JUDGMENT
  1. Merge status: no ticket said whether it is merged/shipped. I assumed all five shipped. Confirm before posting — G01's first rule is to exclude anything not merged.
  2. Breaking changes: none were flagged to me. PAY-415 (due dates move from UTC to firm time zone) *could* surprise anyone who relied on the old display — confirm it is not breaking before posting.
  3. Audience: I wrote only the #product-updates (internal) message. If end users or API partners also need notes, say so — those are separately worded.
  4. The two external actions (post, close tickets) are yours to take; I stopped at the line.

NEXT ACTIONS
  1. You: confirm the three items above, then post the block in 02-slack-post.md to #product-updates.
  2. You: close PAY-412/415/418/420/421 in Jira once posted.
  3. You (optional): ask me for end-user / API-partner versions if those audiences apply.

ASSUMPTIONS
  - All five tickets are merged and shipped (not stated).
  - #product-updates is an internal channel.
  - No breaking changes and no known issues beyond what the tickets state.

CONFIDENCE    medium — the notes are faithful to the ticket text, but I cannot verify merge status, breaking changes, or the right audience set without you.
