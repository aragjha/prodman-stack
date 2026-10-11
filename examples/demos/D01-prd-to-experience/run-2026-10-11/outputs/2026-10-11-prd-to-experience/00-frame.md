# 00 · Frame

**Decision.** What design and engineering build for the client payment portal, starting
Monday — the exact screens, states and flows from invoice email to paid invoice, plus the
decisions only the PM (Maya) can make before work starts.

**Decider and date.** Maya (PM, owner of the PRD). By **Monday 2026-10-12** — the day design and
engineering start. Note: today is **Sunday 2026-10-11**, so the window to answer the open
questions is one day. The weekday/date pair was checked: 2026-10-12 is a Monday.

**Done looks like.**
1. A PRD gap review (requirements without acceptance criteria, ambiguous lines, missing edge/error
   states, missing accessibility).
2. End-to-end user flows including the unhappy paths.
3. Acceptance criteria for every requirement that lacks one.
4. A prototype-ready screen and state specification (every screen, every state, empty + error).
5. A clickable HTML prototype to walk the team through.
6. The questions only the product owner can answer, ordered by what blocks Monday.

**Inputs in hand.**
- `examples/demos/D01-prd-to-experience/input/prd-client-portal.md` — PRD, draft v0.2, synthetic.
- No `context/PRODUCT.md`, `context/DECISIONS.md` or `context/CORRECTIONS.md` (templates only).
- No screenshots of the current product.

**Assumption this run works under.** Non-interactive session; proceeding on the PRD alone and
stating assumptions, rather than blocking on the three context questions. Every line that depends
on a missing input is marked.

**Scope note.** The D01 workflow produces a specification, not visual design. The user also asked
for a *clickable prototype*; this run adds a low-fidelity clickable HTML prototype (grey-box, not
branded visual design) so the team can walk the flow. It is labelled low-fidelity and synthetic.
