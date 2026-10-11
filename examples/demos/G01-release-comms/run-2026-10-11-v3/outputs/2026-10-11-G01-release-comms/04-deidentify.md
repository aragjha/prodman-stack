DRAFT, not reviewed by a person

# 04 · De-identify review (Step 4: run on anything public)

Note on scope: these drafts are Ledgerly's own outbound release communications, not a portfolio piece
about confidential work, so the full `deidentify` skill (built for case studies/posts) is not a clean
fit. I ran its core check — strip anything you are not free to publish and flag anything uncertain —
against each audience-facing draft. Findings:

| Item | Audience | Identifying detail / traceable number? | Decision |
|---|---|---|---|
| Firm-admin email (§B) | Public (firms) | None. No ticket numbers (house style). No counts. | OK to publish after review |
| Accountant panel (§C) | Public (in-app) | None. No ticket numbers. No jargon. | OK to publish after review |
| API changelog (§D1) | Partner engineers | Ticket number LED-504 kept — allowed; house-style ban on ticket numbers covers only firm-admin/accountant material | OK after review |
| Partner email (§D2) | Jonas (named recipient) | Names "Jonas" (recipient) and "Maya" (sender) — normal for a direct business email | OK; confirm sender name/sign-off |

Kept internal, NOT placed in any public note (from `audience.md`): ~300 firms, ~1,800 seats, the ~40
firms using the partner integration, and the release manager's name (Kwame). These are business
metrics and internal roles; none appear in the published drafts.

For a human to confirm before anything leaves the machine: the sender name on the partner email, and
that "Ledgerly" and product/feature names are the intended public branding.
