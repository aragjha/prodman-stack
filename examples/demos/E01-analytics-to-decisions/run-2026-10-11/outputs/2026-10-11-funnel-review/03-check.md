# 03 · Check (E01 step 5)

Claims checked against the **original inputs only** (`metrics-weekly.md`, `events-definitions.md`,
`release-log.md`), not against this run's earlier files.

## Part A — Claims table

| Claim | Source line (pasted from input) | Recomputed / recounted | Verdict |
|---|---|---|---|
| Activation ~62% June–mid-July | rows 06-01..07-20: 33/54, 36/57, 33/53, 34/56, 25/41, 35/55, 39/63, 40/64 | 61.1, 63.2, 62.3, 60.7, 61.0, 63.6, 61.9, 62.5% → avg 62.0% | holds |
| Activation ~41% from week of 07-27 | rows 07-27..09-14: 26/62,27/65,24/61,26/64,28/66,25/63,26/62,27/65 | 41.9,41.5,39.3,40.6,42.4,39.7,41.9,41.5% → avg 41.1% | holds |
| Break is between 07-20 (62.5%) and 07-27 (41.9%) | "2026-07-20 \| 64 ... 40"; "2026-07-27 \| 62 ... 26" | 40/64=62.5%; 26/62=41.9% | holds |
| ~21-point drop | 62.0% − 41.1% | 20.9 ≈ 21 pp | holds |
| Drop persists 6 weeks | weeks 07-27,08-03,08-10,08-17,08-24,08-31,09-07,09-14 all 39–42% | 8 signup-weeks ≥07-27; "6 weeks since" is conservative, all ≥41%-band | holds (understated, fine) |
| Signups healthy 61–66 from 07-27 | 62,65,61,64,66,63,62,65 | min 61, max 66 | holds |
| Invoices sent stable ~7,845–8,042 from 07-27 | 7845,7902,7861,7950,7988,8015,7964,8042 | min 7,845 max 8,042 | holds |
| Seat jump 26 → 61 at week of 08-24 | "2026-08-17 ... 26"; "2026-08-24 ... 61" | 26 then 61 | holds |
| Seat baseline ~27/wk Jul06–Aug17 | 29,26,28,27,25,28,26 | avg = 27.0 | holds |
| Felix recount: "61 ... 29 ... paying ... 32 ... free trial" | events-defs row 23: "61 seats added under the new definition, of which 29 were in paying firms and 32 in firms on a free trial." | 29+32=61 ✓ | holds |
| Paying-only seats 29 vs ~27 baseline = flat | 29 (recount) vs 27.0 baseline | +2, within weekly noise (25–29) | holds |
| Seat def change applies from week of 24 Aug, shipped with 4.1 | events-defs row 20: "Applies from the week of 24 August. The event change shipped with release 4.1" | quoted verbatim | holds |
| 4.0 = invoice template editor rebuild, Tue 2026-07-28 | release-log: "4.0 \| Tuesday 28 July \| Invoice template editor rebuilt with drag and drop blocks... legacy default template is retired" | quoted; 2026-07-28 is a Tuesday ✓ | holds |
| 4.1 = bulk invite, Tue 2026-08-25 | release-log: "4.1 \| Tuesday 25 August \| Bulk invite: firm admins can invite up to 20 teammates at once" | quoted; 2026-08-25 is a Tuesday ✓ | holds |
| 3.9 = signup page 5 fields, Tue 2026-07-14; activation held after | release-log: "3.9 \| Tuesday 14 July \| New signup page: 5 fields instead of 9"; rows 07-13=61.9%, 07-20=62.5% | 2026-07-14 Tuesday ✓; post-3.9 weeks still ~62% | holds |
| 4.0.1 PDF-margin fix in new editor, Tue 2026-08-04 | release-log: "4.0.1 \| Tuesday 4 August \| Fix: PDF margins in the new editor on some browsers" | quoted; 2026-08-04 Tuesday ✓ | holds |
| 06-29 week is holiday volume dip, not rate dip | release-log: "none \| week of 29 June \| No release. Code freeze for the public holiday on Friday 3 July"; row 06-29: 25/41 | 25/41=61.0%, in line with neighbours | holds |
| Review is Tuesday 2026-10-13; today Sunday 2026-10-11 | currentDate 2026-10-11 | 2026-10-11=Sunday, 2026-10-13=Tuesday | holds |
| Activation = first invoice within 7 days of signup | events-defs row 10: "sent their first invoice within 7 days of signing up" | quoted | holds |
| Data labelled synthetic | all three files line 1: "SYNTHETIC: written for a ProdMan.AI demo..." | present on each | holds |

No invented numbers, names, or quotes. Felix and Kwame are the only named people; both appear in the
inputs (`events-definitions.md`, `release-log.md`). No claim sourced to this run's own files.

## Part B — Criteria (PM.md §7 + E01 checks)

| Criterion | Pass/Fail | Evidence line |
|---|---|---|
| Clarity | Pass | Brief opens "One thing broke, and it isn't the one leadership is about to celebrate." |
| Visual | Pass | Diagnosis step-3 table shows the 62%→41% break and the seat jump in one view. |
| Concise | Pass | Decision brief is one page; call stated in the first paragraph. |
| Decision | Pass | "treat the 4.0 editor as the lead cause and run the cheap test; do not report bulk invite as a seat driver" + "What would reverse the call" section. |
| Honesty | Pass | Causes tagged MEDIUM-HIGH/LOW; "correlation with a release is a lead, not proof"; seat read labelled a reporting change. |
| Accuracy (per claim) | Pass | Part A: every number/quote/date recomputed and matches source. |
| E01: every number matches input exactly | Pass | Part A, all rows "holds". |
| E01: definition change caught before read as trend | Pass | Diagnosis step 2 catches the 24-Aug seat redefinition before any seat comparison. |
| E01: causes stated as hypotheses with evidence | Pass | "Candidate causes, ranked" with confidence tags, not asserted facts. |
| E01: experiment has primary, guardrail, stopping rule | Pass | Brief step 5: primary = 7-day activation; guardrail = existing-firm invoices-sent; stopping rule = read after 2 cohorts, escalate if <50%. |

No criterion failed, so no re-fix needed. Self-check only — not a publication grade (PM.md §7).
