# 06 · Check — claims against inputs, then criteria

Sources: `input/release-scope.md` (scope) and `input/audience.md` (audience). Not this run's own files.

## Part A — claims table

| Claim in the artifacts | Source line (pasted) | Recomputed / recounted | Verdict |
|---|---|---|---|
| Code freeze Friday 9 October 2026 | "Code freeze: Friday 9 October 2026." | `date(2026,10,9).weekday()` = Friday | holds |
| Release Tuesday 20 October 2026 | "Planned release: Tuesday 20 October 2026." | `date(2026,10,20).weekday()` = Tuesday | holds |
| 14-day notice deadline = 6 Oct 2026 | "at least 14 days' written notice before any breaking API change" | 20 Oct − 14 days = 6 Oct 2026 | holds |
| Sending today gives 9 days' notice | today = 11 Oct 2026; "Partner notice for LED-504: not sent yet." | 20 Oct − 11 Oct = 9 days | holds |
| Send **up to 50** draft invoices at once | "Send up to 50 draft invoices at once from the invoice list" | quoted | holds |
| Email accountant who owns client on payment; on by default; off in Settings → Notifications | "Email the accountant who owns a client when that client pays an invoice … On by default. Each user can turn it off in Settings, Notifications" | path reformatted (comma → →), wording preserved | holds |
| Filter clients to overdue invoices | "Filter the client list to clients with overdue invoices" | quoted | holds |
| `amount` decimal string → integer cents; `"1250.00"` → `125000`; `GET /v2/invoices`, `GET /v2/payments`; no flag; v1 unchanged | "the `amount` field in GET /v2/invoices and GET /v2/payments changes from a decimal string to an integer number of cents, so \"1250.00\" becomes 125000 … There is no flag to keep the old format. v1 endpoints do not change" | all terms matched char-for-char | holds |
| New firms start with a ready-to-use default template | "New firms start with a ready to use default invoice template again" | quoted | holds |
| Export payments to CSV any date range; >10,000 rows time out; workaround shorter range; fix in 4.2.1 | "Export payments to CSV for any date range … exports over 10,000 rows time out. Workaround: export a shorter date range. Fix planned for 4.2.1" | quoted; "4.2.1" kept internal, phrased as "next update" to firms | holds |
| Due dates showed a day early in some time zones (fixed) | "Fix: due dates shown one day early for firms in some time zones" | quoted | holds |
| LED-507 and LED-508 not in 4.2 | "LED-507 … Not merged"; "LED-508 … Not merged" | 2 not-merged items excluded | holds |
| 7 merged items shipped | rows LED-501,502,503,504,505,506,509 = Merged | counted: 501,502,503,504,505,506,509 = 7 | holds |
| ~300 paying firms, 1–2 admins per firm | "One or two per firm, across about 300 paying firms." | quoted | holds |
| ~1,800 seats (accountants) | "Most of our roughly 1,800 seats." | quoted | holds |
| Partner ≈ 40 firms, nightly v2 reads | "used by about 40 of our firms … reads invoices and payments from our v2 API every night" | quoted | holds |
| Contact: Jonas, integration lead | "Our contact is Jonas, their integration lead." | quoted | holds |
| Release manager Kwame; PM Maya | "Release manager: Kwame (eng lead). PM: Maya." | quoted (internal/partner files only) | holds |

No number, date, name or quote appears in the artifacts that is not traceable to an input above.

## Part B — criteria (PM.md §7 + G01 checks)

G01 "checked by":
- **No unmerged ticket appears as shipped** — PASS. `01-what-shipped.md` lists LED-507/508 under
  "NOT in 4.2"; they appear in no audience message.
- **Breaking change flagged to the audience it breaks** — PASS. LED-504 is in the API-partner piece
  only, with before/after and "What you must change on your side"; it is explicitly kept out of
  admin/accountant copy.
- **Known issues listed** — PASS. LED-506 timeout + workaround appears in `02-admins.md`,
  `03-accountants.md`, and `04`/`05`.
- **Nothing posted, sent or closed** — PASS. All files are DRAFT; `05-go-live-checklist.md` lists
  send/publish as unchecked human actions.

Rubric:
- **Clarity** — PASS. Each message states what changed and whether the reader must act
  ("You may want to act on this one").
- **Visual** — PASS. Admin/accountant copy leads with a bold headline; the partner piece uses a
  before/after table.
- **Concise** — PASS. Accountant panel is headline-first for readers who read only the first line.
- **Decision** — PASS. The frame and checklist name the real decision (can LED-504 ship on 20 Oct)
  and what reverses it (notice timing).
- **Honesty** — PASS. The notice-period blocker is stated up front; `[GO-LIVE DATE]` is left as a
  placeholder rather than asserting a date the contract may not allow.
- **Accuracy** — PASS (per Part A). The one deliberate transform: "4.2.1" → "next update" in
  firm-facing copy (house style: no ticket/version jargon); the fact (a fix is coming) is unchanged.

Release-note artifact check (PM.md §5): each message has *what changed · who it's for · how to use
it · known issues*. PASS.

## Deidentify step (G01 step 4)
These are the product's own outward communications, so the product name is intentional, and the
inputs are labelled SYNTHETIC. A lightweight check was applied instead of a full de-identification:
- Internal names **Kwame/Maya** appear only in internal files (`00`, `01`, `05`) and as the sender
  of the partner email — not in admin/accountant copy. PASS.
- **Jonas** / the partner's identity appear only in the partner-facing channel. PASS.
- No secrets, keys, or customer personal data present. PASS.
Run the full `deidentify` skill if any of these pieces will be posted to a truly public surface
(e.g. a public changelog page) before publishing.
