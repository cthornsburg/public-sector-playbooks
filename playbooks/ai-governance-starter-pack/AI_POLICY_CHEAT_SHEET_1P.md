# City/County AI Policy — 1‑Page Cheat Sheet (NIST AI RMF-aligned)

**Purpose:** quick guidance for staff and supervisors on safe AI use.

**Golden rule:** If you wouldn’t post it on a public website, don’t put it into a public AI tool.

---

## 1) Allowed / Restricted / Prohibited (fast decisions)

### Allowed (Tier 1) — OK without formal approval
Use AI with **public information only** and **no sensitive context**.
- Draft general public messaging (no case details)
- Brainstorm agenda topics / training ideas
- Rewrite a public webpage for clarity

**Must:** validate facts; don’t treat AI output as authoritative.

### Restricted (Tier 2) — Department approval + documented use case
Use AI for internal support where data is **Internal (non-sensitive)**.
- Summarize internal policies/procedures
- Create training outlines from non-sensitive materials
- Translate internal documents that contain **no restricted data**

**Must:** document the use case and keep outputs in approved repositories.

### High-impact / Sensitive (Tier 3) — AI Governance Lead + Security + Legal review
Any of the following triggers Tier 3 review:
- Resident/employee **PII** or sensitive data
- Any workflow that impacts eligibility, enforcement, discipline, benefits
- Any automated scoring/ranking or decisioning
- Any plugins/API integrations or automation

**Must:** human review steps, logging, vendor controls, and an approved use case.

### Prohibited (Tier 4) — Not allowed
- Entering **restricted data** into public AI tools
- Using AI as the **sole source** for high-impact decisions
- Unvetted browser extensions/plugins that touch City/County data
- Pasting secrets (passwords, API keys), network diagrams, vuln data, IR details

---

## 2) Data you must NOT put in public AI tools
- Resident PII (SSNs, IDs, DOBs, addresses when paired with name)
- Employee HR/medical/performance data
- Investigative / law enforcement sensitive information
- Credentials, API keys, security configs
- Incident response details not intended for public release

---

## 3) Human responsibilities (always)
- **Verify**: check claims, numbers, and citations
- **Accountability**: you own the output and outcomes
- **Transparency**: disclose AI use when it materially affects service decisions

---

## 4) If you’re unsure
Stop and ask via the approved channel:
- **Department head** (Tier 2)
- **AI Governance Lead / IT Security / Legal** (Tier 3)

---

## 5) Incident reporting
Report immediately if:
- sensitive data was pasted into an AI tool
- an AI account looks compromised
- AI output caused (or could cause) harmful or unlawful action

Contact: **[Security contact / help desk / incident hotline]**
