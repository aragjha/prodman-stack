# Your product context

The skills read three files from this folder when they exist. Copy each template, drop the
`.template` from the name, and fill it in. Your copies are ignored by git, so they never leave
your machine.

| Copy this | To this | What it saves you |
|---|---|---|
| [PRODUCT.template.md](PRODUCT.template.md) | `PRODUCT.md` | Explaining your product again in every session |
| [DECISIONS.template.md](DECISIONS.template.md) | `DECISIONS.md` | Relitigating a decision you already made |
| [CORRECTIONS.template.md](CORRECTIONS.template.md) | `CORRECTIONS.md` | Correcting the same mistake twice |

Ten minutes on `PRODUCT.md` is the single biggest quality improvement you can make. A skill that
knows your users, your stage and the number you are measured on asks fewer questions and guesses
less.

If you installed this repo as a Claude Code plugin, keep these files in a `context/` folder inside
the project you are working in. The skills look there first.
