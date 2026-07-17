# Plan of Action & Milestones (POA&M) — Caprock Family Clinic (Fictional)

Sequenced by risk score, cost, and dependency — not by ease. Quick wins are
scheduled early only when they don't displace Critical-risk work.

## Phase 1 — Days 0–30 (stop the compliance bleeding)

| # | Action | Closes | Cost | Milestone / evidence |
|---|---|---|---|---|
| 1 | Formalize this assessment as the documented Security Risk Analysis; Privacy Officer signs | R-01 | Staff time | Signed SRA on file |
| 2 | Enforce MFA on all privileged roles via conditional access | R-04 | $0 (existing licensing) | CA policy report: 0 privileged accounts exempt |
| 3 | Assign breach-notification duties by name; 1-page escalation card | R-06 | Staff time | IR contact card distributed; duties in job descriptions |
| 4 | Open vendor ticket + demand patch SLA for EHR appliance; VLAN-segment it meanwhile | R-05 | Staff time | Appliance isolated; vendor SLA in writing |

## Phase 2 — Days 31–90 (build the detective layer)

| # | Action | Closes | Cost | Milestone / evidence |
|---|---|---|---|---|
| 5 | Stand up weekly EHR audit-log review with documented anomaly thresholds | R-02 | Staff time | 4 consecutive weekly review records |
| 6 | Automate leaver workflow (HR feed → directory disable); first quarterly access review | R-03 | Low | Review report; 0 orphaned accounts |
| 7 | Restore-test backups; document RTO/RPO with clinic leadership | R-07 | Staff time | Successful restore log; RTO/RPO memo |

## Phase 3 — Days 91–180 (govern and sustain)

| # | Action | Closes | Cost | Milestone / evidence |
|---|---|---|---|---|
| 8 | Asset discovery sweep: medical devices + SaaS register | R-08 | Low | Inventory ≥95% coverage attestation |
| 9 | Policy refresh cycle: named owners, annual review dates | R-09 | Staff time | All policies <12 months old |
| 10 | Vishing-resistant reset procedure + simulation exercise | R-10 | Low | Simulation results; procedure adopted |
| 11 | Re-assess CSF maturity; target: no function averaging below 2.5 | All | Staff time | Updated scorecard vs this baseline |

## Sequencing rationale

Phase 1 leads with R-01 not because it's the most technical risk but because it's
the largest *legal* one: operating without a documented risk analysis is the
difference between "reasonable safeguards that failed" and "willful neglect" in an
OCR penalty determination. MFA (item 2) is the highest risk-reduction-per-dollar
action on the list. Detection work (Phase 2) precedes governance polish (Phase 3)
because an unreviewed audit log is a currently-exploitable blind spot; a stale
policy is not.
