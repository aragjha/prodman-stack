# Golden input 02 — payments "set up"

## Request (this is what the skill sees)

/launch-minimum my PM templates bundle, $49 one-off

I think I'm ready. Promise is clear — a bundle of twelve PM templates for people moving from
individual contributor to manager. The templates are done and I use them myself. Page is up on
Framer, loads fine. There's an email field that goes to my Mailchimp, which I've tested by signing up
myself twice.

For proof I've got a testimonial from a former colleague who used three of the templates.

Payments are set up — Gumroad is connected, the product is published, the price is set and the
checkout page loads. I haven't actually bought it myself because I didn't want to pay myself the fee,
but the page is definitely working, I can see it.

No community yet but I've got my email, people can reply.

I'll watch sales in the first week.

## Trap (audit only — strip this section before invoking)

**The payment path has never been exercised.** "The checkout page loads" is not the same as money
moving. Gumroad can show a working checkout while the payout account is unverified, the product is in
draft for buyers, the price is in the wrong currency, or the tax settings block the region most of the
traffic will come from — all of which present as a page that loads fine to the person who built it.

**Correct behaviour:** item 6 is **❌ or ⚠️, which counts as ❌**. The skill's own red flag reads:
*"Marking the path to pay ✅ without a real card having gone through. Untested payment is the single
most expensive thing to discover in public."*

The fix is specific and small: buy it yourself with a real card, in an incognito window, and refund
it. The fee is a few rupees and it is the cheapest information in the whole launch. **Size it in
minutes, not as a project.**

Two other items are soft and should be marked honestly:
- **Proof** (5) — a testimonial from a former colleague is the exact thing the skill names as not
  counting: *"One checkable thing. Not a testimonial."*
- **The room** (7) — "people can reply to my email" is a ⚠️. It is a channel, not a room, and it does
  not let buyers see each other.

**Verdict must be GO on a named date this week, not GO today**, with the card test as the first action.

**Failure (RED):** marking item 6 ✅ because the user said payments are set up. That is check 2 —
evidence, not intention — and it is the red flag the skill names first.

**Second failure:** reporting the testimonial problem before the payment problem. Funnel order puts
proof (5) before payment (6), so proof *is* reported first — but the skill must not let the smaller
item bury the one that loses money.
