DRAFT, not reviewed by a person

# Conflict brief — is SAML SSO required for the pilot? (A05)

All four source documents are labelled SYNTHETIC in the request.

## The contradiction, both sides quoted

| Side | Source (synthetic) | Exact words |
|---|---|---|
| SSO is a launch must-have | Doc 1, PRD v2 (product) | "Must have: SSO with SAML for the pilot customer, audit log, admin roles." |
| SSO can wait past the pilot | Doc 2, sales call notes (pilot customer) | The IT lead said Google login is fine for the pilot; SAML SSO "can wait until we roll out to the whole company next year". |

The quotation marks around "can wait until we roll out to the whole company next year" are the IT lead's words as recorded in the notes. "Google login is fine for the pilot" is the note-taker's summary, not a verbatim quote.

## Does a later document already settle it?
No decision log or dated document was provided, so nothing on hand closes this. The CEO message (Doc 4) fixes the date but says nothing about SSO. A later written decision may exist elsewhere that we cannot see. **This needs a person.**

## What each side rests on
- **PRD v2 (product)** states the pilot's must-haves. Owner: product / PRD author.
- **Sales call notes (customer's IT lead)** carry the pilot customer's own statement of what they need for the pilot. The customer is the authority on the pilot customer's requirement. Owner: sales, relaying the customer.

## What each option costs (estimates are engineering's own, Doc 3)

| | Option A — keep SAML SSO for the pilot (follow PRD) | Option B — defer SAML SSO, use Google login for the pilot (follow sales) |
|---|---|---|
| Scope | SSO 3 wk + audit log 2 wk + admin roles 1 wk = 6 engineer-weeks of must-haves | audit log 2 wk + admin roles 1 wk = 3 engineer-weeks |
| Date risk | Fits 7.6 nominal engineer-weeks only with near-zero margin and perfect parallelism; leaves almost nothing for integration, testing or slippage — the main threat to the CEO's "Do not slip the date." | ~4.6 engineer-weeks of margin left for integration, testing and the unexpected; the date is well protected. |
| Customer | Builds the one feature the customer said can wait; audit log (their top priority) competes for the same weeks. | Delivers the audit log, the customer's stated top priority, with room to harden it before their December compliance review. |
| Cost of being wrong | If any stakeholder truly needs SAML for this pilot customer, it is late to find out. Low: IT lead said Google login is fine for the pilot. | PRD v2 must be amended; if the IT lead's view is overruled internally, SSO returns as a 3-week item. |

## Recommendation
**Option B — defer SAML SSO to the company-wide rollout and run the pilot on Google login.** Confidence: **HIGH** on the customer's stated need (quoted from the IT lead); **MEDIUM** on execution, because it assumes Google login is already production-ready for this customer (see assumptions in the plan). The CEO's "do not slip" and sales' "SSO can wait" point the same way; only the PRD disagrees, and the PRD is ours to amend.

**Who decides:** the owner of PRD v2 scope (product owner / CEO).

**Question to put to them:** "The pilot customer's IT lead says Google login is fine for the pilot and SAML SSO can wait until next year's company-wide rollout. SAML SSO is 3 of our ~8 weeks of scope. Do you approve dropping SAML SSO from the 15 November pilot and amending PRD v2, so the date holds and the audit log (their top priority) is solid before their December compliance review?"

## Reconciled spec (applies only if the decider approves Option B)
- PRD v2 "Must have" becomes: **audit log, admin roles**, with **Google login** as the pilot's sign-in.
- SAML SSO moves to the **next-year company-wide rollout**.
- Change note: one change — SAML SSO moved from pilot must-have to the company-wide rollout; everything else in PRD v2 unchanged. Not yet applied; awaiting the decider.
