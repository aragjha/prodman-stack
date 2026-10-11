# 04 · API partner — DRAFT

Audience: the one integration partner (document-management product, ~40 of our firms, nightly reads
of the v2 API). Readers are their engineers; our contact is Jonas, their integration lead.
They read our API changelog and any email we send Jonas. They need exact field names, before/after
examples, the go-live date, and what they must change.

> ⚠️ **BLOCKER before this is sent — read first.** The partner agreement requires **at least
> 14 days' written notice** before any breaking API change. 14 days before the planned release
> (20 Oct 2026) was **6 October 2026**. The notice has **not been sent**. If sent today (11 Oct)
> it gives only **9 days**. This draft keeps the planned date as a placeholder; do **not** send it
> until the date is resolved (see the handback's "Needs your judgment"). The `[GO-LIVE DATE]`
> placeholder below must be set to a date that is ≥14 days after the day you actually send.

---

## A) API changelog entry

### Breaking change — `amount` becomes integer cents (v2)

**Effective:** `[GO-LIVE DATE — must be ≥14 days after notice is sent]`
**Endpoints affected:** `GET /v2/invoices`, `GET /v2/payments`
**v1 endpoints:** unchanged.

**What changes.** The `amount` field changes from a decimal string to an integer number of cents.

| | Before | After |
|---|---|---|
| Type | decimal string | integer |
| Example value | `"1250.00"` | `125000` |

There is **no flag or option to keep the old format.** Once live, all v2 responses use integer
cents.

**What you must change on your side.**
- Stop parsing `amount` as a decimal string.
- Read `amount` as an integer number of cents, and divide by 100 where you need a currency value
  (e.g. `125000` → `1250.00`).
- Apply this to both `GET /v2/invoices` and `GET /v2/payments`.
- If you must keep the old format temporarily, the unchanged **v1** endpoints are the only way to do
  so.

---

## B) Email to Jonas

**To:** Jonas (integration lead)
**Subject:** Breaking change to `amount` in our v2 API — action needed before [GO-LIVE DATE]

Hi Jonas,

We're giving you written notice of a **breaking change** to our v2 API that affects your nightly
reads of invoices and payments.

**What's changing.** The `amount` field in `GET /v2/invoices` and `GET /v2/payments` changes from a
decimal string to an integer number of cents. For example, `"1250.00"` becomes `125000`. There is
no flag to keep the old format. Our v1 endpoints are not changing.

**When.** `[GO-LIVE DATE — to be confirmed; must be at least 14 days from the date of this email]`.

**What you need to do.** Update your integration to read `amount` as an integer number of cents and
divide by 100 where you need a currency value, for both endpoints. If you need more time, the v1
endpoints are unchanged and can be used as a temporary fallback.

The full details, with before/after examples, are in our API changelog: [link].

Please confirm you've received this and let us know if the timing is a problem for your team.

Thanks,
Maya

---
*Internal note: Jonas's name and the partner's identity stay in this partner-facing channel only;
they are not in the admin or accountant messages.*
