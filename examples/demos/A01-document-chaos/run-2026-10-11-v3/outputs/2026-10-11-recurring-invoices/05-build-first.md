DRAFT, not reviewed by a person

# 05 · What to build first (A01 step 7)

Decision this serves: the Q4 launch that leadership is tying to seat expansion (10, 14). Scope ranked is the current agreed scope (PRD v2). Confidence = strength of evidence that customers need it (per [04-themes.md](04-themes.md)). Effort = Kwame's estimate (06); effort numbers are the engineers', not the model's.

## Agreed scope, in build order
Order is set by dependency first (everything needs the engine), then evidence.

| Rank | Requirement | Effort (06) | Evidence confidence | Why here |
|---|---|---|---|---|
| 1 | **R1 Series engine** (create/schedule/send) | 3 wks | HIGH (T2, 5 sources) | Everything depends on it; also the prerequisite for reminders (06: reminders "can only start after the engine is done"). |
| 2 | **R6 Edit future invoices only** | 1.5 wks | HIGH (08; 03 office manager; 13) | Named by customer and prospect; fees rise every January (03), so this must be right at launch. |
| 3 | **R4 Pause / resume** | 0.5 wk | HIGH (08 summer pause) | Cheap, directly evidenced. |
| 4 | **R3 Upcoming list, 60 days** | 1 wk | MEDIUM (T3) | Visibility for cash planning (03) and review (08). |
| 5 | **R5 Preview email** | 1 wk | HIGH (08 "look before they go out") | Wanted; note timing conflict C4 (24h vs 3 days) to settle before build. |
| 6 | **R7 Custom recurrence rules** | 2 wks | **ZERO / weak** | Origin unknown (04), one customer doesn't need it (08), tested badly (12). **First candidate to cut.** |

Agreed-scope total = 10 weeks incl. QA (06) → GA 30 November on a 21 September start.

## The lever for the date (C1)
Cutting **R7 (2 wks)** is the cleanest way to move toward the CEO's 31 October. Dropping R7 removes ~2 of the ~4 weeks gap and removes the least-evidenced, worst-tested item — it does not close the gap alone. There is also "no buffer for holidays or sickness" (06). Hitting 31 October would need more than R7: it is a scope-vs-date decision for leadership, not an arithmetic one.

## Contested scope — do not build until decided (see 03-conflicts.md)
| Item | Evidence | Effort (06) | Blocking decision |
|---|---|---|---|
| **Automatic payment reminders** | **Strongest demand + churn + competitive gap** (T1, 6 sources) | 2 wks, after engine | C2 — CEO rated it "nice to have" on an 18% figure the support dashboard (43%) contradicts. |
| **Multi-currency (EUR)** | Weak signal, 1 prospect; but a written sales promise (C3) | 2 wks | C3 — honour the prospect commitment or correct it before the proposal is sent. |
| **Autopay** | Mixed; deferred by v2 | 5 wks + security review (3–4 wk lead) | Already phase 2 / Q1 2027. No action unless leadership re-opens it. |

## Reading of the evidence (not a decision)
If the goal is seat expansion and retention, the documents point to a gap: the best-evidenced customer pain (reminders, T1) is parked while the least-evidenced item (R7) is funded. The series engine (R1) is the right first build regardless. Whether reminders should displace R7 — or follow the engine in the same quarter, since they reuse it (06) — is a leadership call, surfaced in the handback, not made here.
