# Incident Triage Intake (Template)

Use this as the initial intake form when an incident is reported. Keep it factual; avoid speculation.

## Reporter / contact
- **Reported by (name/role):**
- **Phone:**
- **Email:**
- **Best call-back window:**

## What happened (first description)
- **What did you observe?** (error message, alert, ransom note text, fraud email, etc.)
- **When did you first notice it?** (CT + timezone)
- **Is it still happening?** (Y/N/Unknown)

## Impact (business)
- **Critical services affected:** (e.g., 911/dispatch, payroll, water, courts, email)
- **Current operational impact:** (none / degraded / down)
- **Safety impact:** (Y/N/Unknown)
- **Data impact suspected:** (PII/PHI/CJIS/financial/unknown)

## Scope (systems/users)
- **Locations / departments impacted:**
- **Systems impacted:** (servers, workstations, cloud services)
- **User accounts impacted:** (known compromised, locked out, suspicious logins)
- **Network indicators:** (IPs/domains/URLs if known)

## Detection & evidence
- **Who/what detected it?** (EDR, SIEM, vendor, user report)
- **Alerts/tickets/IDs:** (EDR detection IDs, SIEM rule name, ticket #)
- **Screenshots/files captured:** (where stored)

## Current actions taken (IMPORTANT)
- **Changes already made:** (reboots, password resets, isolations, blocks)
- **Vendors contacted:** (ISP, MSP, cloud provider)

## Immediate next steps (checklist)
- [ ] Start/assign **incident log** + scribe (see `templates/incident-log.md`)
- [ ] Stabilize **out-of-band communications**
- [ ] Preserve logs/telemetry **before major changes** (see `templates/evidence-collection-checklist.md`)
- [ ] If active compromise suspected: isolate affected hosts **without wiping evidence**

## Notes

