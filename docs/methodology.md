# Assessment Methodology

## Framework and scope choices

**Why NIST CSF 2.0 (not 800-53 or HITRUST):** for an 85-person clinic, CSF's
outcome-level categories match the organization's capacity — a control catalog the
size of 800-53 would produce a paper exercise. CSF 2.0 specifically adds the
GOVERN function, which is where small-provider gaps concentrate.

**Assessment unit:** CSF 2.0 *category* level (14 categories assessed), not
subcategory — granular enough to drive a work plan, coarse enough to complete in
one assessment cycle with real evidence per row.

**Maturity scale:** 4-point (Partial / Risk-informed / Repeatable / Adaptive).
Five-point scales invite false precision; the question that matters is whether a
practice is documented, owned, and performed — not its decimal.

## Evidence standard

Every score in [scores.csv](../assessment/scores.csv) carries an evidence summary.
Rule applied: *if it isn't written down, it scores 1, no matter how well people say
they do it* — undocumented practice is person-dependent and dies with turnover,
and it is indefensible in an OCR audit.

## Risk scoring

Likelihood × Impact on 1–5 scales, calibrated to this entity: Impact 5 = clinical
operations stop or reportable breach affecting >500 patients (HHS public list);
Likelihood 4 = expected within 12 months absent action. Scores rank *this
clinic's* risks against each other to sequence the POA&M — they are not
industry-comparable metrics.

## Target profile

Targets (mostly 3, selectively 4) reflect a small covered entity's reasonable bar:
Repeatable everywhere; Adaptive only where HIPAA citation exposure or patient-safety
impact justifies the investment (identity, monitoring, risk analysis, asset
management). Setting every target to 4 would be aspiration, not a plan.

## Traceability chain

Scorecard gap → HIPAA citation ([crosswalk](../assessment/hipaa-security-rule-crosswalk.md))
→ risk with owner ([register](../risk-register/risk_register.md)) → sequenced action
with milestone ([POA&M](../poam/poam.md)). Any finding you can't walk through that
chain is an observation, not a managed risk.
