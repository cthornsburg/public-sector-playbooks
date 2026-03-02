# EDGE CONTROLLER EMERGENCY PATCH PLAYBOOK (DRAFT)

**Audience:** Municipal IT/security teams, network admins, incident response leads  
**Use case:** Rapid response to active exploitation risk (e.g., Cisco SD-WAN controller vulnerabilities)  
**Status:** Draft for review

---

## 1) Trigger Conditions (Any One = Activate)

1. CISA KEV adds relevant CVE for your edge controller product.
2. Vendor advisory marks active exploitation / in-the-wild abuse.
3. Trusted intel (CISA/FBI/MS-ISAC/vendor) indicates likely exploitation path against your deployment model.
4. Evidence of suspicious access to edge controller/admin plane.

---

## 2) Roles and Decision Authority (Set in First 30 Minutes)

- **Incident Lead (IL):** owns operational decisions and timeline.
- **Network Lead (NL):** owns controller patch plan and rollback.
- **Security Lead (SL):** validates exposure, logs, IOC checks.
- **Business Owner (BO):** approves outage windows and service risk.
- **Comms Lead (CL):** internal stakeholder and leadership updates.

**Decision rule:** If active exploitation is credible and controller is internet-reachable, default to **emergency patch mode**.

---

## 3) 0–2 Hours: Stabilize and Verify Exposure

### 3.1 Confirm exact exposure
- Inventory all edge controller instances (prod/DR/lab).
- Confirm internet reachability of management interfaces.
- Identify versions/builds and map to vulnerable versions.
- Record auth posture (MFA, SSO, local admin usage).

### 3.2 Apply immediate risk reduction (before patch if needed)
- Restrict management plane access to allowlisted admin IPs/VPN only.
- Disable unnecessary public management access.
- Enforce MFA where available.
- Rotate privileged credentials if compromise is suspected.

### 3.3 Preserve evidence
- Export relevant auth logs, admin action logs, config change logs.
- Snapshot configs/state before making changes.
- Start incident timeline with UTC + local timestamps.

---

## 4) 2–8 Hours: Patch/Mitigate Execution

### 4.1 Pre-change safety checks
- Confirm tested backup/config export exists and is readable.
- Confirm rollback path and decision threshold (see §6).
- Identify service impact window and stakeholder notification list.

### 4.2 Patch sequence (recommended)
1. Patch non-prod/lab controller first (if representative and quick).
2. Validate control-plane health and critical workflows.
3. Patch DR/secondary controllers.
4. Patch primary production controllers.
5. Validate policy sync, routing/overlay health, and admin access controls.

### 4.3 If patch unavailable or unstable
- Apply vendor-approved mitigations immediately.
- Maintain strict mgmt-plane isolation.
- Increase monitoring frequency (auth failures, unusual admin/API actions).
- Set short review interval (e.g., every 4 hours) until patch is available.

---

## 5) Validation Checklist (Required Before Closure)

- [ ] Vulnerable versions removed or documented mitigations in place.
- [ ] Management interface no longer broadly internet-exposed.
- [ ] Admin credentials rotated (or exception approved/documented).
- [ ] MFA/strong auth confirmed for all privileged access.
- [ ] No unexplained privileged logins during change window.
- [ ] Health checks pass (controller status, policy push, branch uptime).
- [ ] Stakeholder update sent with residual risk statement.

---

## 6) Rollback Criteria (Pre-Approved)

Rollback only if one or more are true:
- Sustained critical outage without workaround.
- Loss of management/control-plane integrity post-patch.
- Vendor confirms urgent defect impacting safety/availability.

If rollback is triggered:
1. Re-apply strict compensating controls (mgmt-plane isolation, allowlists).
2. Escalate to incident status.
3. Open emergency vendor case and document ETA for safe re-patch.

---

## 7) Detection and Hunt Guidance (Same Day)

- Review for anomalous admin/API actions in last 14–30 days.
- Hunt for new local admin creation, token abuse, unusual configuration pushes.
- Correlate controller logs with firewall/VPN/IdP logs.
- Check for unexpected outbound connections from controller hosts.

If suspicious findings exist, transition to DFIR workflow:
- `playbooks/dfir-first-24-hours/README.md`

---

## 8) Communications Templates (Short Form)

### 8.1 Leadership update (internal)
“Due to active exploitation risk affecting edge controllers, we initiated emergency patching/mitigation. Current status: [in progress/completed]. Service impact: [none/minor/major]. Residual risk: [low/medium/high]. Next update in [X hours].”

### 8.2 Technical team update
“Emergency change window active for [platform]. Required actions: [patch version/mitigation], [validation checks], [log review]. Escalate immediately on auth anomalies or control-plane instability.”

---

## 9) Post-Incident Hardening (Within 7 Days)

1. Permanently remove direct internet exposure of management interfaces.
2. Enforce PAM/MFA and eliminate shared admin accounts.
3. Add KEV-to-asset mapping in weekly patch governance.
4. Add edge controller emergency patch tabletop scenario quarterly.
5. Update procurement/security requirements for controller platforms (secure-by-default mgmt access, rapid patch SLAs, log export capability).

---

## 10) Metrics (Track and Report)

- Time to decision (trigger → emergency mode)
- Time to first mitigation
- Time to full patch coverage
- % of edge controllers with restricted mgmt-plane access
- # anomalous privileged events during response window

---

## 11) Cisco SD-WAN-Specific Review Prompts (Optional Annex)

Use this section during review meetings:
- Are vManage/vSmart components directly reachable from internet?
- Are controller APIs restricted to trusted admin networks?
- Are certificate/auth trust settings reviewed after emergency changes?
- Was emergency guidance from CISA/vendor explicitly mapped to each device role?

---

## 12) Reviewer Questions (for Chip)

1. Should this playbook assume 24/7 municipal SOC coverage, or low-staff “on-call only” operations by default?
2. Do you want a one-page quick card version for city manager/executive use?
3. Should we add a companion worksheet (`EDGE_CONTROLLER_PATCH_ACTION_SHEET.md`) for real-time change tracking?
