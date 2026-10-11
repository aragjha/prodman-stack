# Run demo3-G01-release-comms

| Field | Value |
|---|---|
| Wall clock | 360 s |
| Turns | 21 |
| Tokens (all, incl. cache) | 923,567 |
| Cost reported by the CLI | 1.6960860000000002 |
| Error | False |

## Final message, unedited

Done. Everything is drafted, checked by an independent pass, and saved under `outputs/2026-10-11-G01-release-comms/`. Nothing has been sent or published.

---

**RESULT** — Release 4.2 notes drafted for all three audiences + a go-live checklist. One thing needs a decision this week: the **LED-504 breaking API change cannot ship on 20 October without missing the 14-day partner-notice agreement**. → `outputs/2026-10-11-G01-release-comms/03-release-notes.md`

**ROUTE** — G01 (Release and product communication), because the input is a release scope with ticket status plus an audience description. Skills: `pm` → `deidentify` (run as a focused review). No fallbacks.

**What each audience gets** (all DRAFT):
- **Firm admins** — monthly email + "What's new" panel: pay-received emails (on by default, opt out in Settings → Notifications), batch-send 50 drafts, overdue filter, CSV export (with the timeout known issue), due-date fix, default template for new firms. *No ticket numbers* (house style).
- **Accountants** — "What's new" panel, each entry a headline + one line: batch send, pay alerts, overdue filter, due-date fix, CSV export. *No jargon, no ticket numbers.*
- **API partner (Jonas)** — changelog entry + direct email: exact field change (`"1250.00"` → `125000`), before/after, "divide by 100," no compat flag, v1 unchanged, and the ≥14-day notice. Ship date left as a field pending your decision.

**Excluded correctly** — LED-507 (recurring pause/resume) and LED-508 (bank-feed matching) were *not merged at freeze*, so they appear nowhere as shipped.

**CHECKS** — 42 fact rows, independent subagent, 3 corrected (all were missing a citation to the G01 workflow file — no factual error vs your inputs), 0 removed. API before/after values, all weekday/date pairs, the 6-Oct notice deadline, the 25-Oct earliest ship, and the 7/2/9 ticket counts were all recomputed and hold. → `07-check.md`

**NEEDS YOUR JUDGMENT**
1. **LED-504 ship date.** Deadline to send 14-day notice for a 20 Oct release was **6 Oct** (passed); notice still unsent. Options: hold LED-504 for 4.2.1 and ship the rest 20 Oct; or send notice now and move its go-live to **≥25 Oct**; or get a written waiver. *Everything else can ship 20 Oct regardless.*
2. LED-505 is in the admin email only (new-firms-only) — confirm that's right.
3. Sender name on the partner email (I used "Maya" from the scope file).
4. Whether the admin email should mention the API change for the ~40 partner-integration firms, or leave it to the partner. I left it out.

**NEXT ACTIONS** — (1) Maya + Kwame decide the LED-504 date this week; (2) Maya reviews the four drafts, then sends Jonas the notice; (3) Maya confirms panel length limits.

**CONFIDENCE** — high; the one limit is that the LED-504 ship-date call is yours to make, not mine.

All files, including the go-live checklist (`05-go-live-checklist.md`), are ready for your review.
