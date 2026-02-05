# DFIR: The First 24 Hours (Public Sector)

A concise, practical checklist for the first day of an incident.

## Goals
- Preserve evidence
- Contain safely (without destroying artifacts)
- Establish clear command-and-control
- Start reliable communications

## Do this immediately (0–2 hours)
1) **Start an incident log** (who/what/when). One person owns it.
2) **Stabilize communications** (out-of-band contact list, bridge line/chat).
3) **Preserve**: EDR alerts, firewall/VPN logs, email security logs, SIEM, cloud audit logs.
4) **Snapshot before changes** when possible (VM snapshots, host triage images, config exports).
5) **Identify scope**: what systems are impacted, what is business-critical.

## Containment (2–8 hours)
- Segment affected subnets; restrict east-west.
- Disable compromised accounts; rotate credentials with a plan.
- Block known IOCs at edge + EDR.

## Recovery prep (8–24 hours)
- Validate backups (restore test) before trusting them.
- Decide: rebuild vs clean.
- Plan communications (internal, leadership, public-facing).

## Templates
See:
- `templates/incident-log.md`
- `templates/evidence-collection-checklist.md`
- `templates/initial-statement-holding.md`
