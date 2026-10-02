<!-- format: locked-v1 -->
# Scoreboard — `launch-minimum`

**Rung:** Observer · **Irreversible:** no · **Last run:** 2026-10-02 · **Golden inputs:** 5
**Owner:** Anurag Jha · **Rollback:** the audit is a document; delete it

> Red rows stay. A scoreboard with no failures is a scoreboard nobody believes.

---

## Result

**3/5 pass · 0 red flags · rung NOT earned.**

The skill's `## VERIFY` block *declares* Advisor. Advisor requires **5 runs, ≥4 pass**. It scored 3.
**Advisor was an assertion, not a measurement.** It is Observer until it is fixed and re-run.

---

## Rung history

| Date | Rung | Why it moved |
|---|---|---|
| 2026-09-30 | Advisor *(claimed)* | Written into the VERIFY block. Never measured |
| **2026-10-02** | **Observer** | First real run: 3/5. Below the ≥4/5 Advisor bar |

---

## Runs

| # | Golden input | Auto 1–5 | Adv 6 | Adv 7 | Result | What broke |
|---:|---|:--:|:--:|:--:|:--:|---|
| 1 | `01-genuinely-ready.md` | 5/5 | ✗ | ✓ | **FAIL** | An unsized fix in the Smallest-fix column |
| 2 | `02-untested-payment.md` | 5/5 | ✓ | ✓ | PASS | — |
| 3 | `03-the-ninth-thing.md` | 5/5 | ✓ | ✗ | **FAIL** | Declared **GO** with two ⚠️ items — breaches its own check 4 |
| 4 | `04-wrong-end-of-the-leak.md` | 5/5 | ✓ | ✓ | PASS | — |
| 5 | `05-nearly-ready.md` | 5/5 | ✓ | ✓ | PASS | — |

**Score:** 3/5 · **Red flags:** 0

Artifacts: [`evals/runs/launch-minimum/`](../runs/launch-minimum/) — unedited, including the two that failed.

---

## The worst failure

**Run 3.** The skill returned:

> **GO 2026-10-02** — six of the eight are real and evidenced; the two gaps are one sentence and one
> screenshot, 90 minutes total

while its own table marked **item 1 (the promise) ⚠️** and **item 5 (the proof) ⚠️**, and its own
`The hole, in funnel order` section listed both as things to do *before* launching.

The skill's check 4 reads: *"No ⚠️ marked as ready — partial counts as missing — fails if a partial is
in the go column."* **It broke its own rule**, in the one place where breaking it is expensive: a
launch verdict.

### The fix

Step 5's go/no-go gate says *"All eight real → launch today"* but never restates that a ⚠️ disqualifies
a GO. Step 1 says it; step 5 does not repeat it, and step 5 is where the verdict is written.

> **Add to step 5:** *A single ⚠️ or ❌ makes the verdict GO &lt;date&gt;, never GO today. The date is
> after the last gap closes, not the same morning.*

Run 1's failure has the same shape: the Output Format gives every row a **Smallest fix** cell, but
check 6 only says *"each **gap** has a version sized in hours"* — so a fix on a passing row was left
unsized. Tighten check 6 to cover every populated cell, not only gaps.

---

## Defects found in the harness, not the skill

Recorded because a scoreboard that only audits the skill is half an audit. **Three of four checks I
wrote were wrong**, and two would have published fabricated failures.

| # | Defect | Effect |
|---:|---|---|
| 1 | Check 2 keyword-matched raw table rows instead of parsing the **Evidence** column | **2 false failures.** Every ✅ row was in fact fully evidenced |
| 2 | Check 3 matched the words "capture" and "proof" inside explanatory prose, not the numbered list items | **1 false failure.** All five runs were in correct funnel order |
| 3 | Check 4 matched the literal string `go today` instead of resolving the date | **Missed the real failure in run 3.** The adversarial reviewer caught it; the auto check did not |
| 4 | Golden input 04's documented expectation said the report must lead with **capture** | **Wrong.** The skill led with **the promise**, which sits earlier in funnel order and was genuinely weak. The skill was more correct than the trap |

Defect 3 is the one that matters: **the mechanical check passed a run that an independent reader
failed.** Auto checks are necessary and are not sufficient, which is why checks 6 and 7 are
adversarial and why the reviewers were told the criterion and nothing about the intent.

---

## Method

- Traps stripped from all five inputs and verified absent before dispatch.
- Five producers, one per input, **fresh context each**, given only the skill and their own input.
  No producer saw another's output, the traps, or the conversation that commissioned the run.
- Auto checks 1–5 run mechanically, actual values recorded beside expected.
- Checks 6 and 7 judged by **two independent reviewers**, each given one written criterion and the
  instruction *"find the failure; you are not being fair, you are being thorough."* Neither was told
  what the skill was for.
- **No run was edited.** Both failures are published as produced.

## Next

1. Apply both fixes to `SKILL.md`.
2. **Re-run the whole set from the top** — any edit to a skill invalidates its rung.
3. Golden input 04's trap section is corrected to match what the skill correctly did.
