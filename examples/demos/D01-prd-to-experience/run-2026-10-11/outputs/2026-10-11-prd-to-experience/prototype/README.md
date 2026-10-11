# Clickable prototype — client payment portal

**Open `index.html` in any browser.** No build, no server. Use the left rail to jump between
screens, or tap the buttons inside the phone to walk the real path.

## Walk-through for the team (the spine)
S1 Portal home → tap **Pay** on INV-1043 → S2 Invoice detail → **Pay by card** → S3 partner page →
**Pay** → S4 confirmation (Paid). Then show the branches:
- **S1 → empty** ("all paid up") and **bank-only firm** variants.
- **S2 → Pay by bank transfer** → S5 (Payment pending).
- **S2 → Pay part of this** → S7 (partial, with live validation).
- **S3 → simulate declined / timeout** (invoice stays Open).
- **S6** link expired (request new) and link invalid.

## What this is and isn't
- **Low-fidelity, grey-box.** It shows screens, states and the click path — not visual design, not
  the firm's real brand. The blue header is a stand-in brand colour.
- **Synthetic.** Firm names, invoice numbers and amounts are made up. Banner says so.
- Built from `../04-screen-state-spec.md`. The decisions that would change these screens are in
  `../05-open-questions.md` (the multi-currency total, the status set, and bank-transfer handling
  are the three that change S1/S2/S5 most).
