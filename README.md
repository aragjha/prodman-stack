# Your PM work is invisible

You have shipped things. Real things, for years. And you cannot show a single one of them.

The PRDs are in a Confluence you no longer have access to. The roadmap belongs to a company that owns it. The research is full of customer names you cannot say out loud. Meanwhile every job post wants "AI experience" and every portfolio you see belongs to a designer or an engineer who can just link the thing they built.

**You are not behind on AI. You are sitting on ten years of work you are not allowed to show.**

This turns that work into something you can send.

---

## What this does

One skill. You point it at what you remember and whatever you are allowed to keep, and it produces:

1. **De-identified case studies** — the decision you made and why, with every employer, customer and number stripped or replaced
2. **One working artifact** — the highest-leverage project rebuilt as something a person can actually open and click
3. **A portfolio page** — assembled from the above, ready to send to a recruiter or drop in a DM

It runs in Claude Code. It takes about an hour for a first pass.

---

## Start in 15 minutes

```bash
git clone https://github.com/<user>/prodman-stack
cd prodman-stack
claude
```

Then:

```
Read skills/portfolio-from-work/SKILL.md and run it on my last project.
```

It will interview you. **Answer from memory — you do not need to find the documents.** That is the point: your memory of a decision is not your employer's property, and it is the part that was always the interesting bit.

---

## The de-identification gate

This is the part everyone gets wrong, so it is built in rather than bolted on.

**Nothing leaves this folder carrying your employer's name, your customers' names, or a number you are not free to publish.** The skill refuses to produce a case study until the de-identification pass has run, and it shows you exactly what it stripped so you can check.

> "Reduced churn 18% for [named enterprise client]" becomes "cut monthly churn by roughly a fifth on a B2B subscription product."

The second sentence is publishable, survives a legal review, and is **more** interesting to read — because it is about the decision rather than the logo.

If you cannot tell whether something is safe to publish, the skill flags it and stops rather than guessing.

---

## What is inside

```
prodman-stack/
├── README.md                       ← you are here
├── skills/
│   └── portfolio-from-work/
│       └── SKILL.md                ← the skill
├── examples/
│   └── worked-example.md           ← one real case study, start to finish
└── LICENSE                         ← MIT, use it commercially
```

That is deliberately small. **One skill that works beats forty that you never run.** More get added as they prove themselves on real work — not before.

### What this repo cannot do

Three things, stated plainly because you will hit them by day three and they are not bugs:

| | |
|---|---|
| **It will not remember you** | Every session starts from zero. You re-explain your product each time |
| **It cannot tell you if the output is right** | It produces. It does not check |
| **It does not get better because you used it** | Your corrections die when the session closes |

Those are the difference between a folder of skills and a system. If they matter to you, that is what
the paid OS is for — and if they do not, this repo is genuinely yours under MIT, forever, with no catch.

---

## Get the next ones

New skills land here as they are built and tested. If you want them as they ship:

**→ [Drop your email here](https://aragjha.github.io/prodman-stack/)** and each new skill arrives the day it ships, free.

You also get the part that is not in this repo yet: the **eval golden sets** — the frozen adversarial
inputs each skill is tested against, with the traps documented. That is how you check whether a skill
is actually doing its job rather than just producing output.

No newsletter. No drip sequence. A skill, when there is a skill.

---

## Who made this

A working product manager who builds the agents that do his own PM work, and publishes what breaks as well as what works.

MIT licensed. Fork it, sell what you build with it, no attribution needed.
