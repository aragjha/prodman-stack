DRAFT, not reviewed by a person

# De-identify pass (step 4 of G01)

The release notes in [02-release-notes.md](02-release-notes.md) are the only thing headed anywhere
public (#product-updates). I scanned them for the categories the deidentify skill covers.

| Category | Found? |
|---|---|
| Employer / company name | None. "The firm" is generic, from PAY-415's title. |
| Customer / client name | None. "Clients" is generic. No individual client named. |
| Colleague / person name | None. |
| Traceable numbers (prices, counts, metrics) | None. |
| Other identifying detail | None. Ticket IDs (PAY-###) are internal references, synthetic. |

**Nothing needed removal** — the inputs are synthetic and already generic. The ticket IDs are kept
because an internal Slack channel is the audience; drop them if the notes ever go to customers.

With
real customer or employer content, run [deidentify](../../skills/deidentify/SKILL.md) in its own
session before posting.
