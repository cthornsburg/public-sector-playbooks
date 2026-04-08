# KEV-to-Risk — IT Action Sheet (Template)

**Period:** [Month YYYY]
**Owner:**
**Last updated:**

## 1) KEV items relevant to us (this period)
| CVE | Product | Where it exists (systems/app) | Internet-facing? | Owner | SLA (7/14/30) | Status | Notes |
|---|---|---|---:|---|---|---|---|

## 2) Fast-exploitation KEV timeline (first 24 hours)
Use this when KEV activity involves active exploitation, edge/admin exposure, or credible reports of ransomware follow-on within hours.

### 0–2 hours
- Confirm product ownership, affected versions, and every exposed instance.
- Decide whether the product is internet-facing, admin-plane reachable, or heavily privileged.
- Move the item into emergency handling if exposure plus active exploitation is credible.
- Restrict access immediately, for example VPN-only admin, trusted IP allowlist, or temporary external isolation.
- Export logs, config snapshots, and recent admin/auth events before major changes.

### 2–8 hours
- Choose patch now vs temporary mitigation, with patch as the default when stable fixes exist.
- Validate backup, rollback, and vendor guidance.
- Patch or hotfix a representative non-prod system if that can be done quickly without creating delay.
- Patch secondary/DR systems first when appropriate, then production.
- Start hunt queries for suspicious admin actions, new accounts, remote execution attempts, or unusual outbound traffic.

### 8–24 hours
- Confirm exposed vulnerable versions are removed or compensating controls are documented and approved.
- Review privileged account changes, token activity, and remote-management exposure.
- Send a leadership update with current status, service impact, residual risk, and next decision time.
- Capture follow-up hardening actions, including permanent management-plane restrictions and monitoring gaps.

## 3) Compensating controls (if not patched on time)
| CVE | Control applied | Evidence link | Expiration date | Approved by |
|---|---|---|---|---|

## 4) Evidence checklist (minimum)
- Patch/upgrade record or vendor mitigation applied
- Validation scan result (or config verification)
- Monitoring note (EDR/logging query) for attempted exploitation
- Leadership or risk-owner approval for any delay beyond the target window

## 5) Next review date
- [Date]
