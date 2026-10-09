#!/usr/bin/env python3
"""Auto checks 1-5 for `product-research` runs. Records ACTUAL values beside the verdict.

Usage: python3 -I check_auto.py <run-dir> [<run-dir> ...]
A run with no MAP.md (the skill stopped and asked) reports every check as N/A — the adversarial
reviewers decide whether stopping was right. This script never decides that.

Written 2026-10-09 for scoreboard run 1. Lesson carried from launch-minimum's run: keyword
matching on prose produced 3 false results out of 4 checks. So every check here parses the
structure the skill's Output Format promises (sections, tables, columns) and prints what it
actually found, so a human can audit the check instead of trusting it.
"""
import re, sys, pathlib, datetime

MARKS = {"HIGH", "MEDIUM", "ZERO", "NONE", "ASK"}        # NONE = searched, nothing found · ASK = from the user (added for run 2)
MARK_RE = re.compile(r"\b(HIGH|MEDIUM|ZERO|NONE|ASK)\b")  # a mark cell may be composite: "HIGH ×2, ZERO ×1"
ROW_ID = re.compile(r"^(?!#$)[0-9A-Z]{1,3}(\.\d+)?$")      # finding rows are numbered 1, 2.1, or M.1 / C.1 for named-ask angles
SRC_ID = re.compile(r"\b[SZ]\s?\d+\b|#\d+")                # S# = opened source, Z# = a searched-and-empty record
EXPLICIT_EMPTY = re.compile(r"nothing found\s*[-—:]\s*searched|\bcut\b|not searched", re.I)   # any explicit 'cut' is not a silent drop (who may cut is the reviewers' call)
PATTERN_WORDS = re.compile(r"\b(common(ly)?|a trend|trending|most (pms|teams|products|companies|users|people)|the majority)\b", re.I)


def section(text, heading_regex):
    """Return the text of the first '## ...' section whose heading matches, up to the next '## '."""
    m = re.search(r"^(## [^\n]*" + heading_regex + r"[^\n]*\n)(.*?)(?=^## |\Z)", text, re.M | re.S)
    return (m.group(1) + m.group(2)) if m else None   # heading included: timestamps often live there


def table_rows(block):
    rows = []
    for line in block.splitlines():
        if line.strip().startswith("|") and not re.match(r"^\s*\|\s*:?-+", line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def check_run(run):
    run = pathlib.Path(run)
    out = {"run": run.name}
    mp, sp = run / "MAP.md", run / "SOURCES.md"
    if not mp.exists():
        resp = (run / "RESPONSE.md")
        out["mode"] = "STOPPED (no MAP.md)" if resp.exists() else "NO OUTPUT"
        out["response_head"] = resp.read_text()[:300].replace("\n", " ") if resp.exists() else ""
        for k in ("c1", "c2", "c3", "c4", "c5"):
            out[k] = ("N/A", "no map produced")
        return out
    out["mode"] = "MAP"
    MAP = mp.read_text()
    SRC = sp.read_text() if sp.exists() else ""

    # ---- C1 ground truth before search
    gt = section(MAP, r"0\s*·?\s*Ground truth") or ""
    fields = {f: bool(re.search(rf"\*\*{f}[^*]*\*\*\s*:?\s*\S", gt, re.I)) for f in ("Decision", "Belief", "Falsifier")}
    ts = re.search(r"written\s+([0-9]{4}-[0-9]{2}-[0-9]{2}[^,)]*)", gt, re.I)
    # the date-read column, if SOURCES has one; incidental dates inside quotes do not count
    s_all = table_rows(SRC)
    header = next((r for r in s_all if r and re.match(r"^S\s?#?$", r[0].strip(), re.I)), None)  # the S# header row
    date_col = next((i for i, c in enumerate(header) if "date" in c.lower()), None) if header else None
    src_dates = []
    if date_col is not None:
        for r in s_all[1:]:
            if len(r) > date_col:
                m = re.search(r"\b(20[0-9]{2}-[0-9]{2}-[0-9]{2})\b", r[date_col])
                if m: src_dates.append(m.group(1))
    order = ("no timestamp in section 0" if not ts else
             "SOURCES has no date-read column" if date_col is None else
             "date-read column present but empty")
    if ts and src_dates:
        try:
            t0 = datetime.date.fromisoformat(ts.group(1)[:10])
            earliest = min(datetime.date.fromisoformat(d) for d in src_dates)
            order = f"section0={t0} earliest-source={earliest} -> {'ok' if t0 <= earliest else 'SOURCE BEFORE GROUND TRUTH'}"
        except ValueError:
            pass
    c1_ok = all(fields.values())
    out["c1"] = ("PASS" if c1_ok else "FAIL", f"fields present {fields}; order: {order}")

    # ---- C2 every finding cites a source row with a mark
    angles = section(MAP, r"2\s*·?\s*Angles") or ""
    findings = [r for r in table_rows(angles) if len(r) >= 5 and ROW_ID.match(r[0])]
    bad = [r for r in findings if not (SRC_ID.search(r[2]) and MARK_RE.search(r[3].upper()))]
    out["c2"] = ("PASS" if findings and not bad else ("FAIL" if findings else "FAIL (no finding rows parsed)"),
                 f"{len(findings)} finding rows; {len(bad)} without a source id + mark: {[r[1][:40] for r in bad][:5]}")

    # ---- C3 every HIGH in SOURCES has a URL and a date read
    srows = [r for r in s_all[1:] if r and re.match(r"^S\s?\d+$", r[0])]
    mark_col = next((i for i, c in enumerate(header) if c.strip().lower() == "mark"), None) if header else None
    highs = [r for r in srows if mark_col is not None and len(r) > mark_col and "HIGH" in r[mark_col].upper()]
    def has_date(r): return date_col is not None and len(r) > date_col and re.search(r"20[0-9]{2}-[0-9]{2}-[0-9]{2}", r[date_col])
    bad_high = [r for r in highs if not (re.search(r"https?://", " ".join(r)) and has_date(r))]
    why3 = f"{len(srows)} source rows, {len(highs)} HIGH, {len(bad_high)} HIGH without url+date-read"
    if date_col is None: why3 += " (SOURCES has NO date-read column; the skill's format promises one)"
    out["c3"] = ("PASS" if highs and not bad_high else "FAIL", why3)

    # ---- C4 pattern claims cite >=3 sources or say weak signal
    # a pattern claim is the MAP's own sentence, never a quoted source: strip "…" / “…” spans first (run-2 defect)
    def unquoted(l): return re.sub(r"[\"“][^\"”]*[\"”]", "", l)
    lines = [l for l in MAP.splitlines() if PATTERN_WORDS.search(unquoted(l)) and not l.strip().startswith("#")]
    bad_pat = []
    for l in lines:
        n = len(set(re.findall(r"S\s?(\d+)", l)))
        if n < 3 and "weak signal" not in l.lower():
            bad_pat.append(f"[{n} src] {l.strip()[:80]}")
    out["c4"] = ("PASS" if not bad_pat else "FAIL", f"{len(lines)} pattern-claim lines; {len(bad_pat)} with <3 sources and no 'weak signal': {bad_pat[:3]}")

    # ---- C5 every angle has findings or 'nothing found - searched'
    angle_blocks = re.split(r"^### ", angles, flags=re.M)[1:]
    empty = []
    for b in angle_blocks:
        name = b.splitlines()[0][:40]
        has_rows = any(ROW_ID.match(r[0]) for r in table_rows(b) if r)
        says_nothing = EXPLICIT_EMPTY.search(b) is not None
        if not (has_rows or says_nothing):
            empty.append(name)
    out["c5"] = ("PASS" if angle_blocks and not empty else "FAIL", f"{len(angle_blocks)} angle sections; silently empty: {empty}")
    return out


if __name__ == "__main__":
    for d in sys.argv[1:]:
        r = check_run(d)
        print(f"\n=== {r['run']} · {r['mode']}")
        if r.get("response_head"):
            print("  response:", r["response_head"])
        for k in ("c1", "c2", "c3", "c4", "c5"):
            v, why = r[k]
            print(f"  {k.upper():3} {v:28} {why}")
