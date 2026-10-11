# Redactions made after this run, before commit

| File | What | Why |
|---|---|---|
| `2026-10-11-pay-release-notes/check.md` | The account email address, quoted in row 1's Claim, replaced with `[email removed]` | The run wrote the session's account email into its frame file. The checker failed that row and the seal removed the address from the frame, but the check table still quoted it. The seal does not clean the check table; that is a fix for the next version |

This changes the check table's fingerprint: sha256 `a725f4d05e8e35cc...` in seal.txt, `b835793e593b2988...` now. Every other file is as sealed.
