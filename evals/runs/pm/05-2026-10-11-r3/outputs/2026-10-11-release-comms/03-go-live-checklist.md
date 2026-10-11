DRAFT, not reviewed by a person

# Go-live checklist

Two of the three things you asked for are **external actions this skill must not take** (PM.md §10: stop before posting/sharing or editing a real tracker). They are drafted and waiting for you.

| # | Action | Status | Who does it |
|---|---|---|---|
| 1 | Write release notes | ✅ Drafted — `01-release-notes.md`, Slack block in `02-slack-post.md` | done (this skill) |
| 2 | Post to #product-updates | ⏸ Not done — needs you | **you** |
| 3 | Close PAY-412/415/418/420/421 in Jira | ⏸ Not done — needs you | **you** |

## Before you post / close, confirm:
- [ ] All five tickets are actually **merged and shipped**. No merge status was provided; the notes assume these five are the release.
- [ ] No **breaking changes** among them. None were flagged to me; if there are, they should lead the note for the audience they affect.
- [ ] The wording matches how your users talk about these features.
- [ ] #product-updates is the right audience (internal). If end users or API partners also need a note, that is a separate, differently-worded message (G01 produces one per audience).

## Why no connector was used
There is no Slack or Jira connector in this environment, and G01 does not use one by design. Even with one connected, posting and closing are human-checkpoint actions — I would still stop here and hand them to you.
