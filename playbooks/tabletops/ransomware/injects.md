# Ransomware Tabletop Exercise — Injects

Use the rolling timestamps below to keep the session moving. Adjust pacing as needed for a 45-minute compressed run or a 90-minute standard run.

## T+00 — Early signs
Unusual login alerts and endpoint security hits appear on a finance workstation. Shortly after, users report inaccessible file shares.

**Decision prompts**
- Who leads initial triage?
- What evidence is preserved immediately?
- What systems are checked first for scope?

## T+10 — Ransom note
A ransom note appears on multiple systems. Shared drives are unavailable. Leadership wants to know whether this is isolated or widespread.

**Decision prompts**
- What gets isolated now?
- Who approves disruptive containment steps?
- What is the first leadership brief?

## T+20 — Critical service pressure
A department reports impact to a critical service such as permitting, utilities, payroll, or dispatch-adjacent operations.

**Decision prompts**
- What is the continuity plan?
- Which service gets priority, and who decides?
- What manual fallback exists?

## T+30 — Exfiltration uncertainty
Threat intelligence or EDR suggests possible data staging or outbound activity, but confirmation is incomplete. One vendor note says the activity is consistent with a financially motivated cluster referred to in this exercise as **Spectral Raccoon / APT-1337**, while another source says the evidence is still too thin for confident attribution.

**Decision prompts**
- When do you move from outage response to possible breach response?
- Who needs to be engaged now?
- What can be said without overstating facts?
- How do you handle uncertain actor naming in leadership or public updates?

## T+40 — Backup confidence test
The team believes backups exist, but the last restore test was months ago and critical systems may have hidden dependencies.

**Decision prompts**
- What do you restore first?
- What must be verified before trusting a restore path?
- What if restoration is slower than leadership expects?

## T+50 — External pressure
Insurance requests artifacts and a timeline. A local reporter asks whether citizen data is affected and whether the incident is tied to **Spectral Raccoon / APT-1337**, because the name is circulating in rumor or a third-party notification. Staff are posting rumors internally.

**Decision prompts**
- Who owns external communications?
- What documentation must be preserved?
- What is the holding statement?
- What do you say about attribution when the evidence is still incomplete?

## T+60 — Recovery tradeoffs
You can recover some services quickly with partial capability, or wait longer for a cleaner rebuild.

**Decision prompts**
- What matters more right now: speed, assurance, or service coverage?
- Who accepts the tradeoff?
- What is the message to affected departments?

## T+75 — Hotwash and follow-through
The immediate crisis stabilizes, but the session reveals weak backup validation, unclear restoration priorities, and inconsistent communication paths.

**Decision prompts**
- What three improvements happen first?
- Who owns the after-action plan?
- What gets tested again within 30–60 days?
