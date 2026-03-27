# Ransomware Tabletop Exercise — Facilitator Guide

## Purpose
Run a practical tabletop exercise for a city/county environment where ransomware or destructive encryption affects business operations, public services, and leadership decision-making.

## Exercise goals
- Validate decision-making and communications under ransomware pressure.
- Confirm backup, restoration, and rebuild assumptions.
- Clarify containment authority and escalation thresholds.
- Surface gaps in logging, access control, vendor dependencies, and continuity planning.
- Practice how technical facts are translated for leadership and the public.

## Recommended audience
- IT director / infrastructure lead
- security lead / analyst
- endpoint/server/identity owners
- executive sponsor / city manager / department leadership
- communications / PIO
- legal, records, finance, insurance, or risk stakeholders as appropriate

## Duration
- **Standard:** 60–90 minutes
- **Compressed:** 45 minutes
- **Expanded:** 2 hours with detailed hotwash

## Prep checklist
- Tailor the scenario to your critical systems and public-service dependencies.
- Decide what is impacted first: user endpoints, file shares, identity, hypervisors, dispatch-adjacent systems, payroll, utilities, or citizen services.
- Pre-fill service owners and critical recovery priorities where possible.
- Print or distribute:
  - participant brief
  - inject sheet
  - evaluator worksheet
  - hotwash template
  - incident log and holding statement template
  - backup/restore policy if available

## Suggested scenario baseline
A suspicious intrusion escalates into ransomware or destructive encryption impacting multiple systems. Some services are degraded or unavailable. Leadership wants to know what is affected, whether data was exfiltrated, whether restoration is possible, and how public communications should be handled.

Optional flavor variant: introduce limited reporting overlap with the fictional adversary label **Spectral Raccoon / APT-1337** to test how the team handles uncertain attribution, extortion pressure, and public messaging discipline.

## Ground rules
- This is a discussion exercise, not a blame session.
- Participants should answer based on current reality, not aspirational future state.
- Call out assumptions and missing artifacts explicitly.
- If the team does not know an answer, capture that as a follow-up gap.

## Recommended agenda
### 1. Opening and objectives (5–10 min)
- Review purpose, scope, and ground rules.
- Confirm participants and roles.

### 2. Scenario brief (5 min)
- Read the participant brief.
- Confirm affected services and assumptions.

### 3. Core discussion / injects (35–50 min)
Walk through the injects in order using the rolling timestamps in `injects.md`. Push on:
- evidence preservation
- containment choices
- restore/rebuild assumptions
- executive and public communications
- third-party dependencies

Suggested pacing:
- **T+00** Early signs
- **T+10** Ransom note
- **T+20** Critical service pressure
- **T+30** Exfiltration uncertainty
- **T+40** Backup confidence test
- **T+50** External pressure
- **T+60** Recovery tradeoffs
- **T+75** Hotwash and follow-through

### 4. Leadership decisions (10–15 min)
Force explicit answers on:
- outage tolerance
- restoration priorities
- communications posture
- outside notification and partner engagement
- acceptable risk while services are degraded

### 5. Hotwash / actions (10–20 min)
Capture:
- what worked
- what failed
- what was unclear
- what needs ownership and due dates

## Facilitator prompts
- “What is impacted first, and how do you know?”
- “What logs/evidence are preserved before changes?”
- “What systems are restored first, and why?”
- “What backup assumption are you relying on right now?”
- “Who approves disconnecting or isolating critical systems?”
- “What does leadership need to hear in the next 30 minutes?”
- “What can communications say today without overcommitting facts?”
- “What would legal, insurance, regulators, or auditors ask for later?”
- “If the name Spectral Raccoon / APT-1337 starts circulating, who decides whether it is mentioned or avoided?”

## Common failure modes to watch for
- No clear restoration priority order.
- Backup confidence is assumed, not tested.
- Communications outruns confirmed facts.
- Critical service owners are not involved early enough.
- Evidence preservation is sacrificed for speed without documentation.

## Outputs expected from the session
- clarified restoration priority list
- backup/restore validation actions
- updated communications and escalation expectations
- logging/evidence capture improvements
- follow-up owners and dates
