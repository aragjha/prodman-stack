The research pack is ready: `MAP.md` (the map) and `SOURCES.md` (44 sources, each quote verbatim, with URL, date read and a verification mark).

**Before you build slides from it.** You asked for supporting evidence only. I kept the counter-evidence in the map, in rows labelled *contradicts* and listed in section 3, so you choose what goes on a slide. I did not reopen the build decision; nothing I found says "don't build". The goal, belief and falsifier weren't given, so I drafted them and marked them *unconfirmed* in section 0. Correct them if they're wrong.

**What supports the call (slide-ready, all opened and dated):**
- Every major BI vendor ships one, with a paid tier or metered usage:
  - Power BI Copilot is GA on F2+/P1 capacity.
  - ThoughtSpot Spotter sits in its $50 Pro tier.
  - Metabase includes AI in every plan.
  - Mixpanel and Amplitude now call themselves "agent" / "AI analytics" companies.
- Usage is real, though vendor-reported:
  - 52% of ThoughtSpot customers are active on Spotter, and usage is up 133% YoY.
  - About 25% of Amplitude queries come from agents.
- The demand exists. Analysts already use LLMs for SQL; one says it "makes you look like a god to stakeholders".
- Standalone text-to-SQL tools are dying (Vanna archived, Dataherald dormant). The capability is moving inside platforms, which favours building it in-app.

**What leadership may raise (8 rows; worth reading even if they stay off the deck):**
- **Persona.** The pull comes from data teams' *stakeholders*. Data teams themselves voice distrust ("You wouldn't be able to trust the results"). Dataherald's founder found demand in embedded use, not with analysts.
- **Revenue.** No vendor shows revenue from the feature as its own line, and Amplitude bundles it. Through Kano this is a basic: it defends retention but does not earn expansion revenue.
- **Adoption lag.** Governance and legal review slow uptake (3 independent sources).
- **Surface.** Answers are moving into ChatGPT, Claude and Slack via MCP (weak signal).

**How to build it.** Accuracy depends on grounding answers in metric definitions. Raw text-to-SQL scores 84–90%; through a semantic layer it scores 98–100% (dbt benchmark). A short business-semantics doc adds 17–23 points (independent paper). That is both the v1 scope and the positioning: "answers grounded in your metrics", not "an AI assistant".

**One gap before Thursday:** which number this must move (NRR, or weekly active viewers per account), its current baseline, and the target. Without it, nobody can say afterwards whether the build worked.

Could not reach: Reddit (the archive API refuses agents; I did not work around it), the Tableau pricing pages and the Microsoft Fabric forum (both 403). All are marked ZERO, not filled from search snippets.
