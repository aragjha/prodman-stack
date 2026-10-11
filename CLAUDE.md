# ProdMan.AI · prodman-stack

This folder is a toolkit for product managers. Claude Code reads this file at the start of every
session started in this folder, and the line below loads the PM operating guide with it.

@PM.md

## How to work in this folder
- When the user describes a product management problem without naming a skill, invoke the `pm` skill before doing anything else.
  It is registered from `.claude/skills/` (a link to `skills/`). If it is not listed in your skills, read
  [skills/pm/SKILL.md](skills/pm/SKILL.md) and follow it step by step. Do not answer a PM request without it.
- When the user names a skill, read `skills/<name>/SKILL.md` and follow it.
- Read `context/PRODUCT.md`, `context/DECISIONS.md` and `context/CORRECTIONS.md` when they exist. They hold the user's own product context and are never committed.
- Write every run's files to `outputs/<YYYY-MM-DD>-<workflow id>/`. Never edit anything in `evals/golden-sets/`.
- Stop before anything leaves this machine (section 10 of PM.md).
