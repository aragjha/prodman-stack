#!/usr/bin/env python3
"""Check every quoted string in a SOURCES.md against the RAW text of its page.

Why: a page-reading tool hands back a model's version of the page, not the page. Three scoreboard
rounds failed on quotes that were almost, not exactly, verbatim. This script fetches the raw page and
does a plain string match. It decides nothing about meaning; it only answers "is this exact text
there?".

Usage:  python3 verify_quotes.py SOURCES.md
Prints one line per checked quote and exits 1 if any HIGH row has a quote that is not on its page.

Rules it enforces (from SKILL.md, step 3):
  - a quote is the text inside "..." in the Verbatim column; "…" inside a quote splits it into
    fragments, each of which must appear on the page, in order
  - a HIGH row whose quote is not found -> MISMATCH (fix the quote, or downgrade the row to MEDIUM
    and mark the text as a paraphrase)
  - a quote found on the page but starting or ending mid-sentence with no "…" -> CUT
  - a page that cannot be fetched raw -> UNREACHABLE (the row may stay HIGH only if the quote was
    read from an API/JSON endpoint the row names; otherwise downgrade to MEDIUM)
"""
import html, re, sys, unicodedata, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (compatible; prodman-verify/1.0)"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", html.unescape(s))
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def page_text(url: str) -> str | None:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
            raw = r.read().decode("utf-8", "ignore")
    except Exception:
        return None
    raw = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", raw)
    return norm(re.sub(r"(?s)<[^>]+>", " ", raw))


def rows(path: str):
    lines = [l for l in open(path, encoding="utf-8") if l.startswith("|")]
    header = [c.strip().lower() for c in lines[0].strip().strip("|").split("|")]
    col = {name: i for i, name in enumerate(header)}
    for l in lines[2:]:
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if len(c) < len(header) or not re.match(r"^S\d+$", c[0]):
            continue
        yield c[0], c[col.get("verbatim", 2)], c[col.get("url", 3)], c[col.get("mark", len(c) - 1)].upper()


def main(path: str) -> int:
    bad = 0
    cache: dict[str, str | None] = {}
    for sid, verbatim, url_cell, mark in rows(path):
        # a real quote never starts or ends with whitespace; segments that do are the gaps between two quotes
        quotes = [q for q in re.findall(r'"([^"]{12,})"', verbatim) if q == q.strip() and re.search(r"[A-Za-z]{3}", q)]
        url = (re.findall(r"https?://[^\s|)]+", url_cell) or [None])[0]
        if not quotes or not url or mark not in ("HIGH", "MEDIUM"):
            continue
        if url not in cache:
            cache[url] = page_text(url)
        text = cache[url]
        for q in quotes:
            if text is None:
                print(f"{sid}\t{mark}\tUNREACHABLE\t{url}")
                bad += mark == "HIGH"
                break
            frags = [norm(f) for f in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(f.strip()) > 3]
            pos, ok, first, last = 0, True, None, None
            for f in frags:
                i = text.find(f, pos)
                if i < 0:
                    ok = False
                    break
                first = i if first is None else first
                pos = last = i + len(f)
            status = "OK" if ok else "MISMATCH"
            if ok:
                # a quote that starts or ends mid-sentence must say so with an ellipsis
                lead = not q.lstrip().startswith(("…", "...")) and re.search(r"[a-z0-9,]\s$", text[max(0, first - 2):first])
                tail = not q.rstrip().endswith(("…", "...")) and re.match(r"^\s?[a-z0-9]", text[last:last + 2]) and not re.search(r"[.!?:;]$", frags[-1])
                if lead or tail:
                    status = "CUT" + ("-START" if lead else "") + ("-END" if tail else "")
            print(f"{sid}\t{mark}\t{status}\t{q[:70]}")
            bad += status != "OK" and mark == "HIGH"
    print(f"\n{bad} HIGH row(s) need fixing or downgrading")
    return 1 if bad else 0


def crosscheck(doc: str, sources: str) -> int:
    """Every quoted string in doc (MAP.md / RESPONSE.md) must appear verbatim in SOURCES.md."""
    src = norm(open(sources, encoding="utf-8").read())
    bad = 0
    for q in re.findall(r'"([^"]{12,})"', open(doc, encoding="utf-8").read()):
        if q != q.strip() or not re.search(r"[A-Za-z]{3}", q):
            continue
        frags = [norm(f) for f in re.split(r"\s*(?:…|\.\.\.)\s*", q) if len(f.strip()) > 3]
        if not all(f in src for f in frags):
            print(f"NOT-IN-SOURCES\t{q[:80]}")
            bad += 1
    print(f"\n{bad} quote(s) in {doc} not found verbatim in {sources}")
    return 1 if bad else 0


if __name__ == "__main__":
    if sys.argv[1] == "--crosscheck":
        sys.exit(crosscheck(sys.argv[2], sys.argv[3]))
    sys.exit(main(sys.argv[1]))
