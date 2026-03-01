# CSF 2.0 Accuracy Hardening TODO

Last reviewed: 2026-02-28 (America/Chicago)

## Findings

The workbook dataset currently includes legacy CSF 1.1-era category identifiers mixed with CSF 2.0 Govern categories.

Examples observed in `index.html` evidence metadata:

- `ID.BE`
- `ID.GV`
- `ID.RM`
- `ID.SC`
- `PR.AC`
- `PR.IP`

## Required remediation

1. Replace static category/subcategory inventory with authoritative CSF 2.0 Core identifiers from CSRC Reference Tool export.
2. Add `frameworkVersion: "CSF_2_0"` in exported JSON payloads.
3. Add a schema validator that rejects unknown/legacy category IDs.
4. Add a regression check in CI to detect legacy IDs in workbook data.

## Authoritative sources

- CSF 2.0 Core: https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final
- CSRC Reference Tool: https://csrc.nist.gov/Projects/cybersecurity-framework/Filters#/csf/filters
