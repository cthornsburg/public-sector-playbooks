# Ransomware Readiness Pack (Cities/Counties)

**Purpose:** a practical, minimum-viable package a city/county can adopt quickly to reduce ransomware impact and improve response speed.

**How to use this pack:**
1) Complete the Readiness Checklist (Section 1) and create a short backlog.
2) Confirm your “Minimum Viable Logging” (Section 2) so DFIR is possible.
3) Run the Tabletop (Section 3) with leadership + IT + comms.
4) Pre-stage comms templates (Section 4) and vendor contacts.

---

## 1) Readiness Checklist (minimum viable)

### Identity & access
- [ ] MFA enforced for: email, VPN/remote access, privileged accounts, cloud admin portals.
- [ ] Separate admin accounts (no daily-driver admin).
- [ ] Privileged access reviewed monthly; disable stale accounts.
- [ ] Break-glass accounts exist, are monitored, and stored securely.

### Endpoint + server protection
- [ ] EDR deployed on endpoints + servers with alerting configured.
- [ ] Local admin rights minimized (especially on user workstations).
- [ ] Application allowlisting (or at least block known LOLBins where feasible).
- [ ] RDP exposure eliminated or tightly controlled (no direct internet exposure).

### Network controls
- [ ] Network segmentation: critical services separated (finance/payroll, dispatch, utilities, backups).
- [ ] Admin access from hardened admin workstations or jump hosts.
- [ ] DNS filtering / web filtering enabled where possible.
- [ ] Known-bad IP/IOC blocking process exists (edge + EDR).

### Patch & vulnerability governance
- [ ] Patch SLAs defined: 7/14/30 days by severity and exposure.
- [ ] CISA KEV catalog is used as the top priority patch list.
- [ ] Internet-facing systems patched first (VPNs, firewalls, email gateways, remote management).

### Backups (ransomware survivability)
- [ ] 3-2-1 strategy in place (or equivalent) with at least one offline/immutable copy.
- [ ] Backup credentials isolated from domain admin.
- [ ] Restore tests performed at least quarterly; results documented.
- [ ] Backup monitoring alerts on failed jobs and unusual deletion/encryption activity.

### Incident readiness
- [ ] Incident lead + scribe roles pre-assigned.
- [ ] Out-of-band contact list maintained (cell numbers, alternate email).
- [ ] Vendor list maintained (EDR, MSP, cloud, telecom, cyber insurance, IR retainer).
- [ ] Legal/notification decision path defined (who decides, what triggers).

---

## 2) Minimum Viable Logging (so DFIR is possible)

If you cannot answer “what happened” quickly, ransomware incidents get more expensive.

### Must-have log sources
- Identity:
  - [ ] Domain controller authentication logs (or IdP logs if cloud-first)
  - [ ] Admin account activity
- Network:
  - [ ] VPN authentication + connection logs
  - [ ] Firewall logs (allow/deny, egress)
  - [ ] DNS query logs (or resolver logs)
- Endpoint:
  - [ ] EDR detections and raw telemetry exports
- Email:
  - [ ] Email security gateway logs and OAuth/app consent events
- Cloud:
  - [ ] M365/Azure/Google audit logs (admin activity, mailbox rules, risky sign-ins)

### Operational requirements
- [ ] Centralize logs (SIEM or log platform). Keep at least 30 days hot, 180 days searchable if possible.
- [ ] Time sync: NTP across endpoints/servers/network gear.
- [ ] Ensure someone can export logs quickly under pressure (permissions + runbook).

---

## 3) Tabletop Exercise (60–90 minutes)

### Attendees (recommended)
- IT lead + sysadmin/network
- Department leadership (or city manager’s office)
- Comms/PIO
- Legal (or designated contact)
- Finance/payroll representative
- 911/dispatch/operations stakeholder (if applicable)

### Objectives
- Validate decision-making and communications.
- Confirm backup/restore reality (not assumptions).
- Identify gaps in segmentation, logging, and account hygiene.

### Scenario (facilitator script)
1) **Initial indicators**: EDR flags suspicious activity on a finance workstation; unusual VPN login.
2) **Spread**: file share latency spikes; multiple endpoints show encryption activity.
3) **Impact**: payroll and permitting are down; leadership asks for ETA.
4) **Ransom note**: appears on a shared drive; threat actor claims data exfiltration.
5) **Public pressure**: citizens complain on social media; local media calls.

### Key questions (force decisions)
- Do we disconnect from the network? What stays online (911, utilities)?
- Who has authority to shut down services?
- What’s our restoration priority order?
- What evidence must be preserved before containment actions?
- Do we have cyber insurance? Who notifies them and when?
- If exfiltration is suspected, who assesses notification obligations?

### Injects (optional)
- Vendor reports suspicious API activity.
- Backups appear intact, but restore is failing.
- Attack appears to originate from a compromised admin account.

### Output
- A short list of: top 5 gaps, owners, and a 30/60/90-day remediation plan.

---

## 4) Communications Templates (starter set)

These are meant to be edited and approved *before* an incident.

- Holding statement: `templates/initial-statement-holding.md`
- Incident log: `templates/incident-log.md`

### Recommended additions (next iteration)
- Internal staff notice (what to do / what not to do)
- Citizen-facing service interruption notice
- Vendor outreach email (requesting logs, status, contacts)

---

## 5) Pre-incident “Call Sheet” (build this now)

Create a one-page contact sheet:
- Cyber insurance hotline + policy #
- Outside counsel (if used)
- IR provider / retainer contact
- MSP / key vendors (EDR, cloud, telecom)
- Local/state/federal reporting contacts as appropriate

---

## 6) References
- CISA Alerts: https://www.cisa.gov/news-events/alerts
- CISA KEV Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
