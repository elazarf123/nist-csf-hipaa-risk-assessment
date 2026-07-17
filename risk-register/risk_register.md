# Risk Register — Caprock Family Clinic (Fictional)

Scoring: Likelihood × Impact, each 1–5. ≥15 Critical · 10–14 High · 5–9 Medium · <5 Low.
Machine-readable version: [risk_register.csv](risk_register.csv)

| ID | Risk statement | L | I | Score | Rating | Treatment | Owner |
|---|---|---|---|---|---|---|---|
| R-01 | OCR audit or breach investigation finds no Security Risk Analysis on file, triggering willful-neglect penalty tier | 4 | 5 | 20 | **Critical** | Mitigate (this assessment is the first pass) | Privacy Officer |
| R-02 | Insider PHI snooping or orphaned-account misuse goes undetected because audit logs are unreviewed | 4 | 4 | 16 | **Critical** | Mitigate — automated review + alerting | IT Manager |
| R-05 | Unpatched EHR appliance exploited; clinic-wide outage or PHI exfiltration | 3 | 5 | 15 | **Critical** | Mitigate — vendor patch SLA + compensating segmentation | IT Manager |
| R-03 | Terminated workforce member retains access (manual deprovisioning failure) | 4 | 4 | 16 | **Critical** | Mitigate — automate leaver workflow, quarterly access review | IT Manager |
| R-07 | Ransomware event; backups fail restore, extended clinical downtime | 2 | 5 | 10 | High | Mitigate — quarterly restore tests, define RTO/RPO | IT Manager |
| R-04 | Privileged account compromise via credential theft (no MFA) | 3 | 4 | 12 | High | Mitigate — conditional access requiring MFA for privileged roles | IT Manager |
| R-06 | Breach discovered but 60-day notification clock missed (no assigned owner) | 3 | 4 | 12 | High | Mitigate — assign duties in IR plan, tabletop annually | Privacy Officer |
| R-08 | Unmanaged medical device or SaaS holds PHI outside inventory and controls | 3 | 3 | 9 | Medium | Mitigate — asset discovery sweep, SaaS register | IT Manager |
| R-09 | Stale policies fail to reflect actual practice, weakening audit defensibility | 3 | 3 | 9 | Medium | Mitigate — annual review cycle with named owners | Privacy Officer |
| R-10 | Service desk vishing leads to credential reset for attacker | 2 | 4 | 8 | Medium | Mitigate — verification procedure + simulation training | IT Manager |

**Register discipline:** every risk has exactly one owner (a name in production, a
role here), one treatment decision, and traces to a control gap in the
[crosswalk](../assessment/hipaa-security-rule-crosswalk.md) and a remediation line
in the [POA&M](../poam/poam.md). Risks nobody owns are risks nobody works.
