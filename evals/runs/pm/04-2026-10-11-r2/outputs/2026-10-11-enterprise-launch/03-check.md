# 03 · Check

## Part A — claims table (sourced from the four input documents only)

| Claim (in artifact) | Source line from input | Recomputed / recounted | Verdict |
|---|---|---|---|
| SSO with SAML is a "Must have" | Doc 1: "Must have: SSO with SAML for the pilot customer, audit log, admin roles." | quote matches | holds |
| "Google login is fine for the pilot" | Doc 2: "Their IT lead said Google login is fine for the pilot" | quote matches (phrase) | holds |
| SAML "can wait until we roll out to the whole company next year" | Doc 2: SAML SSO "can wait until we roll out to the whole company next year" | quote matches char-for-char | holds |
| "care most about the audit log, because their compliance review starts in December" | Doc 2: "They care most about the audit log, because their compliance review starts in December." | quote matches (dropped leading "They") | holds |
| SSO SAML = 3 weeks | Doc 3: "SSO with SAML: 3 weeks." | matches | holds |
| Audit log = 2 weeks | Doc 3: "Audit log: 2 weeks." | matches | holds |
| Admin roles = 1 week | Doc 3: "Admin roles: 1 week." | matches | holds |
| Usage dashboard = 2 weeks, "Nice to have" | Doc 1: "Nice to have: usage dashboard."; Doc 3: "Usage dashboard: 2 weeks." | matches | holds |
| Two engineers from 20 October | Doc 3: "Two engineers available from 20 October." | matches | holds |
| "Target launch: 15 November" | Doc 1: "Target launch: 15 November." | matches | holds |
| CEO: "We launch the pilot on 15 November no matter what. Do not slip the date." | Doc 4, verbatim | quote matches char-for-char | holds |
| Sum of all four estimates = 8 engineer-weeks | 3+2+1+2 | = 8 | holds |
| PRD must-haves (SSO+audit+admin) = 6 weeks | 3+2+1 | = 6 | holds |
| Audit + admin (Plan B must-haves) = 3 weeks | 2+1 | = 3 | holds |
| Audit + admin + dashboard = 5 weeks | 2+1+2 | = 5 | holds |
| 20 Oct 2026 is a Tuesday | python date calc (calc.py) | Tuesday | holds |
| 15 Nov 2026 is a Sunday | python date calc | Sunday | holds |
| Window = 26 calendar days = 3.71 weeks | 15 Nov − 20 Oct | 26 days; 26/7 = 3.71 | holds |
| 19 working days = ~3.8 weeks per engineer | Mon–Fri count 20 Oct–15 Nov incl | 19; 19/5 = 3.8 | holds |
| Two engineers ≈ 7.6 engineer-weeks gross | 3.8 × 2 | = 7.6 | holds |
| Fri 13 Nov is last working day before launch | 15 Nov is Sun; 14 Nov is Sat; 13 Nov is Fri | Friday | holds |

**Labelled as inference, not quote (checked that they are marked as such in the artifact):**
- "The CEO fixes the date, not the scope" — inference from Doc 4 naming no feature; marked as inference in files 01 and 02.
- "~6 engineer-weeks usable capacity" — an estimate applying a QA/launch buffer to the 7.6 gross; labelled "call it" / "~" in files 01 and 02, not presented as a given.
- No invented metric, customer, person, or number. No baseline invented.

## Part B — criteria (PM.md §7 + A01/C02 checks)

| Criterion | Pass/Fail | Evidence line |
|---|---|---|
| Clarity | Pass | Plan A / Plan B tables with a one-line recommendation ("Take Plan B. Cut SAML SSO...") |
| Visual | Pass | Two side-by-side build tables + capacity numbers; the call is bold |
| Concise | Pass | Plan is one page (file 02); each plan is a short table + bullets |
| Decision | Pass | "Take Plan B" with "What would reverse this call" section naming the two reversers |
| Honesty | Pass | SSO conflict shown both ways; confidence tags HIGH on each reason; inferences labelled; capacity given as a range not a false precision |
| Accuracy (per claim) | Pass | Claims table above: all quotes and numbers match inputs; all sums recomputed |
| A01: every contradiction shows both sources, not silently resolved | Pass | File 01 conflict table + file 02 both plans; conflict is #1 in judgment list |
| A01: superseded docs not used as current | Pass (n/a) | File 01: no doc is dated, none marked superseding; all four reconciled |
| C02: ranking names the metric it serves | Pass | File 02: "Metric the date serves: compliance review starts in December" |
| C02: items with no evidence flagged, not ranked on enthusiasm | Pass | Usage dashboard labelled "optional/nice to have"; estimates attributed to engineering, not invented |

All criteria pass; no fix-and-recheck loop needed. This is a self check for quality, not a publication grade (PM.md §7) — a separate reviewer should grade before this leaves the folder.
