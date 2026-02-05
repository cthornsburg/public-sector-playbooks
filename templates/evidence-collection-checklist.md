# Evidence Collection Checklist (Starter)

## Guiding principles
- Collect *before* making changes when feasible.
- Record exact times, hostnames, usernames, IPs.
- Preserve logs with integrity (export + hash if possible).

## Collect first
- EDR detections + raw telemetry exports
- Firewall/VPN logs (auth events)
- Email security logs (phish, MFA prompts, OAuth grants)
- Domain controller auth logs
- Cloud audit logs (M365/Azure/Google)

## Endpoint triage (if available)
- Running processes, network connections
- Scheduled tasks/services
- Persistence locations
- Recent user logons
