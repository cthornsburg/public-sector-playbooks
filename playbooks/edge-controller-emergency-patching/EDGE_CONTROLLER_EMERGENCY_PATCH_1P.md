# Edge Controller Emergency Patch — 1-Page Quick Card

**Purpose:** Rapidly reduce active-exploitation risk on internet-exposed edge controllers (e.g., Cisco SD-WAN class controllers) with controlled operational impact.

## Trigger (Any One)
- CISA KEV adds relevant CVE.
- Vendor marks active exploitation/in-the-wild.
- Trusted alert (CISA/FBI/MS-ISAC/vendor) indicates urgent risk.
- Suspicious admin/API activity on controller.

## First 2 Hours (Contain + Prepare)
1. **Activate emergency patch mode** and assign leads (Incident, Network, Security, Comms).
2. **Verify exposure:** identify all controller instances + versions + internet reachability.
3. **Lock down management plane:** allowlist admin access (VPN/trusted IP only), remove open internet admin where possible.
4. **Preserve evidence:** export auth/admin/config logs, capture pre-change config snapshot.
5. **Set decision window:** patch now vs temporary mitigation (default to patch if active exploit credible).

## 2–8 Hours (Execute)
1. Validate backup/config export + rollback path.
2. Patch representative non-prod quickly (if feasible).
3. Patch DR/secondary, then primary production controllers.
4. Validate control-plane health, policy sync, branch connectivity.
5. If patch unavailable: apply vendor mitigations + strict mgmt-plane isolation + enhanced monitoring.

## Required Validation Before Close
- [ ] Vulnerable versions remediated (or documented compensating controls).
- [ ] Mgmt interfaces not broadly internet-exposed.
- [ ] Privileged credentials reviewed/rotated if compromise suspected.
- [ ] MFA/strong auth enforced for admin access.
- [ ] No unexplained privileged logins during window.
- [ ] Stakeholder update sent with residual risk.

## Rollback (Only If)
- Sustained critical outage with no workaround.
- Control-plane integrity failure post-patch.
- Vendor confirms urgent defect.

If rollback occurs: reapply strict mitigations, remain in incident mode, escalate vendor case.

## Same-Day Hunt Checks
- Unusual admin/API actions (14–30 day lookback).
- New privileged account creation or token abuse.
- Unexpected config pushes or outbound connections.
- Correlate controller events with firewall/VPN/IdP logs.

## 7-Day Hardening Actions
- Permanently restrict controller management plane exposure.
- Enforce PAM/MFA; remove shared admin accounts.
- Add KEV-to-asset mapping to weekly patch governance.
- Tabletop this scenario quarterly.

## Escalation Message (Leadership)
“Active exploitation risk identified for edge controllers. Emergency patching/mitigation is [in progress/completed]. Service impact: [none/minor/major]. Residual risk: [low/medium/high]. Next update: [time].”

---
**Companion detailed playbook:** `EDGE_CONTROLLER_EMERGENCY_PATCH_PLAYBOOK.md`  
**DFIR follow-on:** `playbooks/dfir-first-24-hours/README.md`
