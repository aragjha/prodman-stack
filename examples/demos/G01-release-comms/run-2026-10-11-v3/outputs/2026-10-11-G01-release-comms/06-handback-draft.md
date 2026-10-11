DRAFT, not reviewed by a person

# 06 · Hand back

RESULT        Release 4.2 drafted for three audiences, plus a go-live checklist; the LED-504 breaking
              API change cannot ship 20 Oct without missing the 14-day partner notice. · outputs/2026-10-11-G01-release-comms/03-release-notes.md

ROUTE         G01 (Release and product communication), because the input is a release scope with ticket
              status plus an audience description, and the job is one message per audience · skills: pm →
              deidentify (deidentify run as a focused review, §04, not a separate subagent) · fallbacks: none

STEPS         1. Confirm what shipped, exclude unmerged — done (01-shipped-confirmed.md)
              2. Breaking changes + known issues first — done (02-breaking-and-known-issues.md)
              3. Release notes + one message per audience — done (03-release-notes.md)
              4. Deidentify on anything public — done as focused review (04-deidentify.md)
              5. Go-live checklist, stop for approval — done (05-go-live-checklist.md); nothing posted/sent

CHECKS        42 rows · 3 failed, all 3 corrected · 0 removed · checked by independent subagent · 07-check.md
              (the 3 failures were claims citing the G01 workflow file, which the checker wasn't given;
              all were corrected by adding the workflows/INDEX.md citation — no factual error vs the inputs)
              Clarity | pass | each audience gets plain language at its reading depth
              Visual | pass | shipped/not-shipped and the date conflict are in tables
              Concise | pass | accountant entries are headline + one line
              Decision | pass | names the LED-504 ship-date call and what would change it
              Honesty | pass | breaking change, known issue, unsent notice and unmerged items all flagged
              Accuracy | pass | every number/date/field traced to the two inputs; API values and date math recomputed

NEEDS YOUR JUDGMENT
              1. LED-504 vs the 14-day notice. The deadline to give notice for a 20 Oct release (6 Oct)
                 has passed and the notice is unsent. Hold LED-504 for 4.2.1, slip its go-live to ≥14
                 days after the notice email (earliest 25 Oct), or get a written waiver. Everything else
                 can ship 20 Oct regardless.
              2. LED-505 ("new firms get default template") is included only in the firm-admin email and
                 left out of the accountant panel, because it affects new firms only. Confirm that's right.
              3. Sender name / sign-off on the partner email (I used "Maya" from the scope file as PM).
              4. Whether the firm-admin monthly email should mention the API change at all for the ~40
                 firms on the partner integration, or leave it entirely to the partner. I left it out.

NEXT ACTIONS  1. Maya + Kwame: decide the LED-504 ship-date question this week (owner: Maya).
              2. Maya: review/approve the four drafts, then send partner notice to Jonas (owner: Maya).
              3. Maya: confirm panel length limits with whoever owns the "What's new" panel (owner: Maya).

ASSUMPTIONS   - Ticket status in release-scope.md is authoritative. G01's Limits line (workflows/INDEX.md)
                reads: "it drafts; you post; it trusts the ticket status you give it."
              - "Maya" is the PM and appropriate sender of the partner email.
              - The three groups in audience.md are the full audience list (the G01 description in
                workflows/INDEX.md says "four audiences"; our input defines three).
              - Non-interactive run: no answer came back to clarifying questions; continued on the inputs.

CONFIDENCE    high — the inputs are self-contained and every claim traces to them; the one limit is that
              the LED-504 ship-date resolution is a human decision I cannot make.
