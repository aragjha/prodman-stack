#!/usr/bin/env python3
"""Build workflows/INDEX.md from workflows/workflows.json, the one home of the workflow index.

Edit the JSON, never the Markdown. Run: python3 workflows/build_index.py
It also checks the index, and refuses to write if a check fails:
  - every workflow has all thirteen fields from the brief, filled
  - IDs are unique and match their family letter
  - every skill from this repo exists at its path; every outside skill has a URL and a fallback
  - tested status is one of the allowed values
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).parent
ROOT = HERE.parent
DATA = json.loads((HERE / "workflows.json").read_text())
TESTED = {"untested", "golden set", "demo run", "blind benchmark"}
FIELDS = ["id", "name", "family", "problem", "inputs", "skills", "steps", "outputs", "checks",
          "setup", "effort", "tested", "example_prompt", "example_result", "limitations"]

errors, seen = [], set()
for w in DATA["workflows"]:
    wid = w.get("id", "?")
    for f in FIELDS:
        if f not in w or w[f] in ("", [], None):
            errors.append(f"{wid}: missing {f}")
    if wid in seen:
        errors.append(f"{wid}: duplicate id")
    seen.add(wid)
    if not wid.startswith(w.get("family", "#")):
        errors.append(f"{wid}: id does not match family {w.get('family')}")
    if w.get("tested", {}).get("status") not in TESTED:
        errors.append(f"{wid}: tested status must be one of {sorted(TESTED)}")
    for s in w.get("skills", []):
        if s.get("source") == "prodman":
            if not (ROOT / s["path"]).exists():
                errors.append(f"{wid}: skill path missing {s['path']}")
        elif not (s.get("url") and s.get("fallback")):
            errors.append(f"{wid}: outside skill {s.get('name')} needs a url and a fallback")
if errors:
    print("INDEX NOT WRITTEN:\n  " + "\n  ".join(errors))
    sys.exit(1)

fam = DATA["families"]
ws = sorted(DATA["workflows"], key=lambda w: w["id"])
tested_counts = {}
for w in ws:
    tested_counts[w["tested"]["status"]] = tested_counts.get(w["tested"]["status"], 0) + 1


def skill_cell(s):
    if s["source"] == "prodman":
        return f"[{s['name']}](../{s['path']})"
    return f"[{s['name']}]({s['url']}) (outside, optional)"


lines = [
    "# Workflow index",
    "",
    f"{len(ws)} PM use cases. Each one names the problem, what you need, the skills it combines, the "
    "steps, how the result is checked, and whether it has actually been tested. The [pm skill](../skills/pm/SKILL.md) "
    "reads this file to route your request; you can also pick a workflow yourself and paste its example prompt.",
    "",
    f"Updated {DATA['updated']}. Generated from [workflows.json](workflows.json) by [build_index.py](build_index.py); "
    "edit the JSON, not this file.",
    "",
    "## How honest the tested column is",
    "| Status | Means | Workflows |",
    "|---|---|---|",
    f"| blind benchmark | Run against other tools on the same task and graded blind | {tested_counts.get('blind benchmark', 0)} |",
    f"| demo run | Run end to end in a fresh session on synthetic inputs, graded by a separate reviewer | {tested_counts.get('demo run', 0)} |",
    f"| golden set | Its main skill has frozen adversarial inputs; the workflow itself has not been run | {tested_counts.get('golden set', 0)} |",
    f"| untested | Written and checked for completeness only. Treat the first run as a test | {tested_counts.get('untested', 0)} |",
    "",
    "Outside skills are optional. Each step that uses one also has a fallback the pm skill runs when it is not installed, "
    "labelled as a fallback in the output.",
    "",
    "## All workflows",
    "| ID | Workflow | Family | Skills | Tested |",
    "|---|---|---|---|---|",
]
for w in ws:
    names = ", ".join(s["name"] for s in w["skills"])
    lines.append(f"| [{w['id']}](#{w['id'].lower()}) | {w['name']}{' ★' if w.get('flagship') else ''} | {fam[w['family']]} | {names} | {w['tested']['status']} |")
lines += ["", "★ flagship demo", ""]

for letter, title in fam.items():
    group = [w for w in ws if w["family"] == letter]
    if not group:
        continue
    lines += [f"## {letter} · {title}", ""]
    for w in group:
        t = w["tested"]
        lines += [
            f"### {w['id']}",
            f"**{w['name']}**{' · flagship demo' if w.get('flagship') else ''}",
            "",
            f"**Problem.** {w['problem']}",
            "",
            "**You need.** " + "; ".join(w["inputs"]) + ".",
            "",
            "**Skills.** " + " → ".join(skill_cell(s) for s in w["skills"]),
            "",
            "**Steps.**",
        ]
        lines += [f"{i}. {s}" for i, s in enumerate(w["steps"], 1)]
        lines += ["", "**You get.** " + "; ".join(w["outputs"]) + ".", "",
                  "**Checked by.** " + "; ".join(w["checks"]) + ".", "",
                  "**Setup.** " + "; ".join(w["setup"]) + ".", "",
                  f"**Effort.** {w['effort']}", "",
                  f"**Tested.** {t['status']}" + (f": {t['evidence']}" if t.get("evidence") else ""), "",
                  "**Example prompt.**", "", "```text", w["example_prompt"], "```", "",
                  f"**Example result.** {w['example_result']}", "",
                  "**Limits.** " + "; ".join(w["limitations"]) + ".", ""]
        for s in w["skills"]:
            if s["source"] != "prodman":
                lines += [f"Fallback for {s['name']}: {s['fallback']}", ""]

(HERE / "INDEX.md").write_text("\n".join(lines))

# ROUTES.md: one line per workflow, so the pm skill can route without reading the whole index
# (INDEX.md is about 40,000 tokens at 56 workflows). The skill reads ROUTES.md to pick, then only
# the chosen workflow's section of INDEX.md.
short = lambda t, n: t if len(t) <= n else t[: n - 1].rsplit(" ", 1)[0] + "…"
routes = ["# Workflow routes", "",
          "One line per workflow. Pick by the decision the user needs, then read only that workflow's section in "
          "[INDEX.md](INDEX.md). Generated by [build_index.py](build_index.py) from [workflows.json](workflows.json).", "",
          "| ID | Workflow | The problem it solves | You need | Tested |", "|---|---|---|---|---|"]
for w in ws:
    routes.append(f"| {w['id']} | {w['name']} | {short(w['problem'], 150)} | {short('; '.join(w['inputs']), 110)} | {w['tested']['status']} |")
(HERE / "ROUTES.md").write_text("\n".join(routes) + "\n")
print(f"INDEX.md written: {len(ws)} workflows, tested {tested_counts}; ROUTES.md written")
