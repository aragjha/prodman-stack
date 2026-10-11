# Claims check brief

You are checking one product management run against its sources. You did not write the run, and
nothing in this brief came from its author: `check.py` built it from a fixed template and filled in
only the file lists below.

## Your files
**Sources.** The only evidence that counts:
- `outputs/2026-10-11-activation-drop/00-request.md`

**Reference files.** Use these only for a claim about PM.md or about a workflow:
- `PM.md`
- `workflows/ROUTES.md`
- `workflows/INDEX.md`

**Files to check.** Everything the run wrote:
- `00-frame.md` at `outputs/2026-10-11-activation-drop/00-frame.md`
- `01-route.md` at `outputs/2026-10-11-activation-drop/01-route.md`
- `02-analysis-plan.md` at `outputs/2026-10-11-activation-drop/02-analysis-plan.md`
- `03-handback-draft.md` at `outputs/2026-10-11-activation-drop/03-handback-draft.md`

**Write your table to:** `outputs/2026-10-11-activation-drop/check.md`

Paths are relative to your working directory. Read no file that is not listed here. Create, edit or
delete no file except the check file.

## What gets a row
Read every file to check, sentence by sentence. Make one row for every sentence that states a fact:
a number, percentage, money amount, date, weekday, count, a comparison word (halved, doubled, most,
all, only, every, never, exactly), a claim about how something works, a claim about what a person or
a document said, a quote, a name, or a citation of a section or a workflow.

Skip these, and only these:
- headings, questions and recommendations;
- an assumption: a sentence that says assume, assumption, guess or hypothesis, or a line under the
  ASSUMPTIONS label (if it also states a fact about the inputs, check that fact);
- a sentence that only describes what the run did or did not do outside its files, for example
  "nothing was posted" (someone else checks those against the session record);
- any line that holds `{{CHECKS}}`, which a script fills in later.

## How to judge a row
1. **Source.** Paste the exact line from a source file, starting with the file name and a colon. A
   claim about PM.md or a workflow takes its line from a reference file. A sentence about this run's
   own files (for example "the plan is in 03-plan.md") takes its line from that file. For any other
   claim, a file the run wrote is never a source. If no line says it, write NONE.
2. **Working.** Recompute every derived value and show the working, with `python3 -c` when it is
   available (never save a script file). For a count, list every counted item with its own pasted
   line, and count an item only when its own line states the thing being counted, not something
   near it. A weekday and a date given together must agree. Write `-` when there is nothing to work
   out.
3. **Verdict.** Does the source say exactly this, and no more? Write `yes` or `no` and nothing else.
   NONE is always `no`. A quote must match its source character for character; a shortened quote
   marks every cut with an ellipsis; a note taker's summary is never a person's quote. A word that
   makes a claim stronger than its source (all for most, approved for fine, one click for a link) is
   a `no`.
   Words in quotation marks claim a person's exact words: the source line must show the same words
   inside quotation marks. Words that appear in the source without quotation marks are a note
   taker's summary, so the verdict is `no` and the Fix drops the quotation marks.
   A web claim needs the page itself: open the cited link and paste its line. A search tool's summary
   is never a source.
   A built file (a prototype, a page, code) is a file to check: every number, label and behaviour it
   shows is a claim, checked against the spec and the sources.
4. **Fix.** For every `no`, write the full sentence the source does support, which replaces the
   whole Claim, or the single word `remove`. Leave Fix empty for a `yes`.

## The check file: exactly this shape
```text
# Check
| # | File | Claim | Source | Working | Verdict | Fix |
|---|---|---|---|---|---|---|
| 1 | 01-brief.md | Four of six firms described chasing payments. | request: 1. Firm A ... | A, C, E, F = 4 | yes | |
```

- One sentence per row, numbered from 1, never merged.
- Copy each Claim exactly as it appears in its file: same words, same punctuation, same markdown
  symbols such as `**` or backticks. A script finds the Claim in the file to apply your Fix, so a
  Claim that does not match stays open and is reported as open.
- File is the file name only, as listed above.
- Inside any cell, write `/` in place of `|` and keep everything on one line.
- Write nothing after the table. The script counts the rows; do not add totals.

When the check file is written, reply with the single word `done`.

<!-- check.py state {"template": "3bdb605b33919fd56ce4f371c49a1e744029c681fba98ba8eb52e23baf8561cb", "draft": "03-handback-draft.md", "sources": ["outputs/2026-10-11-activation-drop/00-request.md"], "references": ["PM.md", "workflows/ROUTES.md", "workflows/INDEX.md"], "files": {"00-frame.md": "7ab980bd8308507a6ae25f1b86afb352932253d2df9f466ee174c29b79297658", "01-route.md": "5d11ba7bc021620f90ebbd909ed4e1bd7e68f4ec3b9367e31fa8f7d7680e605e", "02-analysis-plan.md": "7df8dabb2683cc6127cd3ad4568538ce3196b6a9eb6b167312c3dc5e2d6c4941", "03-handback-draft.md": "9f29e94744b8c29e6062edc87bdbb3fe9ab7ca2593aa862bd25c0e1c471ebfb5"}, "made": "2026-10-11T23:40:25"} -->
