DRAFT, not reviewed by a person

# 02 · Breaking changes and known issues (Step 2: surface first, to the people they affect)

## Breaking change — LED-504 (affects: API partner only)
- `amount` in `GET /v2/invoices` and `GET /v2/payments` changes from a decimal string to an integer
  number of cents. Example: `"1250.00"` becomes `125000`.
- No flag keeps the old format. v1 endpoints do not change.
- The partner's nightly integration reads invoices and payments from the v2 API, so this breaks their
  read of the `amount` field unless they divide by 100 (and read it as an integer, not a string).

### Timeline conflict (the central issue of this release)
- Partner agreement: "at least 14 days' written notice before any breaking API change."
- `release-scope.md`: "Partner notice for LED-504: not sent yet."
- Dates (verified with python3):
  - Planned release: Tuesday 20 October 2026.
  - Latest date to send 14-day notice for a 20 Oct release: **Tuesday 6 October 2026** — already past.
  - Today: Sunday 11 October 2026. If notice went out today, 14 days lands on **25 October 2026**.
- Conclusion: LED-504 cannot ship on 20 October without missing the contractual 14-day notice. This is
  a decision for a human (see hand back). The partner email below is written but is DRAFT and dated to
  whatever ship date is chosen; it must not be sent until the ship date is settled.

## Known issue — LED-506 (affects: anyone exporting payments to CSV)
- Exports over 10,000 rows time out. Workaround: export a shorter date range. Fix planned for 4.2.1.
