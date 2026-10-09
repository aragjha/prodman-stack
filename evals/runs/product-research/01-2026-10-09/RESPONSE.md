# /product-research — AI meeting notes vs calendar-sync reliability

Ground truth was written and stamped (2026-10-09T04:18Z) before the first search; all eight angles were run, 5, 7 and 8 lightly. The map is in `MAP.md`; every quote, URL, date read and verification mark is in `SOURCES.md` (39 rows: 29 HIGH, 3 MEDIUM, 4 ZERO, 3 explicit "nothing found").

## Verdict

**Belief — "ops leads want AI notes in the scheduling product" — still unknown, leaning weak.** Neither of your falsifiers fired, but neither did the belief get confirmed:

- **F1 (no unprompted public ask):** did not fire — but I found exactly **one**. A Calendly customer, May 2026, asking for meeting notes to live on the contact record: "the idea of searching 15 meetings to find notes is daunting." Calendly's reply: "we don't have the capability to surface meeting notes directly on the contact record." (S19) Ops-specific rooms returned nothing: r/OperationsManagement had zero posts on "notetaker"; three other subreddits were rate-limited; Quora and Capterra were unreachable. That is a weak signal, not evidence.
- **F2 (nobody used it):** dead. Zoom reports AI Companion MAU "over four times year over year" (S9); Calendly's beta did "more than 100,000 meeting recordings" (S1); a 900-company mid-market spend panel shows Granola growing 3x in six months (S11).

**Belief as a route to your goal (seat expansion): contradicted.** Everyone who shipped notes monetises it the same way — **per-seat price, not seat count**: Calendly sells it as the Standard Plus / Teams Plus tier (S3, S4); HubSpot puts it in Sales/Service Hub Professional (S6); Google bundled Gemini and raised every Workspace tier by ~$2/user (S7). No launch or pricing page attributes a single seat-add to notes. That is absence of evidence, and I'm reporting it as such.

## What changed since your QBRs

Calendly shipped **exactly your spec** on 19 Aug 2026 — summary, action items, follow-up email, joins Zoom/Meet/Teams — and its CEO described the market he entered as "a litany of note-takers" (S2). Microsoft Teams now approval-gates external bots by tenant default, GA by end of September 2026 (S25). The NYC Bar wants consent before AI recording (S26); an insurer banned third-party notetakers outright (S27); Otter is in a class action (S28). The bot itself rents for $0.65/hour from Recall.ai (S24). So two engineers would be rebuilding a commodity that the platforms are fencing out, while the half the Calendly user actually asked for — **notes on the record** — is the half nobody has.

## Contradicting evidence, not buried

Accuracy and trust from people who tried it: "missing 0-2 critical things", "the opposite of what we decided", "Wrong todos, wrong people assigned to todos" (S13–S15 — two authors, so labelled weak signal). A ClickUp user who turned on the bundled notetaker and cannot fully turn it off (S29). Bot-style notetakers losing mid-market spend (S11). Calendly aims the feature at sales and marketing, not ops (S2).

## Next step: decide

Walk into planning with the two engineers on **calendar-sync reliability** this cycle — the notes feature cannot be defended as a Q1 seat-expansion bet on anything public. Keep the QBR thread alive at zero engineering cost: Mom-Test the three QBR accounts this week (what did you do after your last five meetings, what did it cost, what do you pay for today), and offer them a Recall-rented pilot of recaps pushed into the booking record. Two of three paying or adding seats turns notes into a **priced add-on spec for Q2** — which is what every shipped case says it is.

**The one input only you can supply before planning:** the angle-1 numbers — Q1 expansion target, current expansion rate, seats per account, and what triggered your last 20 seat-adds. Without the trigger list no feature can be scored on seats.

**Not done:** Reddit ops rooms beyond r/OperationsManagement (rate-limited), G2 reviews, the Gartner usage document, the NYC Bar opinion text. Only the first could move the demand finding.
