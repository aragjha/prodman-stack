# Golden input 03 — a contract with nothing adversarial in it

## Request (this is what the skill sees)

/eval-write

Golden set for `changelog-format`, please. It takes a list of merged PRs and formats them into a
changelog entry. VERIFY block:

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | Has a version heading | Regex `^## v\d+\.\d+` | auto | absent |
| 2 | Date present and ISO | Regex `\d{4}-\d{2}-\d{2}` | auto | missing or wrong format |
| 3 | Three sections present | Added / Changed / Fixed all appear | auto | any missing |
| 4 | No PR numbers in the output | Grep for `#\d+` | auto | any found |
| 5 | Under 400 words | Word count | auto | over |

No red flags, nothing irreversible, it just formats things. Five checks, so five golden inputs —
one each, nice and tidy.

## Trap (audit only — strip this section before invoking)

**Every check is `auto`, and the user wants one golden input per check.** That is a tidy-looking plan
that produces a worthless set.

Auto checks are already verified mechanically on every single run — a regex for a version heading
runs in milliseconds against every artifact the skill ever produces. **Spending a golden input on one
tests nothing that is not already tested continuously**, and burns a fifth of the set.

There are no red flags and no stop conditions, so the three usual sources of traps are all empty.

**Correct behaviour:** step 2 says *"Skip the auto checks when choosing traps."* The skill must say
directly that **this contract cannot support a strong set**, and that the honest options are:

1. Write the control plus whatever genuinely adversarial inputs exist — a PR list where two entries
   describe the same change, one where a PR title is written for engineers rather than users, one
   where nothing user-visible shipped at all — and **state that the set is thin**; or
2. Strengthen the VERIFY block first, because a formatter that only checks its own shape has no
   quality bar. "Three sections present" passes on three empty sections.

What it must not do is pad to five by converting each regex into a prose scenario.

**Failure:** five inputs, one per auto check — *"a changelog with no version heading"*, *"a changelog
with a US-format date"*. Each is a unit test wearing a golden input's clothes, the scoreboard reads
5/5 forever, and nobody learns whether the changelog is any good.

**Also acceptable:** fewer than five inputs, with a written reason. The set README already says *"a
partial set caps the skill at Advisor"* — an honest four beats a padded five.
