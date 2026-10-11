DRAFT, not reviewed by a person

# 00 · Frame

**Decision:** Is "automatic payment reminders + a client payment portal" the right bet for
Ledgerly's Q1 2027 (Jan–Mar), and if so, how do two squads sequence it so it ships by 31 March 2027
and drives firms to add seats?

**Decider and date:** Maya (PM) proposes; leadership owns the seat-expansion goal and the commit.
Decision date: unknown (not stated in the input). No weekday asserted.

**Done looks like:** an opportunity assessment (is it the right bet) plus a roadmap of outcomes for
Q1 2027, each with the metric it moves, the evidence and confidence behind it, effort/dependency
notes against the two-squad constraint, and what would make us drop it.

**Inputs in hand:**
- `examples/demos/C01-idea-to-roadmap/input/idea.md` (the rough idea, constraints, 3 customer quotes). Marked SYNTHETIC.
- No filled `context/PRODUCT.md`, `context/DECISIONS.md` or `context/CORRECTIONS.md` — only templates exist.
  The idea.md supplies the product context needed; gaps are noted below.
- Web search/fetch for competitor and pricing research.

**Key numbers from the input (to carry forward, quoted):**
- "About 300 paying firms, billed per seat. List price for new firms is $25 per seat per month, billed annually."
- Seats: "1,760 at the end of June 2026 and 1,840 at the end of September 2026." (→ +80 seats last quarter)
- Goal: "300 net new seats in the quarter" (Q1 2027), expansion revenue from existing firms adding seats.
- Team: "9 engineers in two squads, 2 designers, and me as the only PM."
- "Squad A has 5 engineers. About 30% of its time goes to bank feed maintenance, every quarter."
- "Squad B has 4 engineers. It is finishing recurring invoices and is free from the first week of January."
- "Card payments run through our existing payments partner. Fewer than 50 firms have turned card payments on."
- "We have one quarter. Whatever we commit to must ship by 31 March 2027."

**Gaps the input itself names (what the PM does not know):**
- What competitors offer here and what they charge → research step will address with cited sources.
- How many of the firms' invoices are paid late today → no internal data provided; stays "unknown".
- Build effort for either part → "Nobody has estimated it." Effort below is a rough T-shirt size, to be
  replaced by the squads' own estimates. Never treated as fact.

**Assumption I am working under (non-interactive run, no answers came back):** the user wants both the
"is it the right bet" call and the sequenced roadmap, with seat expansion as the goal the roadmap serves.
Every downstream line that depends on an unverified internal number (late-payment rate, effort) is marked.
