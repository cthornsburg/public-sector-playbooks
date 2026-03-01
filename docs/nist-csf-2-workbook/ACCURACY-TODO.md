# CSF 2.0 Accuracy Hardening TODO

Last reviewed: 2026-02-28 (America/Chicago)

## Status update

- ✅ Phase 1 complete: removed known legacy CSF 1.1 identifier prefixes from workbook item IDs and evidence labels:
  - `ID.BE` → `GV.OC`
  - `ID.GV` → `GV.OV`
  - `ID.RM` → `GV.RM`
  - `ID.SC` → `GV.SC`
  - `PR.AC` → `PR.AA`
  - `PR.IP` → `GV.PO`
- ✅ Guardrail script in place: `validate_ids.py` now fails on reintroduction of those legacy prefixes.

## Remaining work

1. Replace static item inventory with direct export from the authoritative CSF 2.0 Reference Tool.
2. Add `frameworkVersion: "CSF_2_0"` in exported JSON payloads.
3. Add schema validation for category/subcategory IDs against an authoritative allowlist.
4. Add CI regression check to run `validate_ids.py`.

## Authoritative sources

- CSF 2.0 Core: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- CSRC Reference Tool: https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters
