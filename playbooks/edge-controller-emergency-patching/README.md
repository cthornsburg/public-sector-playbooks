# Edge Controller Emergency Patching (Municipal/Public Sector)

Playbook for urgent patching of internet-exposed edge controllers (with Cisco SD-WAN examples).

## Purpose
Provide a fast, repeatable process to reduce active-exploitation risk without creating uncontrolled outages.

## When to use this
- CISA KEV or vendor advisory indicates active exploitation.
- High/critical CVE affects your edge controller platform.
- Credible threat intel ties current campaigns to your product/version.

## Main playbook
- `EDGE_CONTROLLER_EMERGENCY_PATCH_PLAYBOOK.md`

## Scope
- Cisco SD-WAN/vManage/vSmart class controllers
- Similar internet-exposed network/security management controllers

## Outcome targets
- Decision to patch/mitigate made in ≤2 hours
- First production patch/mitigation in ≤8 hours
- External exposure validated and documented same day
