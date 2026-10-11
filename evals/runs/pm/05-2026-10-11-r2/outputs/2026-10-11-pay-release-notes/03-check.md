# 03 · Check (pm skill step 5)

## Part A — claims table

Source = the five ticket lines in the original request. No number, date, person, company, or price
appears in the artifact, so the claims to check are the factual descriptions of each ticket.

| Claim in draft | Source line (original input) | Verdict |
|---|---|---|
| PAY-412: export invoices as CSV from the invoice list | "Invoices can now be exported as CSV from the invoice list" | Matches |
| PAY-415: due dates showed in UTC, now in the firm's time zone | "Fixed: due dates showed in UTC instead of the firm's time zone" | Matches |
| PAY-418: payment reminder emails include a "pay now" link | "Payment reminder emails now include a 'pay now' link" | Matches |
| PAY-420: admins can set a default payment term per client | "Admins can set a default payment term per client" | Matches |
| PAY-421: invoice search ignored accented client names, now matches | "Fixed: the invoice search ignored client names with accents" | Matches |

- No invented metric, baseline, target, date, or customer appears in the draft. ✓
- "one click" (PAY-418 Slack line) is a plain restatement of a link, not a claim beyond the source. Kept as mild phrasing.
- No ticket was added, dropped, or renamed. 5 in, 5 out: 412, 415, 418, 420, 421. ✓

## Part B — criteria (PM.md §7 + G01 checks)

| Criterion | Pass/Fail | Evidence |
|---|---|---|
| Clarity | Pass | Grouped under "New" / "Fixed"; one line per item in plain words |
| Visual | Pass | Key points scannable as bullets/table; New vs Fixed split visible at a glance |
| Concise | Pass | One line per ticket in the Slack post; nothing padded |
| Decision | Pass | Artifact states what ships and flags unconfirmed status; the call (post + close) is queued for the human |
| Honesty | Pass | Ship status marked "assumed per request"; known issues "none supplied"; de-id screen recorded |
| Accuracy | Pass | All five claims match source exactly (Part A) |

**G01-specific checks:**
- No unmerged ticket presented as shipped → status explicitly marked "assumed — confirm". ✓
- Breaking changes flagged → none exist; stated. ✓
- Known issues listed → none supplied; stated. ✓
- Nothing posted, sent, or closed → confirmed; see 04-go-live.md. ✓
