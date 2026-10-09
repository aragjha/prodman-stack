The map is done: `run-05/MAP.md`, with 30 sources in `run-05/SOURCES.md`. Your belief is **contradicted**, and the B2 falsifier fired.

**What I found**
- **B2 ("nobody sells evals to PMs") is false.** At least five courses explicitly name PMs as buyers:
  - Hamel & Shreya, "AI Evals For Engineers & PMs": $4,200, 1,017 reviews
  - Product School: $2,999
  - Tailabs: $399
  - Reforge: membership, starts Oct 21
  - Marily Nika's certification
  - On top of that, Braintrust ($0 / $249 per month) publishes an "Evals for PMs" guide, and the free lenny-skills repo (1.4k★) already ships an AI-evals skill for Claude Code.
- **B1 holds, but weakly.** Only two PMs describe the measurement problem in their own words:
  - a PM who built their own tool after being "blocked by 'Gemini in Google Sheets'"
  - a Google GPM on defining evals per problem
  - Most of the "PMs can't measure" language is seller copy. Reddit was unreachable: the archive APIs refused agents, and I didn't bypass them.
- **"AI skills for PMs" is a free, crowded shelf.** deanpeters has 7.2k★ free. Aakash's free repo leads to a $49 one-time PM OS. That shelf can't carry a paid memory + evals layer.

**Decision: decide now. Go with option B, reframed:** *"The eval layer for PMs who ship AI features: runs in your Claude Code, not another course."*
- Price it against the $399–$4,200 courses, not against $49.
- Take "nobody sells this" off the page.
- Use PM words in the hero ("did the agent answer the question", "ship or hold").

**Before launch**
- **Set a target:** you didn't give me a baseline or target for the landing-page signup rate (row 1.1). Without one, nobody can tell afterwards whether the positioning worked.
- **Constraint for the paid layer:** skills are plain files anyone can copy from git, so the paid memory + evals layer has to be a hosted service, not more skill files.
