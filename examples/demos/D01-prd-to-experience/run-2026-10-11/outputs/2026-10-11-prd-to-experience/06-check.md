# 06 · Check

Self-check for quality (PM.md §7). Claims are traced to the PRD, not to this run's own files.
Source: `examples/demos/D01-prd-to-experience/input/prd-client-portal.md`, read 2026-10-11.

## Part A — claims table
| Claim (where I used it) | Source line from the PRD | Recheck | Verdict |
|---|---|---|---|
| Baseline "34 days", target "25" by "end of March 2027" (05) | line 46: "Baseline: 34 days (August 2026, all firms). Target: 25 days by the end of March 2027." | matches | holds |
| "Fewer than 50 firms have card payments turned on." (01-F) | line 29, same words | char-for-char | holds |
| Link "expires after 30 days"; ">30 days" (02,03,04) | line 34: "Expires after 30 days." | matches | holds |
| "paid within 1 minute" is card-only (02,03,05) | line 37: "the invoice is marked paid within 1 minute" (under R4, card) | matches; R6 has no such line | holds |
| Currencies "USD, CAD, EUR and GBP" (01-B,05) | line 28, same four | matches | holds |
| "The total equals the sum of all open invoices" (01-B) | line 36, R3 criteria | char-for-char | holds |
| "One payment marks every selected invoice paid" (01-B) | line 38, R5 criteria | char-for-char | holds |
| "Firms can issue invoices in USD, CAD, EUR and GBP, and a client's invoices can be in any of these." (01-B) | line 28 | char-for-char | holds |
| "accountants mark invoices paid by hand" (01-A,05) | line 7: "...and accountants mark invoices paid by hand." | matches | holds |
| client "can request a new one by email" on expiry (02,05) | line 34: "the client can request a new one by email" | matches | holds |
| "keep a copy" (02,04) | line 23: "See what they owe, pay it, keep a copy" | char-for-char | holds |
| client "Often reads the invoice email on a phone" (01-D) | line 23, same words | char-for-char (fixed from an earlier pluralised paraphrase) | holds |
| Non-goal "automatic payment reminders" (01,05) | line 17: "Automatic payment reminders (separate initiative)" | same term, lower-cased in prose; used as a label not a quotation | holds |
| Paid invoices "last 12 months" (04) | line 35: "Paid invoices from the last 12 months below" | paraphrase, not quoted | holds |
| Beta "10 card-enabled firms, then all" (05) | line 51: "Beta with 10 firms that already use card payments, then every firm with card payments on." | matches | holds |
| Guardrail baseline "unknown" (05) | line 47: "Baseline: unknown." | matches | holds |
| Open question 2 wording (02,05) | line 59: "Do we notify the accountant when a client pays, or is the 'Paid' status enough?" | matches | holds |
| Owner "Maya (PM)" (00,05) | line 4: "Owner: Maya (PM)." | matches | holds |
| "2026-10-12 is a Monday"; today "Sunday 2026-10-11" (00,05) | computed with python3 (datetime) | 2026-10-12 → Monday; 2026-10-11 → Sunday | holds |
| Contrast floor "4.5:1" (01,03,04) | **not in PRD** | labelled **[proposed]** in every place it appears | holds as a suggestion, not a PRD fact |
| Prototype firm names / invoice numbers / amounts (INV-1043 $640, etc.) | **not in PRD** | labelled SYNTHETIC in the prototype banner and READMEs | holds as synthetic |

No number, date, name or quote in the deliverables traces to anything but the PRD or an explicit
[proposed]/synthetic label.

## Part B — criteria (workflow D01 checks + PM.md §7 rubric)
| Criterion | Pass/fail | Evidence |
|---|---|---|
| Every requirement ends with a testable acceptance criterion | pass | R6 and R10 blanks filled in 03; R1–R5,R7,R9 already had them; edge states given criteria |
| Every gap cites the PRD line it comes from | pass | 01 cites lines 7,17,23,28,29,34–43,54–55,59 |
| Error, empty and edge states covered | pass | 04 lists empty (S1-empty), declined/timeout/abandoned (S3), expired/invalid (S6), partial (S7), pending (S5) |
| Accessibility addressed | pass | 01-D and 04 cross-cutting: mobile-first, keyboard/SR, contrast floor, partner-page dependency |
| Nothing added to scope without being marked a suggestion | pass | all additions tagged **[proposed]**; non-goals restated in 05 |
| Clarity | pass | each file opens with purpose; flows are numbered step lists |
| Visual | pass | tables in 01/03/04; clickable prototype; 05 ordered by blocking |
| Concise | pass | one file per step; prototype is one HTML file |
| Decision | pass | 05 makes the call (per-currency total, status set, manual bank transfer) and flags what's owner-only |
| Honesty | pass | multi-currency conflict shown both ways; guardrail baseline left "unknown"; a11y called "a starting point, not an audit" |
| Accuracy (per claim) | pass | Part A: every claim holds against the PRD or is labelled proposed/synthetic |

**Fix applied during check:** one PRD quote had been pluralised ("often read" vs source "Often
reads"); corrected in 01-D to match the source.

**Self-check caveat (PM.md §7):** this grade was produced by the same run that wrote the artifacts.
It is a quality gate, not a publication sign-off. A separate reviewer should grade before it ships.
