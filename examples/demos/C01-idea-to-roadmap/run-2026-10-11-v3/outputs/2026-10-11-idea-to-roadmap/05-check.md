DRAFT, not reviewed by a person

# 05 · Independent claim check

**Who checked.** A separate subagent (Agent tool, general-purpose) that did not write the artifacts. It
was given only the checker brief, the original input (`idea.md`), and the final artifacts
(`03-roadmap.md`, `02-bets-and-scoring.md`, `01-research-REPORT.md`, `04-handback-draft.md`). It did not
see my notes or intermediate reasoning. Web claims were re-fetched from their cited URLs; product facts
were checked against `idea.md` only.

## Result
- **Rows in the table: 78** fact-stating sentences (incl. sub-rows 19a, 30a, 31a, 66a).
- **Failed rows: 6**, collapsing to **5 distinct corrections**.
- **Removed: 0** (all failures were corrected in place, none deleted as unsupportable).

## Corrections the check returned, and what I did
| # | Failed claim | Fix applied | File |
|---|---|---|---|
| 1 | Reminders called a "built-in, **free**" feature — neither Xero nor QuickBooks quote mentions price | Removed "free"; now "built-in feature" | 01-research-REPORT.md |
| 2 | Paidnice quote started "see every open invoice…" cutting the leading "can see" without an ellipsis | Changed to the verbatim "can see every open invoice, view statements, and pay one or more invoices at once" | 01-research-REPORT.md |
| 3 | "FreshBooks **bundles a client pay portal** from $23/mo" — the Tech.co page states the $23 price but not a portal | Dropped the FreshBooks portal claim; replaced the portal evidence with Chaser's own payment-portal feature page | 01-research-REPORT.md, 01-research-EVIDENCE.md |
| 4 | "PM.md (section 12 / C02) says effort comes from engineers" — PM.md s12 is the Index, not that statement | Re-cited the C02 workflow note in workflows/INDEX.md: "effort estimates should come from your engineers, not from the model" | 02-bets-and-scoring.md |
| 5 | "Squad B **just finished** recurring invoices" — idea.md says it "is finishing" (ongoing) | Changed to "finishing recurring invoices" | 03-roadmap.md |

## Secondary fix from the automated quote verifier (verify_quotes.py)
The Chaser portal sentence introduced in correction #3 was flagged CUT-START (a mid-sentence marketing
fragment the verifier could not confirm as a sentence boundary). I downgraded it to **second hand** in
the evidence file and paraphrased it in the report (no verbatim quote), so no unverified quote remains.
Final verifier run: **0 HIGH rows need fixing; 0 report quotes untraceable to the evidence file.**

## What the check confirmed exactly (passed)
All core product facts from `idea.md` matched character-for-character or recomputed correctly:
seats 1,760 and 1,840; the derived +80 (1,840 − 1,760) and 3.75× (300 ÷ 80); $7,500/month (300 × 25)
and $90,000/year (300 × 25 × 12); $25/seat; "fewer than 50 firms"; the 300-seat goal; the 31 March 2027
deadline; team composition (9 engineers; Squad A 5 + ~30% bank feeds; Squad B 4 + free first week of
January; 2 designers; 1 PM); the ~3.5 effective engineers (5 × 0.7); and all three customer quotes. The
"862 words" claim in the draft matched `wc -w` at the time; after corrections the report is 872 words
(still under the 900 limit).
