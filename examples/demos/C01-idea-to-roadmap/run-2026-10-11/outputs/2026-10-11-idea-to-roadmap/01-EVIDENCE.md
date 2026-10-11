# 01 · EVIDENCE — competitor offerings & pricing for payment reminders + client portal

Starting position written 2026-10-11 (before searching).

- **Decision:** Should Ledgerly build automatic payment reminders + a client payment portal in
  Q1 2027, and if so how should the two squads sequence it, given the feature must drive seat
  expansion (300 net new seats in the quarter)?
- **Goal (from the PM, not the web):** 300 net new seats in Q1 2027. Context: ~300 firms, $25/seat/
  month billed annually; 1,760 seats end-Jun 2026 → 1,840 end-Sep 2026. (SYNTHETIC demo numbers.)
- **Belief (third person):**
  - B1: The PM believes reminders + portal is the right bet because late payment is the most common
    complaint from firms.
  - B2: The PM believes it is urgent because a competitor shipped payment reminders this summer and
    it comes up in deals.
  - B3 (leadership): Leadership believes shipping this will make existing firms add seats.
- **What would change their mind:**
  - If reminders + portals are a free/bundled commodity across competitors (then it can't justify
    *added seats* — it's table stakes, defends rather than expands).
  - If nothing in the feature creates a reason to add a *seat* (seats = users, not usage), the
    expansion thesis (B3) fails even if the feature is loved.
  - If reminder "nagging" risk (deliverability, client relationships) is real enough that firms
    won't turn it on for their big clients (the 15-seat admin's worry).

---

## Sources (S# | exact quote | URL | how checked)

- **S1 | FreshBooks pricing.** "Automated Late Payment Reminders" and "Client Account Portal" are
  both included in all four plans (Lite, Plus, Premium, Select). "Team Members ($11/mo per user)".
  List prices: Lite $23.00/month, Plus $43.00/month, Premium $70.00/month, Select custom.
  https://www.freshbooks.com/pricing | read on the page.
- **S2 | Xero invoice reminders (Paidnice blog, citing Xero Central).** "Included in every Xero
  plan, no add-on cost"; "You can have up to five reminders in your organisation."
  https://www.paidnice.com/blog/xero-invoice-reminders-explained | second hand (blog quoting Xero
  Central; not Xero's own page).
- **S3 | QuickBooks Online help.** "From the dropdown fields, select days, and before or after to
  tell QuickBooks when to send the reminder."
  https://quickbooks.intuit.com/learn-support/en-us/help-article/invoicing/send-invoice-reminders-automatically-manually/L84cQjpxo_US_en_US
  | read on the page (confirms automatic reminders are built into QBO invoicing).
- **S4 | Chaser pricing (standalone AR tool).** Compact from £199/month ($259/mo), Core from
  £599/month ($779/mo), Complete from £899/month ($1169/mo), Custom on request. Pricing scales by
  "total annual revenue" (Compact <£4m, Core <£10m, Complete <£100m); Compact includes 4 users,
  Core and Complete unlimited. https://chaserhq.com/global/pricing | read on the page.
- **S5 | Bill.com AR.** AR module "automate[s] payment reminders" and customers "can pay online
  through multiple methods"; tiers quoted in search summary as Essentials $45 / Team $55 /
  Corporate $79 per month. https://www.bill.com/product/pricing/ | second hand (search summary,
  page not fetched) — used only as qualitative corroboration, prices not relied on.
- **S6 | Leanpay blog (reminder deliverability risk).** "It only takes your emails being flagged as
  spam to slow down your cash flow dramatically." and "A reminder every day for a week? Bad idea.
  Spam filters detect an excessive frequency as harassment. This increases the likelihood of your
  message being reported, which damages your sender reputation."
  https://www.leanpay.io/en/blog/unpaid-payment-reminders-why-your-emails-land-in-spam-how-avoid-it
  | read on the page.

### Customer quotes (from the PM, idea.md — SYNTHETIC)
- **Q1 (office manager, 9-seat firm):** "Every Friday I email the clients who haven't paid. If
  Ledgerly did that for me, I'd move our two new juniors onto Ledgerly instead of the spreadsheet."
- **Q2 (partner, 4-seat firm):** "My clients lose the invoice email and then ask me to resend it.
  I want one link where they can see everything they owe us and pay it."
- **Q3 (firm admin, 15-seat firm):** "Reminders sound useful, but I'm nervous about a robot nagging
  my biggest clients. I'd need to control who gets chased and what it says."

## What happened to the belief (weakening evidence first)
- **Weakens B1/B3 (growth bet, seat expansion):** Reminders AND a client portal are *included free*
  in QuickBooks (S3), Xero (S2), FreshBooks (S1) and Bill.com (S5). They are table stakes, not a
  differentiator — a defensive build. Appears in REPORT findings row 1 and the call.
- **Weakens B3 (seats specifically):** Competitors that bill per user (FreshBooks, S1: "$11/mo per
  user") still *include* reminders/portal in the base plan rather than charging for them per seat.
  So the money comes from *more users on the platform*, not from the feature as a paid add-on. This
  reframes the seat thesis in REPORT and the roadmap (the lever is pulling the firm's own staff onto
  Ledgerly, per Q1). Appears in findings row 2.
- **Weakens B1 (safe to ship):** S6 shows automated reminders carry real deliverability/relationship
  risk; Q3 shows a real customer won't turn it on without controls. Appears in findings row 4 and
  becomes a hard requirement in the roadmap.
- **Supports B2 (a premium standalone category exists):** Chaser (S4) charges $259–$1,169/month for
  dedicated AR chasing, priced by revenue — proof firms will pay real money to chase debt. Appears
  in findings row 3. Dropped as a *direct* model for Ledgerly (different buyer/pricing axis), kept
  as evidence demand is real.
- **No source dropped silently.** Bill.com prices (S5) were not relied on because the page was not
  fetched; kept only as qualitative corroboration.
