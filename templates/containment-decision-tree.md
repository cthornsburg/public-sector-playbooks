# Containment Decision Tree (Starter)

This is a **starter** decision aid. Always preserve evidence first when feasible.

## 0) First question: is there active threat actor activity *right now*?
Signals: new suspicious logins, EDR active alerts, lateral movement, encryption in progress.

### If YES (active):
1) **Stabilize comms** (out-of-band) + start incident log.
2) **Preserve what you can quickly** (EDR export, firewall/VPN/auth logs).
3) **Isolate affected hosts** (EDR network containment / switch port shutdown / VLAN quarantine).
4) **Stop known bad**: block IOCs, disable confirmed compromised accounts.
5) **Do NOT** mass-reimage or wipe until DFIR says evidence is sufficient.

### If NO/UNKNOWN (not obviously active):
1) Preserve logs/telemetry first.
2) Increase monitoring/alerting for key signals.
3) Begin scoped containment (password resets for affected users, revoke tokens, remove persistence).

## 1) Account compromise?
- If you suspect credential theft:
  - Disable affected accounts (or force password reset) **after** collecting auth logs.
  - Revoke sessions/tokens (M365/Entra/Google) and remove suspicious OAuth apps.

## 2) Ransomware indicators?
- If encryption is occurring:
  - Prioritize isolating affected segments/hosts.
  - Preserve ransom note samples + file extensions + process names + EDR details.
  - Validate backups (offline/immutable) **before** trusting restore.

## 3) Public-facing system compromise?
- If web server/app suspected:
  - Capture current state (VM snapshot/image, configs, web logs).
  - Consider temporary takedown or WAF rules to stop exploitation.

## 4) Communication triggers
- If PII/PHI/CJIS/financial data potentially accessed:
  - Engage leadership + legal/IR vendor + insurance (if applicable).
  - Use a holding statement template (see `templates/initial-statement-holding.md`).

