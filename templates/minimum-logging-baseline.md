# Minimum Logging Baseline (Starter) — Public Sector

Goal: have enough logs to answer the first questions during an incident:
- What happened?
- When did it start?
- Which accounts/systems were involved?
- Is it contained?

## Baseline (collect/retain if you can)
### Identity / authentication
- **Directory auth logs** (AD/DC security logs, Entra ID sign-in logs)
- **MFA events** (prompts/approvals/denies)
- **Privileged account activity** (admin group changes, role assignments)

### Email / collaboration
- Email security events (phish detections, clicks, quarantines)
- Mailbox access + forwarding rule changes
- OAuth app grants / consent events

### Endpoint security
- EDR alerts + telemetry export capability (process tree, network, file events)
- AV/EDR policy change logs

### Network edge
- Firewall allow/deny + NAT logs (if available)
- VPN auth logs + connection metadata
- DNS logs (resolver logs if you run them)
- Web proxy logs (if used)

### Servers / critical apps
- Windows event logs for critical servers (auth, service installs, scheduled tasks)
- Application logs for ERP/finance/public-facing portals

### Cloud / infrastructure
- Cloud audit logs (Azure Activity, M365 Unified Audit Log, AWS CloudTrail, GCP Audit Logs)
- Admin actions on storage/email/identity platforms

## Retention (starter guidance)
- **Hot (searchable):** 30 days minimum
- **Warm (archived):** 180 days preferred (budget-dependent)

## During an incident (export now)
- Export the relevant logs to a case folder.
- Record export time ranges + hashes when possible.
- Avoid “cleanup” scripts until DFIR confirms evidence needs.

