DRAFT, not reviewed by a person

# 07 · Independent check (fresh subagent; read only inputs + final artifact + hand back)

Checker: separate subagent (Agent tool), given only the checker brief, the two input file paths, and
the artifact/hand-back paths. It did not see any intermediate run files.

## Result
- Rows in table: 42 (plus a counts block and a negative check, both passing).
- Failed rows: 3 (#4, #40, #42). (The subagent's summary line said "4" but listed 3; the 3 listed are
  the real failures.) All 3 are the same category: claims/quotes that reference the **G01 workflow
  description**, which lives in `workflows/INDEX.md` — a file the checker was not given, so it could not
  verify them. None is a factual error against `release-scope.md` or `audience.md`.
- Removed: 0.

## All special-attention checks passed
- API before/after: string `"1250.00"` → integer `125000` ✓
- Dates: freeze 9 Oct = Friday ✓; release 20 Oct = Tuesday ✓; today 11 Oct = Sunday ✓; latest 14-day
  notice date = 6 Oct (Tuesday) ✓; earliest go-live if notice sent today = 25 Oct ✓
- Counts: 7 merged, 2 not merged, 9 total ✓
- LED-507 and LED-508 appear only as excluded, never as shipped ✓
- 14-day notice wording quoted char-for-char ✓; >10,000-row export issue ✓; LED-502 on-by-default /
  Settings → Notifications ✓

## Corrections applied (3)
1. Row #4 (03-release-notes.md): added the source — the G01 description in `workflows/INDEX.md` says
   "four audiences need four different messages"; this release has three reader groups.
2. Row #40 (06-handback): same citation added to the assumption about the audience count.
3. Row #42 (06-handback): replaced the clipped quote with the full G01 line and its file path.

## Note
25 October 2026 is a Sunday; no weekday is attached to that date in any artifact, so there is no
mislabel. If one is ever added, it must read "Sunday".
