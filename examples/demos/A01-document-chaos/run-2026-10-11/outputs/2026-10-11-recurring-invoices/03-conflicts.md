# 03 · Conflicts (shown side by side, not silently resolved)

Ordered by how much they move the plan. Newer document noted; owner = who must decide.

## C1 — Launch date: 31 October vs 30 November  ·  owner: CEO + eng
| Side A | Side B |
|---|---|
| **CEO, 9 Sep (#10):** "recurring invoices will be live for all customers by 31 October… The board is counting on it for the Q4 seat expansion story, so please plan to that date." | **Eng estimate, 12 Sep (#06):** 10 weeks from Mon 21 Sep → GA **Mon 30 November**. **Roadmap draft, 16 Sep (#01):** "GA 30 November." **PRD v2, 28 Aug:** "Launch target moves to late November." |
Newer: the estimate and roadmap (12–16 Sep) are newer than the CEO's 31 Oct statement (9 Sep), and
all three post-CEO documents plan to 30 Nov. **Gap = 30 days.** Cutting R7 (2 wks) still lands
~mid-November, past 31 Oct. The board commitment and the build plan do not agree. **Must be decided before the CEO meeting.**

## C2 — Late-payment rate: 18% vs 43%  ·  owner: PM to reconcile, then CEO
| Side A | Side B |
|---|---|
| **CEO, 9 Sep (#10):** "Only 18% of our invoices are paid late, so payment reminders are a nice to have, not a priority this quarter." | **Support summary, 22 Jul (#05):** "Per the July collections dashboard, 43% of invoices sent through Ledgerly are paid after their due date." |
Same metric, two numbers, ~2.4× apart. The CEO's deprioritisation of reminders rests entirely on the
18% figure. If 43% is the true number, the premise is wrong. Neither source shows its derivation here.
**Reconcile before the meeting** — this single number may flip C3.

## C3 — Payment reminders: "not a priority" vs the strongest demand signal in the file  ·  owner: CEO + leadership
| Side A — deprioritise | Side B — overwhelming demand |
|---|---|
| **CEO, 9 Sep (#10):** reminders "a nice to have, not a priority this quarter. Recurring billing is where the seat growth is." **Roadmap (#01):** reminders "parked, not planned." **PRD v2:** non-goal "this year." | **Support (#05):** late-payment chasing is the **#1 ticket theme, 31 tickets**, up from 22 in June. **Churn (#04):** "of the last 3 firms that cancelled, 2 said the reason was chasing late payments by hand." **Sales (#11):** lost 2 of 4 Falcon deals over reminders; "Reminders are now table stakes." **Sales (#03):** the firm we lost in July "went to Falcon… The reason: automatic payment reminders." **Interview (#08):** chasing "came up first and took most of the call." |
Reminders meet the 3-independent-sources bar many times over (support, 2× sales, CS/churn, interview,
competitor). Effort is low: **2 weeks, reuses the series scheduler** (#06) — but can only start after the
engine (R1) ships. The conflict is between a leadership directive and the evidence. **Leadership decides;
lay both sides in front of them with C2.**

## C4 — Multi-currency (EUR) at launch: committed to a prospect vs a non-goal  ·  owner: PM + sales (Rosa/Tom)
| Side A — committed | Side B — out of scope |
|---|---|
| **Sales call, 14 Aug (#03):** "I told them multi currency recurring invoices will be there at launch. They want that in writing before they sign." **Slack, 3 Sep (#04):** Tom: "I told them yes on the 14 August call, I thought it was in." | **PRD v2, 28 Aug (#02):** "Recurring invoices in any currency other than the firm's default currency" = non-goal. **Maya, Slack (#04):** "PRD v2 has other currencies as a non goal for launch." |
A verbal sales commitment contradicts the written PRD. Evidence for EUR is **one 40-seat deal** (close
target end of Sept, $22/seat). Eng cost: **2 weeks** (#06). Decide: honour it (add 2 wks, worsening C1)
or retract it with sales before the proposal goes out.

## C5 — Preview-email lead time: 24 hours vs 3 days  ·  owner: PM/design
| PRD v2, 28 Aug (#02): R5 "24 hours before an invoice is sent." | Design review, **1 Sep** (#12, newer): "preview email goes to the accountant… **3 days before send**, so mistakes can be caught over a weekend." |
Design review is newer and gives a reason. Likely the current intent; PRD v2 just not updated. Low stakes
but a real contradiction — set R5 to one value and update the PRD.

## Resolved by a newer document (no decision needed — recorded so they're not re-litigated)
- **Autopay in v1 (Must) → out, phase 2.** PRD v2 (28 Aug) supersedes v1 (15 Jul) and kickoff (Rosa, 9 Jul). Reason: card storage needs a security review.
- **Upcoming list 30 days → 60 days.** PRD v2 and design review both say 60; v1's 30 is dead.
- **R5 priority Should → Must.** PRD v2 over v1.
- **Pricing: $6 add-on / 0.5% autopay → included in every plan, $25/$29 from 1 Oct.** Grace's 5 Sep update (#15) replaces her 8 Jul note (#07); she says do not quote the 0.5%. Roadmap (#01) already cites the 5 Sep version.
