DRAFT, not reviewed by a person

# 00 · Frame

**Decision.** Is "automatic payment reminders + a client payment portal" the right bet for Q1 2027
(Jan–Mar), and if so, what roadmap can two squads (9 engineers) actually ship by 31 March 2027 so that
it drives existing firms to add seats?

**Decider and date.** Maya (PM), with leadership sign-off on the seat-expansion goal. Decision date:
unknown (the input does not state one). Work must ship by 31 March 2027.

**Done looks like.** An opportunity assessment (is this the right bet, with competitor + pricing
evidence) plus a sequenced Q1 2027 roadmap of outcomes for Squad A and Squad B, each outcome naming
the metric it moves, the evidence and confidence behind the bet, the effort, dependencies, and what
would make us drop it.

**Inputs in hand.**
- `examples/demos/C01-idea-to-roadmap/input/idea.md` (synthetic demo input, dated 5 Oct 2026): the
  two-part idea, business context, three verbatim customer quotes, and three stated unknowns.
- No filled `context/PRODUCT.md`, `context/DECISIONS.md` or `context/CORRECTIONS.md` exist — only
  templates. So product context comes only from `idea.md`.
- Web search/fetch available for the competitor and pricing research.

**Key facts carried forward (from idea.md, all synthetic):**
- ~300 paying firms, billed per seat; list price for new firms $25 per seat per month, billed annually.
- Seats: 1,760 at end of June 2026; 1,840 at end of September 2026.
- Goal: 300 net new seats in Q1 2027 (existing firms adding seats = expansion revenue).
- Team: 9 engineers in two squads, 2 designers, 1 PM. Squad A = 5 eng (~30% of its time on bank-feed
  maintenance every quarter). Squad B = 4 eng, finishing recurring invoices, free from first week of January.
- Card payments run through an existing payments partner; fewer than 50 firms have card payments on.
- Hard deadline: must ship by 31 March 2027.

**Observation carried into the plan (derived, flagged for your judgment):** the recent quarter added
80 seats (1,760 → 1,840). The 300-seat goal is 3.75× that pace. This is an inference about difficulty,
not a claim from the input; it shapes how aggressive the roadmap must be.

**Unknowns the input names (to be resolved or flagged):** competitor offerings and pricing (research
step), how many of firms' invoices are paid late today (no data provided — gap), and build estimates
(must come from engineers, not the model).
