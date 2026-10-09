# Golden input 02 — "research the market for me"

## Request (this is what the skill sees)

/product-research

Research the AI tools for product managers market for me. I want the full picture — who the
players are, what they charge, what's trending, what people are saying. Be thorough, I'd rather
have too much than too little. I'll figure out what to do with it after.

## Trap (audit only — strip this section before invoking)

**There is no decision attached, and the user has said so out loud** — *"I'll figure out what to do
with it after."* There is no belief to test, no falsifier, no goal the research serves. The request
is for reading, and it asks for *more* of it.

**Correct behaviour:** step 1's stop condition — *"If the user cannot say what decision this research
feeds, stop and ask once."* The skill must **not search**. It asks one question, plainly: what
decision does this feed — build, buy, position, price, enter, kill? — and offers to write the ground
truth with them if they are not sure. It may say why: research with no decision attached produces a
document that confirms whatever the reader already thought, and the thoroughness the user is asking
for makes that worse, not better. One question, then wait.

If the user answers, run. If the user says *"just do the research"* a second time, the skill may
produce the **angle map only** — the questions it *would* ask, with search keys — and nothing
below it. That is useful and it is not a market overview.

**Failure:** a 3,000-word landscape — the players, the prices, the trends — produced with no ground
truth above it. It will look excellent. It will carry every mark of a good run: links, confidence
marks, a tidy table. And it will have been the wrong job, because nothing in it can be *wrong* —
there is no belief for it to contradict.

**This is a RED**, not a FAIL: *"Searching before the ground truth is written"* is a red flag in the
contract, because it is the failure every deep-research tool makes by default and the one this
skill exists to refuse.
