# Outside resources

These are the 15 outside skill collections and connectors that the ProdMan.AI toolkit points product managers to, each checked at source on 11 October 2026.

**Task families:** A documentation, B research, C roadmapping and planning, D design and UX, E analytics and success metrics, F evaluations, G delivery and communication, H career and portfolio.

| Resource | What it does for a PM | Families | How to install | Licence | Score out of 100 | Tested by us |
|---|---|---|---|---|---|---|
| [Anthropic knowledge work plugins](https://github.com/anthropics/knowledge-work-plugins) | Writes specs, updates the roadmap, plans sprints, drafts stakeholder updates, synthesizes research, reviews metrics and critiques designs. | A B C D E G | `claude plugin marketplace add anthropics/knowledge-work-plugins` then `claude plugin install product-management@knowledge-work-plugins`, plus `design@knowledge-work-plugins` and `data@knowledge-work-plugins` for design and data work | Apache 2.0 | 94 | Not benchmarked |
| [Atlassian MCP server](https://github.com/atlassian/atlassian-mcp-server) | Lets Claude read and update Jira and Confluence, and turns a spec into a backlog, meeting notes into tasks and Jira into a status report. | A C G | `claude mcp add --transport http atlassian https://mcp.atlassian.com/v2/mcp` then sign in with `/mcp` | Apache 2.0 for the repository; the hosted service runs under Atlassian's terms | 91 | Not benchmarked |
| [Awesome PM Skills](https://github.com/menkesu/awesome-pm-skills) by Udi Menkes | Runs 25 workflows built from Lenny's Podcast, from specs and interviews to metrics, AI eval plans and career decisions, and grades the work you already have. | A B C E F G H | `/plugin marketplace add menkesu/awesome-pm-skills` then `/plugin install awesome-pm-skills@awesome-pm-skills` | MIT; the podcast quotes keep their owners' rights | 89 | Not benchmarked |
| [Amplitude MCP server and plugin](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) | Lets Claude query your Amplitude data to find opportunities, feedback themes, experiment results and the places where users struggle. | B D E | `claude plugin install amplitude@claude-plugins-official` | MIT for the plugin; the hosted service runs under Amplitude's terms | 89 | Not benchmarked |
| [PM Skills Marketplace](https://github.com/phuryn/pm-skills) by Pawel Huryn | Gives Claude 69 PM skills and 42 chained workflows for discovery, strategy, PRDs, OKRs, A/B test analysis and launch. | A B C D E G H | `claude plugin marketplace add phuryn/pm-skills` then `claude plugin install pm-execution@pm-skills` | MIT | 87 | Benchmarked: one research skill, 17 of 25 |
| [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills) by Dean Peters | Teaches Claude 77 PM methods with the reasoning behind them, from PRDs and user stories to roadmaps, SaaS metrics and interview practice. | A B C D E G H | `/plugin marketplace add deanpeters/Product-Manager-Skills` then `/plugin install prd-development@pm-skills` | CC BY-NC-SA 4.0: free to use at work, not to resell | 86 | Benchmarked: one research skill, 17 of 25 |
| [PM skills](https://github.com/product-on-purpose/pm-skills) by Product on Purpose | Covers 68 skills from discovery to measurement, including acceptance criteria, analytics event specs and design sprints, with a shared project memory file. | A B C D E F G | `/plugin marketplace add product-on-purpose/agent-plugins` then `/plugin install pm-skills@product-on-purpose` | Apache 2.0 | 86 | Benchmarked: one research skill, 19 of 25 |
| [Linear MCP server](https://linear.app/docs/mcp) | Lets Claude find, create and update Linear issues, projects and comments. | C G | `claude mcp add --transport http linear-server https://mcp.linear.app/mcp` then sign in with `/mcp` | Hosted service under Linear's terms | 86 | Not benchmarked |
| [Notion MCP server](https://developers.notion.com/docs/mcp) | Lets Claude search, read and update your Notion pages and databases. | A C | `claude mcp add --transport http notion https://mcp.notion.com/mcp` then sign in with `/mcp` | Hosted service under Notion's terms | 86 | Not benchmarked |
| [PM Pilot](https://github.com/mshadmanrahman/pm-pilot) by Shadman Rahman | Writes decision briefs in which every claim carries its source, synthesizes interviews, and drafts PRDs, weekly status reports and meeting prep. | A B C G | `claude plugin marketplace add mshadmanrahman/pm-pilot` then `claude plugin install pm-core@pm-pilot` | MIT | 85 | Benchmarked: one research skill, 21 of 25 |
| [Mixpanel MCP server](https://docs.mixpanel.com/docs/features/mcp) | Lets Claude run Mixpanel queries and reports and manage dashboards, cohorts, experiments and feature flags. | E | `claude mcp add --transport http mixpanel https://mcp.mixpanel.com/mcp` then sign in with `/mcp` | Hosted service under Mixpanel's terms | 83 | Not benchmarked |
| [Anthropic example skills](https://github.com/anthropics/skills) | `internal-comms` writes status reports and leadership updates in your company's format, and `skill-creator` builds your own skills and tests them with evals. | F G | Already in the Claude apps on paid plans. In Claude Code: `/plugin marketplace add anthropics/skills` then `/plugin install example-skills@anthropic-agent-skills` | Apache 2.0 for these two skills | 79 | Not benchmarked |
| [PostHog MCP server](https://posthog.com/docs/model-context-protocol) | Lets Claude query PostHog analytics and SQL and manage dashboards, experiments, feature flags and surveys. | E | `npx @posthog/wizard@latest mcp add` | MIT for the code; the hosted service runs under PostHog's terms | 78 | Not benchmarked |
| [Eval skills](https://github.com/ai-evals-course/evals-skills) by Shreya Shankar and Hamel Husain | Walks you through evaluating an AI feature: reading real outputs, naming the failure modes, then building and checking LLM judges. | F | `npx skills add https://github.com/ai-evals-course/evals-skills` | Apache 2.0 | 76 | Not benchmarked |
| [Figma MCP server and plugin](https://github.com/figma/mcp-server-guide) | Lets Claude read design context, draw FigJam diagrams and turn a PRD into a project plan board, though View and Collab seats get only 6 calls a month. | C D | `claude plugin install figma@claude-plugins-official` | Figma Developer Terms; no open source licence | 71 | Not benchmarked |

**Word, PowerPoint, Excel and PDF files.** The Claude apps make these on paid plans with Anthropic's own document skills. Those skills are source available, not open source, and their licence forbids copying them, so use them inside Claude and never copy their folders. That is why they are not in the table.

Our own five skills come first where they fit: `product-research` for research, `eval-write` for evaluations, `launch-minimum` for launch readiness, and `portfolio-from-work` with `deidentify` for portfolio work. The table above covers the rest.

## How we chose

**Three checks came first, and a fail cut a resource whatever its score.**
1. **Licence.** We read the licence file at source on 11 October 2026 and kept a resource only if it lets a product manager use it at work. No licence file, or terms that forbid using the files outside the vendor's own product, meant a fail. A hosted service passed when its vendor documents it for customers.
2. **Privacy and security.** We recorded what each resource runs on your machine (scripts, hooks, installers) and where your data goes. Anything undisclosed would have failed. Everything that runs code or sends data is marked in [resources.json](resources.json).
3. **Maintenance.** At least one commit in the 180 days before 11 October 2026, or a vendor documenting its hosted service as current.

**Then seven scores from 1 to 5,** weighted as follows: real world PM usefulness 25, quality of output 20, ease of setup and use 15, integration with Claude 15, reuse across workflows 10, transparency, licence and cost 10, maintenance and reliability 5. The score out of 100 is the sum of each weight times its score divided by 5.

**Quality of output comes only from testing.** Our blind benchmark gave nine research setups one real PM question and had separate graders score each report on clarity, visuals, concision, decision usefulness, honesty and accuracy at source. Five outside collections were in it, each through one research skill, and four of them are on this list; their quality score speaks for that one skill only. Plain Claude with no skill scored 22 of 25 there, more than any outside skill. Where we have not tested a resource, its quality is not scored, and its total uses the score plain Claude earned (4 of 5). Read the score of an untested resource as how useful, easy, open and maintained it is, not as proof of good output.

**Stars are reported, not scored.** The most starred collection we tested (26,866 stars at the time) tied for the lowest accuracy at 60%, and the one with 22 stars scored the highest total of the outside skills.

**We checked 14 more and left them out.** Some failed a check, some are covered better by a resource above, one is a paid product, and some need setup a product manager should not have to do, such as paid API keys or a developer preview program.

**Read a skill before you install it.** Skills are instructions plus code, and public skill marketplaces have carried malicious ones. In February 2026 [Snyk](https://research.snyk.io/blog/agent-skills-threat-landscape/) reported 76 confirmed malicious payloads among the 3,984 skills it scanned.

## Attribution

We link to every resource on this page and copy none of their files. Each stays under its owner's licence, and naming a product here does not mean its owner endorses ProdMan.AI. If you copy any of their files yourself, these are the terms that apply.

| Resource | Owner | Licence | What the licence asks if you copy files |
|---|---|---|---|
| Knowledge work plugins | Anthropic | Apache 2.0 | Keep the licence and notices, and mark your changes |
| Atlassian MCP server repository | Atlassian | Apache 2.0 | Keep the licence and notices, and mark your changes |
| Awesome PM Skills | Udi Menkes | MIT | Keep the copyright and permission notice; podcast quotes belong to Lenny Rachitsky and his guests |
| Amplitude plugin | Amplitude | MIT | Keep the copyright and permission notice |
| PM Skills Marketplace | Pawel Huryn | MIT | Keep the copyright and permission notice |
| Product Manager Skills | Dean Peters | CC BY-NC-SA 4.0 | Credit the author, link the licence, mark changes, share alike, no commercial use; the author also asks that the skills are never sold or repackaged without written permission |
| PM skills | Product on Purpose | Apache 2.0 | Keep the licence and notices, and mark your changes |
| PM Pilot | Shadman Rahman | MIT | Keep the copyright and permission notice |
| PostHog MCP server code | PostHog | MIT | Keep the copyright and permission notice |
| internal-comms and skill-creator | Anthropic | Apache 2.0, per skill | Keep the licence and notices, and mark your changes |
| Word, PDF, PowerPoint and Excel skills (not listed above) | Anthropic | Source available, all rights reserved | Do not copy, extract or adapt them; use them inside Anthropic's own apps |
| Eval skills | Shreya Shankar and Hamel Husain | Apache 2.0 | Keep the licence and notices, and mark your changes |
| Figma MCP server and skills | Figma | Figma Developer Terms | Use them under Figma's terms; there is no open source licence |
| Linear, Notion and Mixpanel MCP servers | Their vendors | Hosted services | Use them under each vendor's terms |

Jira, Confluence, Linear, Notion, Amplitude, Mixpanel, PostHog, Figma and FigJam are trademarks of their owners.
