# Run demo-G01-release-comms

| Field | Value |
|---|---|
| Wall clock | 218 s |
| Turns | 15 |
| Tokens (all, incl. cache) | 606,942 |
| Cost reported by the CLI | 1.0488745 |
| Error | False |

## Final message, unedited

Done. Everything is DRAFT in `outputs/2026-10-11-release-4.2-comms/`. Nothing was posted or sent.

```
RESULT   Release 4.2 notes + one message per audience + go-live checklist, all DRAFT.
         outputs/2026-10-11-release-4.2-comms/  (02 admins · 03 accountants · 04 API partner · 05 checklist)
ROUTE    G01 Release and product communication · pm → deidentify (lightweight check, not full skill — these are the product's own outward comms, inputs synthetic) · no steps skipped
CHECKS   22 claims checked against the two inputs, all hold · dates/counts recomputed · outputs/2026-10-11-release-4.2-comms/06-check.md
         No unmerged ticket as shipped | pass (LED-507/508 under "NOT in 4.2")
         Breaking change flagged to who it breaks | pass (LED-504 in partner piece only)
         Known issue listed | pass (LED-506 timeout + workaround in every firm-facing piece)
         Nothing posted/sent | pass (all DRAFT)
```

## What each audience gets

- **Firm admins** (monthly email + "What's new" panel): the payment-notification email is **on by default** and changes what their team receives, so it leads with the Settings → Notifications opt-out. Then bulk-send (50), overdue filter, CSV export (with the 10k-row timeout + workaround), and the time-zone due-date fix. No API content, no ticket numbers.
- **Accountants** (panel only, headline-first since most read just the first line): overdue filter and bulk-send up front, then the payment email, CSV export with the workaround, and the fix. No jargon, no API, no ticket numbers.
- **API partner / Jonas** (changelog + direct email): the LED-504 breaking change with exact field names, a before/after table (`"1250.00"` → `125000`), affected endpoints, "no flag," v1 unchanged, and what to change on their side.
- **Left out of firm-facing copy on purpose:** the new-firm default template (new firms only) and LED-507/LED-508 (didn't merge).

## NEEDS YOUR JUDGMENT

1. **The partner notice breaks the 14-day clause.** The agreement requires ≥14 days' written notice before a breaking API change. 14 days before the 20 Oct release was **6 Oct**; the notice still isn't sent, and sending today gives only **9 days**. Pick one: (a) delay the `amount` change to a release ≥14 days after you send notice; (b) get Jonas's written agreement to the shorter window; or (c) ship 4.2 on 20 Oct *without* LED-504 and release the `amount` change separately. The partner email/changelog keep a `[GO-LIVE DATE]` placeholder until you decide — **don't send them as-is.**
2. **LED-506 ships with a known defect** (10k-row export timeout). I listed it with the workaround; confirm you're comfortable shipping it rather than holding it.
3. **Product name on public surfaces.** If the changelog goes to a genuinely public page, run the full `deidentify` skill first. Confirm "4.2.1" → "next update" in firm copy reads right for your house style.

**NEXT ACTIONS** — (1) Maya + agreement owner decide #1 and set the go-live date; (2) Maya approves admin/accountant copy; (3) partner-agreement owner approves the Jonas email before it sends.

**ASSUMPTIONS** — ticket statuses in `release-scope.md` are accurate as of freeze; "4.2.1" = "next update" is acceptable firm-facing phrasing; no filled `context/` files exist so house style comes only from `audience.md`.

**CONFIDENCE** — High on the drafts and the claim checks; the one thing that limits the release is the notice-period decision, which is yours, not a drafting problem.
