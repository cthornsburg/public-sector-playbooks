# Patch SLA Table (Simple)

This is a starting point for cities/counties. Tune based on your constraints.

| Category | Definition | Target remediation time | Examples |
|---|---|---:|---|
| **7-day (Emergency)** | KEV + internet-facing OR KEV marked ransomware use OR active exploitation confirmed | 7 days | VPN gateways, email servers, public web apps |
| **14-day (High)** | KEV affecting privileged apps or high-value internal services | 14 days | Helpdesk/RMM, hypervisors, identity tooling |
| **30-day (Standard)** | Other critical patches not in KEV (or KEV with low exposure + compensating controls) | 30 days | Internal apps with tight segmentation |

**Rule:** anything that exceeds SLA requires (1) compensating controls and (2) explicit risk acceptance.
