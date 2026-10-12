# ProdMan.AI · stop collecting AI tools

**15 PM skill packs, picked and scored. 56 workflows. One `/pm` command that runs them.**
Free and open source, for [Claude Code](https://code.claude.com/docs/en/overview). Describe a product
problem in plain words; `/pm` picks the workflow, runs the right skills in order, checks the result
against your inputs and tells you what still needs your judgment.

```text
/pm I have 20 messy product docs. Find the conflicting requirements and tell me what to build first.
```

[Install](#install-two-commands) · [The 15 picks](#the-15-picks-in-the-order-to-install-them) ·
[What happens after you install](#what-happens-after-you-install) · [Your first hour](#your-first-hour) ·
[56 workflows](#56-workflows-by-use-case) · [Scores](#scores-failures-included) ·
[Roadmap](https://prodman.ai/roadmap) · [Free community](https://prodman.ai/join)

---

## Install: two commands
Inside Claude Code:

```text
/plugin marketplace add aragjha/prodman-stack
/plugin install prodman@prodman-stack
```

Then type `/pm` and your problem, in any project. Prefer a folder you can read and edit?

```bash
git clone https://github.com/aragjha/prodman-stack
cd prodman-stack
claude
```

---

## The 15 picks, in the order to install them
We checked 29 PM skill packs and connectors for Claude and kept 15. Every licence was read at source,
every pick is scored out of 100, and four were tested in a blind benchmark.
Full table with scores, licences and install lines: [resources/README.md](resources/README.md).

**1. Start here (three installs, everyone)**
| # | Pick | Why |
|---|---|---|
| 1 | **ProdMan** (this repo) | One `/pm` command, your PM standards in [PM.md](PM.md), and 56 workflows that call everything below |
| 2 | **[Anthropic's product management plugin](https://github.com/anthropics/knowledge-work-plugins)** | Highest score on the list (94): specs, roadmap updates, sprint plans and stakeholder updates |
| 3 | **[PM Pilot](https://github.com/mshadmanrahman/pm-pilot)** by Shadman Rahman | Best outside skill in our blind research test (21 of 25); every claim in its briefs carries its source |

**2. Then connect the tools you already use**
| You use | Connect |
|---|---|
| Jira or Confluence | [Atlassian MCP server](https://github.com/atlassian/atlassian-mcp-server) |
| Linear | [Linear MCP server](https://linear.app/docs/mcp) |
| Notion | [Notion MCP server](https://developers.notion.com/docs/mcp) |
| Amplitude, Mixpanel or PostHog | [Amplitude](https://amplitude.com/docs/amplitude-ai/amplitude-mcp) · [Mixpanel](https://docs.mixpanel.com/docs/features/mcp) · [PostHog](https://posthog.com/docs/model-context-protocol) |
| Figma | [Figma MCP server and plugin](https://github.com/figma/mcp-server-guide) |

**3. Then go deeper, when a job needs it**
| Pick | Reach for it when |
|---|---|
| [PM Skills Marketplace](https://github.com/phuryn/pm-skills) by Pawel Huryn | You want depth: 69 skills and 42 chained workflows |
| [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills) by Dean Peters | You want the reasoning behind each method (free at work, never for resale) |
| [PM skills](https://github.com/product-on-purpose/pm-skills) by Product on Purpose | You want 68 skills with a shared project memory |
| [Awesome PM Skills](https://github.com/menkesu/awesome-pm-skills) by Udi Menkes | You want workflows built from Lenny's Podcast |
| [Eval skills](https://github.com/ai-evals-course/evals-skills) by Shreya Shankar and Hamel Husain | You ship an AI feature and need to know where it fails |
| [Anthropic's internal comms and skill creator](https://github.com/anthropics/skills) | You write leadership updates, or want to build and test your own skill |

Read a skill before you install it: skills are instructions plus code, and public marketplaces have
carried malicious ones ([Snyk, February 2026](https://research.snyk.io/blog/agent-skills-threat-landscape/)).

---

## What happens after you install
```text
you → /pm "your problem" → decision → 1 of 56 workflows → skills run in order → claims checked → result + your calls
```
1. **Every session starts with your standards.** The folder's CLAUDE.md loads [PM.md](PM.md): evidence rules, templates, review checkpoints.
2. **You type `/pm` and the problem.** It turns the request into a decision: what is being decided, by whom, by when.
3. **It picks the workflow.** One of 56, matched to the decision, and it names what is missing before it starts, such as a file or a connector.
4. **It runs the skills in order.** ProdMan's own, the picks you installed, and a labelled fallback for any you did not.
5. **A separate reader checks the claims.** Every number, date and quote against your inputs, counted by a script.
6. **You get the result and the judgment calls.** The artifact, what still needs your decision, and the next actions. Nothing is sent, posted or changed outside the folder.

---

## Your first hour
| Minutes | Do this |
|---|---|
| 0 to 5 | Install: the two commands above |
| 5 to 15 | Tell it your product: copy [context/PRODUCT.template.md](context/PRODUCT.template.md) to `context/PRODUCT.md`, or let `/pm` ask you three questions |
| 15 to 40 | Run one workflow on a real problem from this week (prompts below) |
| 40 to 50 | Connect your tracker and your analytics: one command each, in section 2 above |
| 50 to 60 | Add one pick for the work you do most, and [tell the community](https://prodman.ai/join) what broke |

**Five first prompts to try**
```text
/pm Here are notes from 6 customer interviews. What should we build next quarter, and how sure can I be?
/pm Activation dropped last month. Here is the export. Why, and what should we test first?
/pm Turn this PRD into user flows, edge cases and a clickable prototype.
/pm Write release notes for these five tickets, one version per audience.
/pm Should we build AI meeting notes or fix calendar sync first? Research it and make the call.
```

---

## 56 workflows by use case
Each one names the problem, the inputs, the skills it combines, the steps, how the result is checked,
and how tested it really is. Full directory: [workflows/INDEX.md](workflows/INDEX.md).

| Family | Use cases |
|---|---|
| **A Documents** | messy docs to clarity · knowledge base · notes to PRD · decision log · contradictory specs |
| **B Research** | research a decision · competitors · market size · interview synthesis · opportunities · jobs to be done · problem statement |
| **C Planning** | idea to roadmap · prioritisation · outcome roadmap · quarterly plan · sprint prep · dependencies and risks · stakeholder alignment |
| **D Design** | PRD to experience · journey map · information architecture · UX evaluation · usability review |
| **E Analytics** | metrics to decisions · north star · activation funnel · retention · experiments · feature adoption · monthly review |
| **F Reviews** | tests for an AI skill · PRD score · roadmap review · research check · strategy review · go or no go · AI output check |
| **G Delivery** | release notes · launch readiness · weekly status · risk summary · post launch review |
| **H Career** | portfolio from confidential work · de-identify · interview prep · teardown · learning plan |
| **I AI features** | evals from real outputs · agent spec · model choice · AI risk review |
| **J Stakeholders** | executive update · decision memo · saying no with evidence · one on one prep |

---

## What is in this repo
| Part | What it does |
|---|---|
| [skills/pm](skills/pm/SKILL.md) | **The entry point.** Request to decision, decision to workflow, skills in order, claims checked |
| [PM.md](PM.md) | The PM standards every skill reads first: evidence rules, templates, rubric, checkpoints, privacy |
| [workflows/](workflows/INDEX.md) | The 56 workflows, one line each in [ROUTES.md](workflows/ROUTES.md) |
| [resources/](resources/README.md) | The 15 picks: scores, licences, install lines, and the 14 we cut |
| [skills/product-research](skills/product-research/SKILL.md) | Research a decision: argues against your belief first, checks every quote, makes the call |
| [skills/launch-minimum](skills/launch-minimum/SKILL.md) | The eight things that must exist before a launch, and nothing else |
| [skills/portfolio-from-work](skills/portfolio-from-work/SKILL.md) and [deidentify](skills/deidentify/SKILL.md) | Confidential work into case studies you can send, with names and numbers removed |
| [skills/eval-write](skills/eval-write/SKILL.md) | The five trick inputs a skill has to survive, written before the skill |
| [evals/](evals/README.md) | Golden sets, scoreboards and the benchmark, failures left on |
| [context/](context/README.md) | Templates for your product, decisions and corrections. Yours never leave your machine |

---

## Scores, failures included
Every skill ships five inputs built to make it fail, and every graded run is published in
[evals/scoreboards](evals/scoreboards/README.md) with the misses left on. Two you should know:

- **Research.** On one PM research task, graded blind by six AI graders, plain Claude with no skill scored 22 of 25 and beat the five community research skills we tested (17 to 21). Our first version scored 16, last. Rebuilt twice, it scored 23, a one point lead inside the grading noise, and it paraphrased one number. [The benchmark](evals/benchmarks/2026-10-11-research-head-to-head.md).
- **`/pm` itself** has passed 1 of its 5 trick inputs at best across four graded runs. It named the right route in 19 of 20 graded runs and stopped before any outside action in all 20; its claims check is the part still being fixed. [The scoreboard](evals/scoreboards/pm.md).

---

## What this repo cannot do
| | |
|---|---|
| **Remember you across projects** | Your context files help inside one folder. Anything not written down is gone when the session closes |
| **Reach your tools on its own** | Workflows that need Jira, Linear or analytics say so first, and work only from what you give them |
| **Replace a reviewer** | A separate reader checks every claim, but it is the same model. A score you publish should come from someone else |
| **Promise time saved** | It covers tasks. Nobody has measured hours saved, so we do not claim any |

[ProdMan OS](https://prodman.ai/os) is where memory across projects and workflows on a schedule are
being built. This repo stays free under MIT either way.

---

## Contributing, community, credits
- **New workflows and skills** arrive with their five trick inputs first ([eval-write](skills/eval-write/SKILL.md) helps), then one scored run. A skill nobody can fail does not get merged.
- **Found a wrong number or a broken skill?** Open an issue with the output.
- **Free community:** a WhatsApp group for PMs who build with AI: [prodman.ai/join](https://prodman.ai/join)
- **Credits:** every outside resource is linked, never copied, with its licence in [resources/README.md](resources/README.md). Naming a product does not mean its owner endorses ProdMan.AI.

Built by Anurag Jha, a product manager who builds the agents that do his own PM work. MIT licence.
