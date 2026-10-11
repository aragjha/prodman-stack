DRAFT, not reviewed by a person

# Check — independent pass (subagent, general-purpose Agent)

Checked: 00-frame.md and 01-handback-draft.md, sentence by sentence, against the request
("Make me a product roadmap", no inputs), workflows/INDEX.md, PM.md, and the `ls` of context/.
The checker did not see the run's notes or intermediate reasoning.

- **Rows:** 26
- **Failed rows:** 5 (rows 7, 19, 20, 22, 23)
- **Corrections applied:** 5 (below), plus 1 the checker could not see from files (subagent-vs-fresh-pass).

## Corrections applied to the hand-back
1. **context wording** (frame + handback) — "only blank templates exist" / "context is empty" overstated:
   `context/` also holds `README.md`, and the templates are not verified blank. Narrowed to:
   "the three live context files are absent; only `*.template.md` files and a `README.md` exist."
2. **step count** (handback) — "Steps 3-6 of C01/C02" overstated C02, which has only steps 1-5.
   Narrowed to "steps 3-6 of C01 / steps 3-5 of C02."
3. **PM.md principle 5** (handback) — "every roadmap item ties to a number" overstated the principle
   ("Tie work to a number someone already watches. If no metric moves, say so..."). Narrowed to the
   principle's own wording.
4. **check attribution** — the draft said "no subagent used." A subagent WAS used (the Agent tool).
   Corrected to "checked by a subagent."
5. The "three questions asked; no answer came back" row (19): the checker flagged it as unsupported by
   the files. It is accurate — three questions were posed via the AskUserQuestion tool and no answer
   returned — but the files did not record them, so the corrected hand-back notes the questions were
   asked interactively (not written to a file).

## Confirmed (the specifically-flagged claims)
- PM.md principle 6 quote exact. pm skill step 1 quote exact. C01/C02 names and required inputs match
  INDEX.md. PM.md principle 5 subject correct (wording narrowed). context/ holds only templates +
  a README (not "only templates").
