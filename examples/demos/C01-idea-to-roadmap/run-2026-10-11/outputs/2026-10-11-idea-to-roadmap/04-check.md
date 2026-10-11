# 04 · Check — claims vs. inputs, and criteria

Checked against the original input (`idea.md`) and the cited pages only — never this run's own files.

## Part A — claims table

| Claim (in REPORT/roadmap) | Source line | Recomputed / recounted | Verdict |
|---|---|---|---|
| 1,760 seats end-Jun, 1,840 end-Sep 2026 | idea.md: "1,760 at the end of June 2026 and 1,840 at the end of September 2026" | quoted exactly | holds |
| Last quarter grew +80 seats | derived | 1,840 − 1,760 = 80 | holds |
| Target 300 seats = 3.75× last pace | idea.md: "300 net new seats in the quarter" | 300 ÷ 80 = 3.75 | holds |
| ~300 firms | idea.md: "About 300 paying firms" | quoted ("About") | holds |
| Avg ~6.13 seats/firm (Sep) | derived | 1,840 ÷ 300 = 6.13 | holds |
| ~1.0 seat per firm needed | derived | 300 ÷ 300 = 1.0 | holds |
| $25/seat/month | idea.md: "$25 per seat per month, billed annually" | quoted | holds |
| $7,500 MRR / $90,000 ARR at goal | derived | 300 × 25 = 7,500; × 12 = 90,000 | holds |
| Squad A 3.5 effective engineers | idea.md: "5 engineers. About 30% of its time goes to bank feed maintenance" | 5 × (1 − 0.30) = 3.5 | holds (labelled "about") |
| Squad B 4 engineers, free from week 1 of Jan | idea.md: "Squad B has 4 engineers… free from the first week of January" | quoted | holds |
| <50 firms have card on = 16.7% | idea.md: "Fewer than 50 firms have turned card payments on" | 50 ÷ 300 = 16.7% (stated as "<") | holds |
| Ship by 31 Mar 2027 | idea.md: "Whatever we commit to must ship by 31 March 2027" | quoted | holds |
| Q1 2027 = Jan–Mar | idea.md: "Q1 2027 (January to March)" | quoted | holds |
| Q1 quote: "…move our two new juniors onto Ledgerly instead of the spreadsheet" | idea.md customer 1 | grep: 1 exact match | holds |
| Q2 quote: "one link where they can see everything they owe us and pay it" | idea.md customer 2 | grep: 1 exact match | holds |
| Q3 quote: "nervous about a robot nagging my biggest clients" / "control who gets chased and what it says" | idea.md customer 3 | grep: 1 exact match each | holds |
| "two new juniors" | idea.md customer 1: "our two new juniors" | quoted within Q1 | holds |
| Xero: "Included in every Xero plan, no add-on cost" | S2 Paidnice (quoting Xero Central) | verifier: found verbatim | holds (second hand — labelled) |
| FreshBooks adds users at "$11/mo per user"; reminders + portal included all plans | S1 freshbooks.com/pricing | read on page | holds |
| Chaser $259–$1,169/month, priced by revenue | S4 chaserhq.com/global/pricing | Compact $259, Complete $1,169; "total annual revenue" | holds |
| Leanpay: "Spam filters detect an excessive frequency as harassment." | S6 leanpay.io | read on page, verbatim | holds |
| QuickBooks reminders are built in (no separate add-on) | S3 QuickBooks help | help page describes before/after-due auto reminders in QBO invoicing | holds |
| Bill.com customers "can pay online through multiple methods" | S5 search summary | one source only, page not fetched | holds (labelled "one source only") |

Claims checked: 23. Fixed: 1 (Leanpay quote ellipsis cut mid-sentence → replaced with a whole-sentence
verbatim quote). Removed: 0. Bill.com prices deliberately not relied on (labelled).

## Part B — criteria (PM.md §7 + C01 workflow checks)

**C01 workflow checks**
| Check | Verdict | Evidence line |
|---|---|---|
| Every roadmap item names the outcome and the metric it moves | pass | "Outcome 1 — Firms stop chasing late payers by hand (→ seats)… Metric it moves: net new seats from firms that enable reminders" |
| Every bet cites evidence or is marked an assumption | pass | Bet 1 "demand HIGH, but the seat link is an assumption to test"; Bet 4 "inferred from low attach, no demand data" |
| Sequence respects stated team + time constraints | pass | "Squad B (free from Jan wk 1)… target ship end Feb"; "Squad A (3.5 effective)… may not fully ship by 31 Mar" |
| Outside facts carry a link | pass | Findings table rows each link QuickBooks/Xero/FreshBooks/Chaser/Leanpay |

**PM.md §7 rubric**
| Criterion | Verdict | Evidence line |
|---|---|---|
| Clarity | pass | "The call: Build it, but reframe it… table stakes, not a growth feature" |
| Visual | pass | Scored bets table (Impact/Confidence/Effort) + "The goal, sized honestly" table — key point visible in 60s |
| Concise | pass | REPORT under 900 words (verifier ran clean on it); roadmap is tables, not prose |
| Decision | pass | "Sequence reminders-with-controls first… portal second" + each outcome's "What would make us drop it" |
| Honesty | pass | "low that this feature alone hits 300 net new seats"; effort labelled "NOT a squad estimate"; two baselines marked unknown |
| Accuracy (per claim) | pass | Part A: 23/23 claims trace to a source; all derived values recomputed |

**Artifact-specific:** roadmap lists *outcomes* not features (Outcome 1/2 are stated as outcomes);
research has a counter-evidence section ("What you believed, and what happened to it" + EVIDENCE
"What happened to the belief"). Both present.

No criterion failed. One claim was fixed mid-check (Leanpay quote) and re-verified.
