#!/usr/bin/env python3
"""The pm skill's claims check, made mechanical (version 4, 2026-10-11).

Runs 1 to 3 of the scoreboard failed the same way: the session that wrote the work also steered its
check. It rewrote the checker's brief, named the answers to expect, chose which files the checker saw,
saved a summary instead of the table, and edited the hand back after the check. This script takes
each of those choices away from the author:

  brief   builds the checker's brief from CHECKER.md, a fixed template, and fills in only file lists;
          records a fingerprint of every file to check
  seal    refuses if any file changed after the brief, counts the checker's own table, applies the
          checker's own fixes, removes email addresses the user did not type, fills the hand back's
          CHECKS line with those counts and prints the final hand back
  tally   prints the counts of a check file without changing anything
  verify  after a run: is every file still as sealed, and (optionally) is a final message identical
          to the sealed hand back

Usage:
  python3 check.py brief  <run-dir> [<input file or folder> ...]
  python3 check.py seal   <run-dir>
  python3 check.py tally  <run-dir>
  python3 check.py verify <run-dir> [<file holding the final message>]

Standard library only. Exit 2 means refused, with the reason printed.
"""
import datetime
import hashlib
import json
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
TEMPLATE = HERE / "CHECKER.md"
REPO = HERE.parent.parent
PLACEHOLDER = "{{CHECKS}}"
REQUEST = "00-request.md"
OWN = {"check-brief.md", "check.md", "seal.txt", "handback.md", REQUEST}
STATE = re.compile(r"\n<!-- check\.py state (\{.*\}) -->\n?$", re.S)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def refuse(msg):
    print(f"REFUSED: {msg}")
    sys.exit(2)


def sha(path):
    return hashlib.sha256(pathlib.Path(path).read_bytes()).hexdigest()


def files_to_check(run):
    out = []
    for p in sorted(run.rglob("*")):
        rel = p.relative_to(run).as_posix()
        if p.is_file() and not any(part.startswith(".") for part in p.relative_to(run).parts) and rel not in OWN:
            out.append(rel)
    return out


def expand(inputs, run):
    out = []
    for raw in inputs:
        p = pathlib.Path(raw).expanduser().resolve()
        if not p.exists():
            refuse(f"input not found: {raw}")
        items = [p] if p.is_file() else sorted(q for q in p.rglob("*") if q.is_file())
        for q in items:
            if any(part.startswith(".") for part in q.parts[-3:]):
                continue
            if run == q or run in q.parents:
                print(f"skipped as a source, the run wrote it: {q}")
                continue
            out.append(str(q))
    return list(dict.fromkeys(out))


def references():
    refs = []
    local = pathlib.Path.cwd() / "PM.md"
    refs.append(local if local.exists() else REPO / "PM.md")
    refs += [REPO / "workflows" / "ROUTES.md", REPO / "workflows" / "INDEX.md"]
    return [str(r.resolve()) for r in refs if r.exists()]


def show(path):
    """A path relative to the working directory when it is inside it, so a published run folder carries
    no machine paths; otherwise absolute."""
    p = pathlib.Path(path).resolve()
    try:
        return p.relative_to(pathlib.Path.cwd().resolve()).as_posix()
    except ValueError:
        return str(p)


def render(run, sources, refs, files):
    text = TEMPLATE.read_text()
    bullets = lambda xs: "\n".join(f"- `{show(x)}`" for x in xs) or "- (none)"
    text = text.replace("{{SOURCES}}", bullets(sources))
    text = text.replace("{{REFERENCES}}", bullets(refs))
    text = text.replace("{{FILES}}", "\n".join(f"- `{f}` at `{show(run / f)}`" for f in files))
    text = text.replace("{{CHECK_FILE}}", show(run / "check.md"))
    return text


def load_state(run):
    brief = run / "check-brief.md"
    if not brief.exists():
        refuse("check-brief.md is missing. Run: python3 check.py brief <run-dir> <inputs>")
    raw = brief.read_text()
    m = STATE.search(raw)
    if not m:
        refuse("check-brief.md has no state line; it was not written by check.py, or it was edited")
    state = json.loads(m.group(1))
    body = raw[: m.start()].rstrip("\n")
    if body != render(run, state["sources"], state["references"], list(state["files"])).rstrip("\n"):
        refuse("check-brief.md was edited after check.py wrote it. Run brief again, then a new check")
    if state["template"] != sha(TEMPLATE):
        refuse("CHECKER.md changed after this brief was built. Run brief again, then a new check")
    return state


def parse_table(path):
    rows = []
    for line in path.read_text().splitlines():
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if not cells or not cells[0].isdigit() or len(cells) < 7:
            continue
        middle = cells[2:-3]
        claim, source = (middle[0], "|".join(middle[1:])) if len(middle) >= 2 else (middle[0] if middle else "", "")
        rows.append({"n": int(cells[0]), "file": cells[1].strip("` "), "claim": claim, "source": source,
                     "working": cells[-3], "verdict": cells[-2], "fix": cells[-1]})
    return rows


def failed(row):
    verdict = row["verdict"].strip().strip("`*").lower()
    return verdict != "yes" or row["source"].strip().strip("`*").upper().startswith("NONE")


def normalise(text):
    """Text without * and backticks and with runs of whitespace collapsed, plus a map back to the original."""
    out, where, space = [], [], False
    for i, ch in enumerate(text):
        if ch in "*`":
            continue
        if ch.isspace():
            if space:
                continue
            out.append(" ")
            where.append(i)
            space = True
            continue
        out.append(ch)
        where.append(i)
        space = False
    return "".join(out), where


def find_spans(text, claim):
    claim = claim.strip()
    if not claim:
        return []
    spans, start = [], 0
    while True:
        i = text.find(claim, start)
        if i < 0:
            break
        spans.append((i, i + len(claim)))
        start = i + len(claim)
    if spans:
        return spans
    norm, where = normalise(text)
    target = normalise(claim)[0].strip()
    start = 0
    while target:
        i = norm.find(target, start)
        if i < 0:
            break
        a, b = where[i], where[i + len(target) - 1] + 1
        while b < len(text) and text[b] in "*`":
            b += 1
        while a > 0 and text[a - 1] in "*`" and (a < 2 or text[a - 2] != "\\"):
            a -= 1
        spans.append((a, b))
        start = i + len(target)
    return spans


def apply_fix(text, claim, fix):
    spans = find_spans(text, claim)
    if not spans:
        return text, False
    removing = fix.strip().strip("`*").lower() == "remove"
    for a, b in reversed(spans):
        if removing:
            # take one neighbouring space with the sentence, so no double or trailing space is left
            if text[b:b + 1] == " ":
                b += 1
            elif a > 0 and text[a - 1] == " ":
                a -= 1
        text = text[:a] + ("" if removing else fix.strip()) + text[b:]
    if removing:
        lines = []
        for line in text.splitlines():
            bare = line.strip()
            if bare and re.fullmatch(r"([-*+]|\d+[.)])", bare):
                continue
            lines.append(re.sub(r"(?<=\S)  +(?=\S)", " ", line))
        text = "\n".join(lines) + "\n"
    return text, True


def cmd_brief(run, inputs):
    if not (run / REQUEST).exists():
        refuse(f"save the request exactly as the user typed it to {run / REQUEST} first")
    for name in ("check.md", "handback.md", "seal.txt"):
        (run / name).unlink(missing_ok=True)
    files = files_to_check(run)
    drafts = [f for f in files if f.endswith("handback-draft.md")]
    if len(drafts) != 1:
        refuse(f"write exactly one hand back draft named NN-handback-draft.md first (found {len(drafts)})")
    if PLACEHOLDER not in (run / drafts[0]).read_text():
        refuse(f"the CHECKS line of {drafts[0]} must hold {PLACEHOLDER}; the seal fills it with the counts")
    sources = [show(run / REQUEST)] + [show(x) for x in expand(inputs, run.resolve())]
    refs = [show(x) for x in references()]
    state = {"template": sha(TEMPLATE), "draft": drafts[0], "sources": sources, "references": refs,
             "files": {f: sha(run / f) for f in files}, "made": datetime.datetime.now().isoformat(timespec="seconds")}
    body = render(run, sources, refs, files)
    (run / "check-brief.md").write_text(body.rstrip("\n") + "\n\n<!-- check.py state " + json.dumps(state) + " -->\n")
    print(f"Brief written: {show(run / 'check-brief.md')} ({len(sources)} sources, {len(files)} files to check)")
    print("Change nothing in the run folder from now until the seal; a changed file voids the check.")
    print("Start the checker with the Agent tool. The prompt is exactly this one line and nothing else:\n")
    print(f"Read {run / 'check-brief.md'} and do exactly what it says.")


def cmd_seal(run):
    state = load_state(run)
    current = files_to_check(run)
    changed = [f for f in state["files"] if not (run / f).exists() or sha(run / f) != state["files"][f]]
    added = [f for f in current if f not in state["files"]]
    if changed or added:
        refuse("the run folder changed after the brief (" + ", ".join(changed + added) +
               "). Nothing may change between the brief and the seal: run brief again, then a new check")
    check = run / "check.md"
    if not check.exists():
        refuse("check.md is missing. The checker writes it, never the author: start the checker again with the same one line prompt")
    rows = parse_table(check)
    if not rows:
        refuse("check.md holds no table rows in the brief's shape. Start the checker again with the same one line prompt")
    texts = {f: (run / f).read_text() for f in state["files"]}
    applied, still_open, corrected, removed = [], [], 0, 0
    bad = [r for r in rows if failed(r)]
    for r in bad:
        f = r["file"]
        if f not in texts:
            match = [k for k in texts if pathlib.Path(k).name == f]
            f = match[0] if len(match) == 1 else None
        if not f or not r["fix"].strip():
            still_open.append((r, "no fix given" if f else "unknown file"))
            continue
        texts[f], ok = apply_fix(texts[f], r["claim"], r["fix"])
        if not ok:
            still_open.append((r, "claim text not found in the file"))
            continue
        if r["fix"].strip().strip("`*").lower() == "remove":
            removed += 1
            applied.append(f"row {r['n']} in {f}: removed")
        else:
            corrected += 1
            applied.append(f"row {r['n']} in {f}: replaced with the checker's wording")
    typed = set(EMAIL.findall((run / REQUEST).read_text()))
    emails = 0
    for f, t in texts.items():
        for e in set(EMAIL.findall(t)) - typed:
            emails += t.count(e)
            t = t.replace(e, "[email removed]")
        texts[f] = t
    for f, t in texts.items():
        if t != (run / f).read_text():
            (run / f).write_text(t)
    line = (f"{len(rows)} claims checked by a separate reader · {len(bad)} failed · {corrected} corrected · "
            f"{removed} removed · {len(still_open)} still open · table: check.md")
    if still_open:
        line += " · open: " + "; ".join(f"row {r['n']} ({r['file']}): {why}" for r, why in still_open)
    if emails:
        line += f" · {emails} email address(es) the user did not type removed"
    handback = texts[state["draft"]].replace(PLACEHOLDER, line)
    (run / "handback.md").write_text(handback)
    seal = [f"sealed {datetime.datetime.now().isoformat(timespec='seconds')} by check.py (pm skill version 4)",
            f"template sha256 {state['template']}", f"brief made {state['made']}",
            f"rows {len(rows)} · failed {len(bad)} · corrected {corrected} · removed {removed} · open {len(still_open)} · emails removed {emails}",
            "", "applied:"] + [f"- {a}" for a in applied] + ["", "open:"] + \
           [f"- row {r['n']} ({r['file']}): {why}" for r, why in still_open] + ["", "files after the seal (sha256):"]
    for f in sorted(set(files_to_check(run)) | {"handback.md", "check.md", "check-brief.md", REQUEST}):
        seal.append(f"{sha(run / f)}  {f}")
    (run / "seal.txt").write_text("\n".join(seal) + "\n")
    print("SEALED. Your final message is everything below this line, copied unchanged, with nothing added before or after it.")
    print(handback.rstrip("\n"))


def cmd_tally(run):
    rows = parse_table(run / "check.md")
    bad = [r for r in rows if failed(r)]
    print(f"rows {len(rows)} · failed {len(bad)}")
    for r in bad:
        print(f"- row {r['n']} ({r['file']}): verdict {r['verdict'] or '(empty)'} · source {r['source'][:60] or '(empty)'} · fix {r['fix'][:60] or '(none)'}")


def cmd_verify(run, message=None):
    seal = run / "seal.txt"
    if not seal.exists():
        refuse("no seal.txt: this run was never sealed")
    problems = []
    for line in seal.read_text().splitlines():
        m = re.fullmatch(r"([0-9a-f]{64})  (.+)", line)
        if m and (not (run / m.group(2)).exists() or sha(run / m.group(2)) != m.group(1)):
            problems.append(f"changed after the seal: {m.group(2)}")
    if message:
        said = pathlib.Path(message).read_text()
        if "## Final message, unedited" in said:
            said = said.split("## Final message, unedited", 1)[1]
        squash = lambda s: re.sub(r"\s+", " ", s).strip()
        if squash(said) != squash((run / "handback.md").read_text()):
            problems.append("the final message is not the sealed hand back")
    print("\n".join(problems) if problems else "verified: every file as sealed" + (", final message identical to handback.md" if message else ""))
    sys.exit(1 if problems else 0)


def main(argv):
    if len(argv) < 3 or argv[1] not in {"brief", "seal", "tally", "verify"}:
        print(__doc__)
        sys.exit(2)
    run = pathlib.Path(argv[2]).expanduser().resolve()
    if not run.is_dir():
        refuse(f"run folder not found: {argv[2]}")
    {"brief": lambda: cmd_brief(run, argv[3:]), "seal": lambda: cmd_seal(run), "tally": lambda: cmd_tally(run),
     "verify": lambda: cmd_verify(run, argv[3] if len(argv) > 3 else None)}[argv[1]]()


if __name__ == "__main__":
    main(sys.argv)
