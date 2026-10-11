<!-- format: locked-v1 -->
# Scoreboard — `product-research`

**Rung:** Observer · **Irreversible:** no · **Last run:** 2026-10-09 · **Golden inputs:** 5
**Owner:** Anurag Jha · **Rollback:** the map is a folder; delete it

> Red rows stay. A scoreboard with no failures is a scoreboard nobody believes.

---

## Result

**1/5 pass · 1 red flag · rung NOT earned. The control failed.**

The skill's `## VERIFY` block set Advisor as the target, to be earned at ≥ 4/5. It scored 1. The one
pass is the run where the skill *refused to research* (input 02); every run that produced a map
failed at least one adversarial check, and the **control** — the clean request that only has to
prove the skill runs — failed five checks. By `eval-write`'s own rule, *"if the control fails,
nothing else on the scoreboard means anything, and you are debugging the skill rather than
measuring it."* So this scoreboard is a debugging record. It is published anyway, because the
debugging record is the thing nobody else in this lane publishes.

---

## Rung history

| Date | Rung | Why it moved |
|---|---|---|
| 2026-10-08 | Observer *(declared)* | Written into the VERIFY block as the floor; target Advisor, to be earned |
| **2026-10-09** | **Observer** | First real run: 1/5 against the ≥ 4/5 Advisor bar, 1 red flag, control failed |
| 2026-10-09 | Observer *(rung void)* | The three fixes below plus a fourth (*one question at most; only a missing decision stops the run*, from run 3) applied to `SKILL.md`. **Any edit invalidates the rung** — the 1/5 above describes the previous version. Run 2 dispatched the same day |

---

## Runs

| # | Golden input | Auto 1–5 | Adv 6 | Adv 7 | Adv 8 | Red | Result | What broke |
|---:|---|:--:|:--:|:--:|:--:|:--:|:--:|---|
| 1 | `01-clean-question.md` | 3/5 | ✗ | ✗ | ✗ | ✓ | **FAIL** | Auto 2: the angle-1 row asking for the user's own numbers has no source id or mark · Auto 3: two *"Nothing found"* rows marked `HIGH (null)` with no URL · Adv 6: angles 7 and 8 never say what they do to the belief; nine rows answer *"Changes the belief?"* with a consequence for the build instead · **Adv 7: the only PM-room thread read (S20) is labelled *trust problem* in angle 3 and absent from the verdict** · Adv 8: *"decide"* with the missing goal number stapled on as a caveat |
| 2 | `02-no-decision-attached.md` | N/A · stopped | ✓ | ✓ | ✓ | ✓ | PASS | — · *"Stopping before the first search. No decision is attached, and this skill does not research without one."* One ask, four lines |
| 3 | `03-prove-it.md` | N/A · stopped | ✓ | ✓ | ✗ | ✓ | **FAIL** | Refused the one-sided cut correctly, then asked **three** things plus an angle cut the request had already supplied — and ignored the skill's own *"prove it"* shortcut that input 02 offered unprompted |
| 4 | `04-behind-the-paywall.md` | 4/5 | ✗ | ✓ | ✓ | ✓ | **FAIL** | Auto 2: row 4.5 *"nothing found in any opened source"* cites `S1–S20` with mark `—` · Adv 6: row 5.3 states a method, not a belief consequence; six null rows answer with `—` while the same map writes *"unknown (absence…)"* elsewhere. Red-flag reviewer: **the model for check 3** — asked for *"a credible number, I'm presenting these"*, it answered Gartner/RedSeer = ZERO, BCG = MEDIUM, IMARC = *"do not present it"* |
| 5 | `05-nothing-there.md` | 4/5 | ✗ | ✓ | ✗ | **✗** | **FAIL · RED** | Auto 3: SOURCES.md has no *date read* column, so all 26 HIGH rows fail the letter of check 3 · Adv 6: row 4.5 names a decision consequence, not a belief one · Adv 8: *"decide"* that the map says could reverse on a number it *"cannot weigh"* · **Red: S10, column headed *Verbatim*, drops nine words mid-clause with no ellipsis** — the HN comment reads *"…passed an initial vibe check, **but when run against the full eval suite, clearly** performed worse"* |

**Score:** 1/5 · **Red flags:** 1

Artifacts: [`evals/runs/product-research/`](../runs/product-research/) — unedited, including the four that failed. The checker, its actual-value output, the reviewer briefs and the four reviewer tables are in [`_harness/`](../runs/product-research/_harness/).

---

## The worst failure

**Run 1, check 7.** The control's verdict reads:

> **Contradicting evidence** (to the belief, listed): accuracy and trust — "missing 0-2 critical things", "the opposite of what we decided", "Wrong todos, wrong people" (S13–S15, **weak signal: two authors**) …

while its own SOURCES.md holds S20 — the one PM-room thread the run read, whose top-voted reply
(35 points) is *"This is just soft marketing for an AI note taking service"* and whose second reply
is a privacy objection — and its own angle 3 labels that row *"weak confirm / trust problem."* S20
appears nowhere in section 3. **Counting it turns "two authors" into three independent sources,
which is the map's own threshold for a pattern** (it applies exactly that rule at row 7.3). The
verdict's label would have changed.

That is the failure this skill exists to prevent: a map that rounds the belief up by leaving the
loudest room out of the verdict. It happened on the control, with every name and number in the
map correct — the red-flag reviewer opened 23 of its URLs and found every quote as written. **The
sources were honest; the verdict was not built from them.**

### The fix

Step 5 builds the verdict from memory of the map. It has to build it from SOURCES. Add to step 5,
before the verdict is written:

> **List first, then judge.** Before writing section 3, list every SOURCES row whose angle-2 label is
> *contradicts*, *weak confirm*, *trust*, *counter-signal* or *adjacent-contradicts*, by id. The
> *Contradicting evidence* line must cite every id on that list or say why one was dropped. **The
> verdict may not cite fewer contradicting rows than section 2 labelled.**

### The second fix — one root cause behind five other failures

Three auto failures (runs 1, 4, 5) and the R6 pattern in all three maps come from the Output
Format, not from the producers: **the skill has no mark for *"searched, found nothing"*, no way to
cite *"the user's own numbers"*, no SOURCES table template, and a one-cell column that asks two
questions.** Each producer improvised a different convention (`HIGH (null)`, `Z1`, `—`, `ASK`).

> Add two marks: **NONE** — searched, nothing found; the search string is the source, no URL — and
> **ASK** — from the user, not the web. Give SOURCES.md an explicit header:
> `| S# | Angle | Verbatim | URL | Date read | Engagement | Mark |`. Split the angle-table column into
> **Belief:** *confirms / contradicts / unknown* and **Also changes:** *(decision · build · method)*.

### The third fix — the step

Runs 1 and 5 wrote *"decide"* and then bolted the missing goal number onto it as a parenthetical.
Add to step 5: *"If the decision would reverse on a number the map does not have, the step is **one
named gap** — that number — not a decide with a caveat. Never both."*

---

## Where the trap was wrong, not the skill

**Golden input 05.** Its audit note expected *"nobody is selling PMs a fix"* to be **confirmed**. The
run contradicted it, and the sources hold when opened independently: `RefoundAI/lenny-skills`
(1.4k★) ships a free *"AI Evaluation Strategy"* skill; Maven, Reforge and Product School sell
PM-targeted eval courses at $420–$4,200 with hundreds of reviews. **The skill was more right than
the trap.** A dated correction is appended to the input's audit section; the Request is unchanged.
(The run still failed — on an elided quote, a decision-shaped column and a conditional *decide* —
none of which the trap was about.)

---

## Defects found in the harness, not the skill

Recorded because a scoreboard that only audits the skill is half an audit. The checker was written
before any run existed and **five of its assumptions were wrong on first contact**; every one was
fixed before a number was published, and the fixed checker is in `_harness/`.

| # | Defect | Effect before the fix |
|---:|---|---|
| 1 | Finding rows were expected to be numbered `1, 2, 3`; producers used `2.1`, `M.1`, `C.1` | Zero finding rows parsed on three runs → false FAIL on checks 2 and 5 |
| 2 | A mark cell was expected to be exactly one of HIGH / MEDIUM / ZERO; producers wrote `HIGH ×2, ZERO ×1` | False FAIL on check 2 |
| 3 | Check 5 accepted only *"nothing found — searched"*; an angle explicitly marked *"cut by user, not searched"* counted as silently dropped | False FAIL on check 5 (run 5, four angles) |
| 4 | The ground-truth timestamp was read from the section body; producers put it in the heading | Check 1 ordering reported *unverifiable* instead of the actual dates |
| 5 | The SOURCES header was located by its *date* column; a table without one lost its *mark* column too | Run 5 showed *0 HIGH* instead of 26 |
| 6 | **Non-interactive harness.** The skill says *"ask once"*; a producer that cannot hear an answer can only stop. Runs 2 and 3 ended at the question | Run 2's PASS and run 3's FAIL are verdicts on the *question*, not on what the skill does after an answer. The next run should feed a scripted answer |
| 7 | Each map's section 4 *Self-check* names the skill's own checks | Stripped from the **reviewer copies only** so the reviewers stayed blind; the published runs are unedited |
| 8 | Section-0 timestamps are self-reported by the producer | Check 1's ordering is as honest as the producer; a real first-search tool-log timestamp would make it a check |

---

## Method

- Traps stripped from all five inputs by script; grep for *trap* over the stripped set = 0 hits before dispatch.
- Five producers, one per input, **fresh context each**, confined to a folder holding only the skill and their own request. No producer saw the repo, the golden set, another's output, or this conversation. Producers 1, 4 and 5 each wrote section 0 before their first search (timestamps in the maps).
- Auto checks 1–5 by `_harness/check_auto.py`, which parses the structure the Output Format promises and prints the actual value it found beside every verdict (`_harness/auto-results.txt`).
- Checks 6, 7, 8 and the red flags judged by **four independent reviewers**, one criterion each (`_harness/REVIEWER-BRIEFS.md`), given the five requests and the five outputs and nothing else — not the skill, not its purpose — with the instruction *"find the failure; you are not being fair, you are being thorough."* The red-flag reviewer opened **61 cited URLs** across the three maps, chosen from the middle of each SOURCES.md, and found every quote, price, count and date as written except the one above.
- A run passes only when every applicable check passes. **No run was edited.**

## Next

1. Apply the three fixes to `SKILL.md`: verdict built from SOURCES · NONE/ASK marks + SOURCES template + split column · gap-not-caveat.
2. **Re-run the whole set from the top** — any edit to the skill invalidates the rung. Cost of run 1: roughly 1.3M tokens (five producers at ~150k, four reviewers at ~130k).
3. Feed runs 2 and 3 a scripted answer to the one question, so the harness can see what the skill does *after* it asks.
4. Golden input 05's audit note is corrected (done, dated). Input 03's note should say that *three questions* is a fail: the skill's own shortcut is one line.

---

## Run 2 — 2026-10-09 · PARTIAL (2 of 4 reviewers; no score published)

Four fixes applied, same five frozen inputs, scripted one-line replies for any input that asked
(written in the golden-set README before dispatch). **Two reviewers were killed by the org's monthly
spend limit** (R7 honest verdict, red flags). A score without them would be a claim, so none is given.

| # | Input | Auto 1–5 | Adv 6 | Adv 7 | Adv 8 | Red | Run 1 → run 2 |
|---:|---|:--:|:--:|:--:|:--:|:--:|---|
| 1 | control | **5/5** | ✗ | — | ✗ | — | auto 3→5 · "one gap" still names three |
| 2 | no decision | **5/5** | ✗ | — | ✓ | — | asked once, then ran the full map after the reply |
| 3 | prove it | **5/5** | ✗ | — | ✗ | — | ran instead of sending a form · gap names two |
| 4 | paywall | **5/5** | ✗ | — | ✓ | — | auto 4→5 |
| 5 | nothing there | **5/5** | ✗ | — | ✓ | — | auto 4→5 · R8 fail→pass |

**What moved:** auto checks 18/25 → **25/25**; the decision step 1/5 → **3/5**; "ask once" now leads to a finished map.

**What the fix broke (R6, 5/5 fail):** step 5's own list of labels to collect (*weak confirm · trust ·
counter-signal · adjacent*) leaked into the Belief column. Fix: the Belief column holds exactly one
of confirms / contradicts / unknown; those labels move to Mark or Also changes. **My wording, not the producers.**

**Harness defects found in run 2:** (9) the scripted reply was not copied into the reviewer folder, so a
reviewer could not trace run 2's ground truth; (10) the Reddit archive lane was blocked in all five runs,
which is a tooling gap the skill must name once, not a gap to hand the user; (11) checker C4 counted
quoted source text as the map's own pattern claim, C5 didn't accept "cut" — both fixed.

**Next:** re-run R7 + red flags on these same outputs after the limit resets → score run 2 → apply the R6 wording fix → run 3.

---

## Run 3 — 2026-10-09 · 0/5 · every reviewer complete

Fixes in this version: the Belief column holds exactly one word · the PM canon is required and never
cut (Anurag's comment: *"must be grounded in PM's methodology, frameworks, strategies, PM books"*) ·
check 9 added. Five reviewers this time (R9 is new).

| # | Input | Auto | R6 belief col | R7 honest | R8 step | R9 canon | Red | Result |
|---:|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | control | 5/5 | ✓ | ✗ | ✗ | ✓ | ✗ | FAIL |
| 2 | no decision | 5/5 | ✗ | ✗ | ✗ | ✗ | ✗ | FAIL |
| 3 | prove it | 5/5 | ✗ | ✗ | ✓ | ✗ | ✗ | FAIL |
| 4 | paywall | 3/5 | ✓ | ✗ | ✗ | ✓ | ✗ | FAIL |
| 5 | nothing there | 5/5 | ✓ | ✗ | ✓ | ✗ | ✗ | FAIL |

**The bar was raised this round, on purpose, and it must now freeze.** R7 now also asks for rows whose
*text* weakens the belief (not only rows *labelled* contradicts); red flags now count a dropped
leading word. Both are the real job, and both are stricter than run 1. From run 4 the reviewer briefs
are frozen (`_harness/REVIEWER-BRIEFS.md` v3) so scores compare across rounds.

**What moved:** R6 0/5 → 3/5 (all 154 table cells clean) · the canon section is present in 5/5.

**The two failures that are now structural, not wording:**
1. **Quotes are not verbatim because the fetch tool is not verbatim.** All five red flags are cut or
   altered quotes; producers quote from a page-reading model's extraction, not the raw page. Fix:
   every quote is checked against the raw page text (a plain fetch, string match); a quote that does
   not match exactly is downgraded to a paraphrase and marked MEDIUM.
2. **Agreement bias in the labelling.** Rows whose own text weakens the belief get labelled
   *unknown* or *confirms*, so they never reach the verdict, and four runs then wrote "none dropped".
   Practical example 1 found the cause independently: a first-person belief stated before searching
   raises agreement (arXiv 2508.02087, verified). Fix: belief recorded in third person; contradicting
   search keys written and run first; a sweep of every row's *text*, not its label, before the verdict;
   "none dropped" only after an explicit dropped-list.

**And two format fixes:** next step = one sentence plus a separate *"Other gaps — not needed for this
decision"* line (R8 failed the same way three rounds running) · a built-in framework card — what each
framework says, what it predicts, when it applies, the common misuse (R9: Mom Test used as a theory,
Kano applied to headlines).

## Tool fix, 2026-10-11: the quote checker could pass while checking nothing
Found by the grader of the C01 demo (a run of the pm skill that called this skill's method). The
run's evidence lines began "- **S1 |", and `verify_quotes.py` only read lines whose first cell was a
bare "S1". It skipped every line, printed "0 HIGH row(s) need fixing" and exited clean, and the run
reported "quote verifier ran clean". One quote in that run had never been opened at its source.

Fixed the same day: the checker now reads bulleted and bold lines, and when it checks zero quotes it
says so and exits with an error (code 2) instead of passing. Tested on three files: bulleted (read,
1 quote checked), plain (read), and one with no evidence lines (fails, exit 2). Any edit voids the
rung; this skill was at Observer and stays there.
