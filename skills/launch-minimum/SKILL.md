---
name: launch-minimum
description: The eight things that must exist before you launch anything, and nothing else. Audits what you have, names what is missing, and refuses to let you build a ninth thing until the eight are real. Use before any launch, and again whenever a launch stalls.
disable-model-invocation: false
user-invocable: true
---

# /launch-minimum — the eight things, and nothing else

Most launches fail twice. First they fail by shipping with a hole in them — no way to reach anyone
who liked it, no reason to believe the claim. Then they fail by never shipping at all, because
there was always one more thing to build.

This skill exists to end both arguments. **Eight items. If one is missing you are not ready. If all
eight exist you are, and anything beyond them is procrastination with a changelog.**

## When to Use
- Before launching anything: a product, a feature, a side project, a repo.
- When a launch has stalled and you cannot say why.
- When you catch yourself building a ninth thing.

## Inputs
- What you are launching, in one line.
- Nothing else. The skill interviews for the rest.

---

## The eight

| # | Item | The question it answers | Done when |
|---:|---|---|---|
| **1** | **The promise** | Who is this for and what changes for them? | One sentence, naming a person and a change. No adjectives |
| **2** | **The artifact** | What do they actually get? | It exists and you have used it yourself |
| **3** | **The surface** | Where does it live? | A URL that loads for a stranger |
| **4** | **The capture** | How do you reach them again? | Someone who likes it can give you something you can contact them with |
| **5** | **The proof** | Why should they believe you? | One checkable thing. Not a testimonial |
| **6** | **The path to pay** | How does money move, if it does? | A link that takes a real card, tested with a real card |
| **7** | **The room** | Where do they land afterwards? | A place where a human answers |
| **8** | **The signal** | What number tells you it worked? | One number, defined before launch, that you will actually look at |

---

## Process

### 1. Audit, honestly
Ask about each of the eight in order. For each, demand **evidence rather than intention**:

- Not "we have a landing page" → **what URL, and does it load right now?**
- Not "people can sign up" → **what happens to the email after they type it?**
- Not "we take payments" → **has a real card ever gone through?**

Mark each ✅ exists · ⚠️ partial · ❌ missing. **A ⚠️ is a ❌ for launch purposes.** Something that
half works fails in public at the worst moment.

### 2. Name the hole
Report the missing items in **funnel order**, not difficulty order. The earliest gap is the one that
matters, because every item downstream of a hole is untestable.

> A broken capture makes every post you write spend its traffic once. Fixing the payment page first
> would be fixing the wrong end of a leak.

### 3. The smallest version of each missing item
For each gap, propose the **smallest thing that counts** — not the good version.

| Item | Smallest that counts | What people build instead |
|---|---|---|
| Surface | One page, or a public repo README | A website with five sections |
| Capture | One form, one field | A CRM integration |
| Proof | One screenshot of a real result | A case study PDF |
| Room | One group chat link | A community platform |
| Path to pay | One payment link | A checkout flow |

**The smallest version is not a compromise. It is the version that gets tested this week** instead of
being perfected into next month.

### 4. The ninth-thing check
Ask what else they were planning to build before launching. Then ask, for each: **which of the eight
does this improve?**

If the answer is "none", it is not a launch blocker. Write it on a separate list called `AFTER` and
move on. This step is the whole point of the skill — it is where launches actually get unstuck.

### 5. The go/no-go
State it plainly:

- **All eight real** → launch today. Name the first action and the hour.
- **One or two missing** → name them, size them in hours, and give a date that is this week.
- **Three or more missing** → not a launch, a build. Say so, and sequence them in funnel order.

Never say "nearly ready". It is the phrase that costs the most weeks.

---

## VERIFY
**Rung:** Advisor · **Irreversible?** no — the audit is a document. The launch it recommends is not,
which is why item 6 must be verified with a real transaction before it is marked ✅.

| # | Check | How | Type | Fails if |
|---:|---|---|---|---|
| 1 | All eight assessed | Each has a state and evidence | auto | any item is unassessed |
| 2 | Evidence, not intention | Every ✅ cites a URL, a file, or a transaction | auto | a ✅ rests on "we have one" |
| 3 | Gaps in funnel order | Missing items listed earliest-first | auto | ordered by ease instead |
| 4 | No ⚠️ marked as ready | Partial counts as missing | auto | a partial is in the go column |
| 5 | The ninth-thing list exists | `AFTER` is written, even if empty | auto | absent |
| 6 | Smallest version proposed | Each gap has a version sized in hours | adversarial | a gap is sized in weeks |
| 7 | A real verdict | Go, or a dated plan. Never "nearly" | adversarial | hedged |

**Red flags (any one = rung 0):**
- Marking the path to pay ✅ without a real card having gone through. **Untested payment is the single
  most expensive thing to discover in public.**
- Declaring go with a ⚠️ in the capture item — it means every visitor earned is a visitor lost.

**Rollback:** the audit is a document; delete it. A launch is not reversible, which is why the
verdict is the user's and never the skill's.

---

## Output Format

```markdown
# Launch Minimum — <what you are launching> — <date>

## Verdict
**<GO today | GO <date> | NOT A LAUNCH>** — <one sentence>

## The eight
| # | Item | State | Evidence | Smallest fix |
|---:|---|:--:|---|---|

## The hole, in funnel order
1. <earliest gap> — <hours> — <who>

## AFTER (not launch blockers)
- <everything that improves none of the eight>

## The signal
We will know it worked when **<one number>** does **<one thing>** by **<date>**.
```

## Example Invocation
`/launch-minimum a free repo of PM skills`
`/launch-minimum our pricing page redesign — we keep slipping and I don't know why`
