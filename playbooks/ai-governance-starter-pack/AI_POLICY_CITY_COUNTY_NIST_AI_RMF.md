# City/County AI Acceptable Use & Governance Policy (NIST AI RMF-aligned) — v0.1

**Audience:** City/County government departments, boards, commissions, and contractors

**Status:** Template for adaptation (not legal advice)

**Framework alignment:** NIST AI Risk Management Framework (AI RMF 1.0) — Govern / Map / Measure / Manage

**Effective date:** [YYYY-MM-DD]

**Owner:** [Title, e.g., CIO / CISO / Chief Data Officer]

**Applies to:** All City/County employees, contractors, interns, volunteers, and third parties using City/County systems or data.

---

## 1) Purpose
This policy establishes minimum requirements for the safe, lawful, and accountable use of Artificial Intelligence (AI) systems by the City/County. The City/County will use AI to improve service delivery and operations while reducing risks to residents, employees, critical services, privacy, security, and public trust.

## 2) Scope and definitions
### 2.1 AI system (definition)
An **AI system** includes tools that generate, summarize, classify, recommend, predict, detect, or otherwise produce outputs that influence decisions or actions (including generative AI and machine-learning models).

### 2.2 Covered systems and data
This policy covers:
- AI used on City/County-owned devices and accounts
- AI used to process City/County information (even on personal devices)
- AI tools integrated into City/County workflows (e.g., ticketing, HR screening, document review)

**City/County information** includes any non-public or sensitive data, including resident data, employee data, operational data, investigative data, and any data protected by law or contract.

## 3) Guiding principles (NIST AI RMF — Govern)
The City/County will ensure AI use is:
- **Accountable:** A human owner is responsible for each AI use case and tool.
- **Transparent:** Residents and staff are informed when AI materially affects services or decisions.
- **Secure by design:** AI tools must meet baseline cybersecurity requirements.
- **Privacy-protective:** Data minimization and lawful processing are mandatory.
- **Fair and non-discriminatory:** AI must not create unlawful disparate impacts.
- **Reliable:** AI outputs must be validated for the intended use.

## 4) Roles and responsibilities
### 4.1 AI Governance Lead
[Name/Title] is responsible for policy oversight, maintaining the AI inventory, and coordinating risk decisions.

### 4.2 Department AI Use Case Owner
Each AI use case must have a designated owner responsible for:
- documenting the use case (purpose, data types, users)
- validating output quality
- ensuring training/communications for staff
- ensuring incident reporting and corrective actions

### 4.3 IT/Security
IT/Security is responsible for:
- approving technical integrations
- monitoring, logging, and incident response
- vendor security due diligence

### 4.4 Procurement / Legal / Records
Procurement/Legal/Records support:
- contract language and vendor risk requirements
- retention and public records considerations
- required notices and disclosures

## 5) AI inventory and approval process (NIST AI RMF — Map)
### 5.1 Inventory requirement
All AI tools and AI-enabled features used with City/County data must be recorded in the **AI Use Case Register**.

Minimum fields:
- tool/vendor, version
- use case description
- department owner
- data types involved (Public / Internal / Confidential / Restricted)
- outputs and decisions influenced
- integration method (web, API, plugin)
- retention/logging expectations

### 5.2 Approval levels
AI use is categorized into tiers:

**Tier 1 — Allowed (no formal approval required)**
Allowed with **public information only**, no integration, and no decisions affecting individuals.
Examples:
- drafting generic public communications using non-sensitive prompts
- brainstorming agenda topics with no non-public context

**Tier 2 — Restricted (department approval + documented use case)**
Allowed only with documented use case and department head approval.
Examples:
- summarizing internal policies (non-sensitive)
- generating internal training outlines
- translation of internal documents that do not contain restricted data

**Tier 3 — High-impact / Sensitive (AI Governance Lead + Security + Legal review)**
Requires formal review before use.
Examples:
- any use involving resident PII, employee PII, protected health info, student data, payment data
- any use that materially affects eligibility, enforcement, disciplinary actions, or benefits
- any automated decisioning or scoring
- any integration via API or plugin

**Tier 4 — Prohibited**
Not allowed under any circumstances.
Examples:
- using public AI tools to process restricted data
- deploying AI to make final enforcement/discipline decisions without meaningful human review
- tools that cannot meet contractual security/privacy requirements

## 6) Data handling rules (privacy + security)
### 6.1 Prohibited data in public AI tools
Unless explicitly approved in writing for a vetted enterprise system, the following **must not** be entered into public AI tools:
- resident PII (names + addresses, SSNs, IDs, DOB, etc.)
- employee HR data (disciplinary, medical, performance)
- law-enforcement / investigative details
- credentials, API keys, network diagrams, vulnerability data
- incident response details not intended for public release

### 6.2 Data minimization
Prompts must use the minimum data needed. Use placeholders where possible.

### 6.3 Retention and records
AI outputs created in the course of government business may be public records and subject to retention. Staff must store official outputs in approved repositories (document management, ticketing, case systems) per records schedules.

## 7) Operational use rules (acceptable use)
### 7.1 Human accountability
AI output is **advisory** unless explicitly approved for automation. Users remain responsible for:
- verifying accuracy
- checking citations/claims
- ensuring compliance with laws and policy

### 7.2 No sole-source truth
AI output must not be used as the only source for facts in:
- resident communications that could cause harm
- budget/finance decisions
- legal notices or compliance statements

### 7.3 High-impact decisions
For any Tier 3 use, the City/County must maintain:
- documented human review steps
- appeal/recourse pathways when individuals are affected
- periodic evaluation for bias and error

## 8) Vendor/procurement requirements (NIST AI RMF — Measure/Manage)
AI vendors/tools used with non-public data must provide, at minimum:
- clear data use terms (no training on City/County data without explicit opt-in)
- security controls (MFA, SSO where possible, encryption in transit/at rest)
- breach notification timelines
- logging/audit features
- retention/deletion controls
- subprocessor disclosure
- support for legal hold / records needs (as applicable)

## 9) Security, logging, and incident reporting
### 9.1 Logging
For Tier 3 systems, the City/County must enable logging sufficient to support:
- user accountability
- misuse detection
- incident response and investigations

### 9.2 Incident reporting
Report suspected AI-related incidents immediately to [Security contact], including:
- suspected data exposure via prompts/uploads
- account compromise
- AI output causing harmful or illegal action

## 10) Training and communications
All staff must complete annual training that covers:
- what data is prohibited in public AI tools
- how to validate AI outputs
- how to report incidents

## 11) Enforcement
Violations may result in:
- removal of access
- disciplinary action up to and including termination
- contract remedies for vendors/contractors

## 12) Review cycle
This policy will be reviewed at least annually and after:
- major AI deployments
- significant incidents
- changes in law or CSA/state guidance

---

## Appendix A — Quick “Allowed / Restricted / Prohibited” cheat sheet

**Allowed:** Public-only drafting/brainstorming; no sensitive context.

**Restricted:** Internal non-sensitive summarization/translation; documented use case.

**Prohibited:** Any restricted data in public tools; sole-source high-impact decisions; unvetted plugins/integrations.

---

## Appendix B — References
- NIST AI RMF 1.0: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI RMF 1.0 PDF: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

(Optionally add: NIST GenAI Profile and any applicable state/county policies.)
