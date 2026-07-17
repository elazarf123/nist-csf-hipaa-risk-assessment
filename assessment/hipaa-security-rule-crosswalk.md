# HIPAA Security Rule ↔ NIST CSF 2.0 Crosswalk (assessed gaps only)

Only rows where this assessment found a gap are listed — a crosswalk of everything
is documentation; a crosswalk of *your* gaps is a work plan. R-numbers link to the
[risk register](../risk-register/risk_register.md).

| Gap found | HIPAA Security Rule citation | Standard type | CSF 2.0 | Risk |
|---|---|---|---|---|
| No documented Security Risk Analysis | §164.308(a)(1)(ii)(A) | **Required** | ID.RA | R-01 |
| Audit logs never reviewed, no PHI-access alerting | §164.308(a)(1)(ii)(D), §164.312(b) | **Required** | DE.CM | R-02 |
| Manual deprovisioning, no access review | §164.308(a)(3)(ii)(C), §164.308(a)(4) | Required/Addressable | PR.AA | R-03 |
| Partial MFA on privileged access | §164.312(d) | Required | PR.AA | R-04 |
| EHR appliance unpatched 14 months | §164.308(a)(1)(ii)(B) Risk management | **Required** | PR.PS | R-05 |
| Breach-notification duties unassigned | §164.308(a)(6); Breach Rule §164.404 | **Required** | RS.CO | R-06 |
| Backup restores untested, RTO undefined | §164.308(a)(7)(ii)(A)-(B) Contingency plan | **Required** | RC.RP, PR.DS | R-07 |
| Medical devices / SaaS untracked | §164.310(d) Device & media controls | Required | ID.AM | R-08 |
| Policies stale and unowned | §164.316(b)(2)(iii) Review requirement | **Required** | GV.PO | R-09 |
| No vishing-resistant reset training | §164.308(a)(5) Security awareness | Addressable | PR.AT | R-10 |

**Reading note:** "Addressable" under HIPAA does not mean optional — it means the
entity must implement it or document why an alternative is reasonable. None of the
gaps above have documented alternatives, so all ten are compliance exposure, not
just security debt.
