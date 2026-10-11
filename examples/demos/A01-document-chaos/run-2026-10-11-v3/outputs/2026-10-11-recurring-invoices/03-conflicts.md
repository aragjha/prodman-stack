DRAFT, not reviewed by a person

# 03 · Contradictions, side by side (A01 steps 4–5)

Each conflict shows both sources with the quoted line, which is newer, and who has to decide. None is resolved silently.

## C1 — Launch date: 31 October vs 30 November  ·  owner: Daniel (CEO) + eng
| Side A (CEO's board commitment) | Side B (current PRD + estimate + roadmap) |
|---|---|
| 10 (CEO, **9 Sep**): "I told the board that recurring invoices will be live for all customers by 31 October. The board is counting on it for the Q4 seat expansion story, so please plan to that date." | 02 (PRD v2, 28 Aug): "Launch target moves to late November, pending Kwame's estimate." 06 (eng, **12 Sep**): "10 weeks from 21 September puts general availability on Monday 30 November." 01 (roadmap, **16 Sep**): "GA 30 November." |
| **Newest leadership statement.** | **Newest working estimate** (06, 12 Sep) and newest plan (01, 16 Sep). |

The CEO's date (10) predates the roadmap (01) that already shows 30 November, so this is unresolved, not settled. The gap is ~4 weeks on a 10-week build that starts 21 Sep. Hitting 31 October means cutting scope (see C5/R7) or cutting the date. **This is the top decision for the CEO meeting.**

## C2 — Payment-reminders demand: "18% paid late" vs "43% paid after due date"  ·  owner: leadership + finance
| Side A (CEO) | Side B (support dashboard) |
|---|---|
| 10 (CEO, 9 Sep): "Only 18% of our invoices are paid late, so payment reminders are a nice to have, not a priority this quarter." | 05 (support, 22 Jul): "Per the July collections dashboard, 43% of invoices sent through Ledgerly are paid after their due date." |

Two different figures for the same thing (invoices paid late). The CEO's de-prioritisation of reminders rests on the lower number. Whichever is right, the priority call is leadership's — but the CEO should see the 43% figure before the meeting. Reminders are also the strongest demand theme and a competitive gap (see [04-themes.md](04-themes.md)).

## C3 — Multi-currency (EUR) at launch: sales promise vs PRD non-goal  ·  owner: Maya (PM) + sales/leadership
| Side A (sales commitment) | Side B (PRD v2) |
|---|---|
| 03 (sales, 14 Aug): "they need recurring invoices in EUR as well as USD from day one… I told them multi currency recurring invoices will be there at launch. They want that in writing before they sign." | 02 (PRD v2, 28 Aug): non-goal — "Recurring invoices in any currency other than the firm's default currency." |
| 04 (Slack, 3 Sep) Tom: "I told them yes on the 14 August call, I thought it was in." Maya: "PRD v2 has other currencies as a non goal for launch." | 06 (eng): "Multi currency series — 2 weeks" (not in scope). |

A written commitment was made to a 40-seat prospect (close target end of Sept) that the current PRD explicitly excludes. Decide before anything is sent to that prospect. Adding EUR is +2 weeks (06), which collides with C1.

## C4 — Preview-email timing: 24 hours vs 3 days  ·  owner: Maya (PM)
| Side A (PRD v2) | Side B (design review, newer) |
|---|---|
| 02 (28 Aug) R5: "preview email 24 hours before an invoice is sent." | 12 (**1 Sep**): "The preview email goes to the accountant… 3 days before send, so mistakes can be caught over a weekend." |

Design review is newer and gives a reason (weekend catch). Low stakes, but the PRD and the build spec currently disagree. Confirm which the team builds.

## C5 — Custom recurrence rules (R7): in scope but no evidence or demand  ·  owner: Maya (PM)
| In scope | Against |
|---|---|
| 02 & 09 R7 "Should"; 06 estimates 2 weeks. | 04 (Slack) Kwame: "does anyone actually need every second Tuesday? custom rules are the gnarliest part of the build." Maya: "it's been in since v1, I'll find out where it came from." 12 (design): rules builder "tested badly with 2 internal users." 08 (interview): "Everyone is billed on the first. Four or five clients are quarterly. That's it." |

R7's origin is unknown (Maya, 04), one interviewed customer does not need it, and it tested badly — yet it is the second-largest line in the estimate (2 wks). It is the obvious scope cut if C1 forces 31 October. See [05-build-first.md](05-build-first.md).

## Resolved by a newer document (no decision needed)
- **Pricing — add-on vs included:** 07 ($6/firm add-on, 8 Jul) is replaced by 15 (5 Sep): "included in every plan. No add on." Roadmap 01 already reflects this. *Resolved.*
- **Autopay at launch:** v1 R2 Must (09) → out, phase 2 Q1 2027 (02, 01). *Resolved.*
- **Upcoming list window:** 30 days (v1 09) → 60 days (02, 12). *Resolved.*
- **Autopay pricing:** 0.5%/transaction (07) withdrawn — 15: "do not quote the 0.5% from my July note." *Resolved.*
