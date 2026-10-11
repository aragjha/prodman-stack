# 06 · Check

Every claim traced to an **original input** (never this run's files). Derived values recomputed.

## Part A — claims table

| Claim | Source line (from the input) | Recomputed / recounted | Verdict |
|---|---|---|---|
| GA = Mon 30 Nov, 10 wks from Mon 21 Sep | #06 "10 weeks from 21 September puts general availability on Monday 30 November." | 2026-09-21=Monday; +70 days=2026-11-30=Monday; 70/7=10 | ✓ holds |
| Eng total = 10 weeks | #06 table: 3,1,0.5,1,1.5,2,1 | 3+1+0.5+1+1.5+2+1 = 10 | ✓ holds |
| Agreed musts (R3–R6) = 4 weeks | #06: R3=1, R4=0.5, R5=1, R6=1.5 | 1+0.5+1+1.5 = 4 | ✓ holds |
| Date gap = 30 days | CEO #10 "31 October"; eng #06 "30 November" | 2026-10-31→2026-11-30 = 30 days | ✓ holds |
| 31 Oct is a Saturday | CEO #10 "by 31 October" | 2026-10-31 = Saturday | ✓ holds (noted) |
| CEO: "Only 18% of our invoices are paid late" | #10 verbatim | quoted | ✓ exact |
| Support: "43% of invoices sent through Ledgerly are paid after their due date" | #05 verbatim | quoted | ✓ exact |
| Late-payment tickets 31, up 9 from June | #05 table "31"; note "up from 22 tickets in the same period of June" | 31−22 = 9 | ✓ holds |
| "of the last 3 firms that cancelled, 2 said the reason was chasing late payments by hand" | #04 Owen 09:12 verbatim | 2 of 3 | ✓ exact |
| Lost 2 of 4 Falcon deals | #11 "Falcon came up in 4 of our deals since 1 July. We lost 2 of those 4" | 2 of 4 | ✓ exact |
| "Reminders are now table stakes…" | #11 "Reminders are now table stakes in any deal where Falcon shows up." | quoted | ✓ exact |
| Reminders = 2 wks, reuses scheduler, after engine | #06 "Automatic payment reminders | 2 | reuses the series scheduler, so it can only start after the engine is done" | — | ✓ exact |
| R7 custom rules = 2 wks | #06 in-scope "Custom recurrence rules | R7 | 2" | — | ✓ exact |
| Multi-currency = 2 wks | #06 "Multi currency series | 2"; #04 Kwame "about 2 weeks" | — | ✓ exact |
| Autopay = 5 wks + 3–4 wk security review | #06 "Autopay | 5 | plus an outside security review with 3 to 4 weeks lead time" | — | ✓ exact |
| Series engine R1 = 3 wks | #06 "Series engine… | R1 | 3" | — | ✓ exact |
| Kwame: "does anyone actually need every second Tuesday? custom rules are the gnarliest part of the build" | #04 09:31 verbatim | quoted | ✓ exact |
| Design: 9-control mock "tested badly with 2 internal users" | #12 "Sam's mock has 9 controls on one screen and tested badly with 2 internal users." | 2 users | ✓ exact |
| Interview: "Everyone is billed on the first. Four or five clients are quarterly. That's it." | #08 verbatim | quoted | ✓ exact |
| Interview: chasing "came up first and took most of the call" | #08 Lena obs verbatim | quoted | ✓ exact |
| Preview email: 24h (PRD v2) vs 3 days (design) | #02 R5 "24 hours before"; #12 "3 days before send" | design (1 Sep) newer than PRD v2 (28 Aug) | ✓ holds |
| Success metric: 30% of active firms, ≥1 live series, 60 days after launch, baseline 0 | #02 verbatim | quoted | ✓ exact |
| Pricing: $25 annual / $29 monthly from 1 Oct; included in every plan; pre-1-Oct proposals keep $22 if signed by 31 Oct | #15 verbatim | quoted | ✓ exact |
| Dead pricing: $6 add-on, 0.5% autopay | #07; #15 "do not quote the 0.5% from my July note" | — | ✓ holds |
| v1→v2 changes: autopay out; 30→60 day list | #09 R2/R3; #02 "What changed" | — | ✓ holds |
| Multi-currency wanted by one 40-seat deal, $22/seat, close end of Sept | #03 "40 seat firm", "$22 per seat", "Close target: end of September" | 1 deal | ✓ holds |
| Squad B = 4 engineers, start Mon 21 Sep | #06; #01; #14 | — | ✓ holds |
| Bounced-email handling "not designed yet" | #06 risks verbatim | quoted | ✓ exact |
| Named people/roles (Maya PM, Daniel CEO, Kwame eng, Grace finance, Rosa sales, Tom AE, Owen CS, Ines support, Lena/Sam design, Noor/Felix/Noor eng) | per each doc header | — | ✓ all from inputs |

No number, date, name or quote in the artifacts originates outside the 15 inputs.

## Part B — criteria

A01 "Checked by":
| Check | Verdict | Evidence line |
|---|---|---|
| Every requirement cites its file | **pass** | 02-requirements: each R has an "Also appears in" column with file #s |
| Every contradiction shows both sources, not silently resolved | **pass** | 03-conflicts C1–C5 each have Side A / Side B with file citations |
| Superseded docs not used as current | **pass** | 01-inventory marks v1 #09, #07, #13, #14; scope taken only from PRD v2 |
| No requirement/date/number absent from docs | **pass** | Part A traces all |
| Ranking states the decision it serves | **pass** | 05 header: "the Q4 recurring-invoices plan for the CEO, whose stated goal is Q4 seat expansion" |

PM.md §7 rubric:
| Criterion | Verdict | Evidence |
|---|---|---|
| Clarity | pass | Conflicts table reads in one pass; each has an owner |
| Visual | pass | The 30-day gap and 18%/43% split are in bold tables |
| Concise | pass | Six short files; no padding |
| Decision | pass | 05 makes a recommendation and names what would reverse it (settle C2) |
| Honesty | pass | EUR tagged WEAK (single deal); R7 tagged ZERO evidence; no guardrail metric flagged as missing |
| Accuracy (per claim) | pass | Part A: all exact / holds |

Nothing failed; no re-fix needed. This is a self-check for quality, not a publication grade (PM.md §7:
the author never grades its own work for publication).
