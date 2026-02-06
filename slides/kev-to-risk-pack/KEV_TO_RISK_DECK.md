# KEV-to-Risk (Executive Deck) — 5 Slides

> Copy/paste into Slides/PowerPoint as-is, or convert to a formal template later.

## Slide 1 — Executive Summary (What changed + why you care)
- This month: **[X]** new KEVs relevant to cities/counties
- Top risks (plain English):
  - **Internet-facing** services (VPN/email/web portals) are common entry points
  - KEV items imply **active exploitation in the wild**
- Our posture (one line): **[On track / At risk]** based on patch status

## Slide 2 — The KEV signal (why KEV is different)
- KEV ≠ theoretical vulnerability list
- KEV = **confirmed exploitation** (real attacker tradecraft)
- Governance ask: we prioritize KEV remediation over “routine patching”

## Slide 3 — Exposure in our environment (map to asset classes)
Fill the table:

| Asset class | Examples | Internet-facing? | Owners | KEV impact (Y/N) | Current status |
|---|---|---:|---|---:|---|
| Remote access | VPN / ZTNA | Yes | | | |
| Email/collab | Mail servers / M365 | Yes/No | | | |
| Public web | CMS / portals | Yes | | | |
| Privileged apps | Helpdesk, RMM | Usually | | | |
| Core infra | AD, hypervisors | No (should be) | | | |

## Slide 4 — Plan & timelines (7/14/30)
- 7 days: **KEV + internet-facing (always)**; also KEV items with known ransomware use
- 14 days: high-risk internal systems + privileged apps
- 30 days: everything else (or compensating controls documented)

**Risk acceptance:** anything beyond SLA requires explicit approval and a compensating control.

## Slide 5 — Asks (what leadership must decide)
- Approve:
  - patch windows / downtime
  - emergency changes for KEV items
  - funding for visibility (asset inventory + vuln management + logging)
- Assign:
  - executive sponsor
  - monthly owner for this cadence
