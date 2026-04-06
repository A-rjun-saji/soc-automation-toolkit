# SOC Automation Toolkit

Python security automation tools built by a SOC Analyst L1.
Domains: Cybersecurity Automation | Cloud Security | DFIR | Detection Engineering

---

## Phase 1 — Foundations

### CLI Log Line Classifier
A command-line tool that classifies Windows Event Log lines by Event ID.

**What it does:**
- Takes a raw Windows event log line as input
- Extracts the Event ID using string parsing
- Classifies it — 4624 (Logon), 4625 (Failed Logon), 4688 (Process Creation)
- Prints a formatted alert report
- Handles invalid input gracefully with error handling
- Runs continuously until user exits

**How to run:**
python phase1/log_classifier.py

**Example input:**
2026-04-05 FAILED LOGIN user=admin src=1.2.3.4 event_id=4625

**Example output:**
========================================
EVENT CLASSIFICATION REPORT
Log Line   : 2026-04-05 FAILED LOGIN user=admin src=1.2.3.4 event_id=4625
Event ID   : 4625
Description: Failed Logon — possible brute force

---

## Roadmap
- Phase 1 ✅ — Foundations (CLI log classifier)
- Phase 2 🔄 — Core Python (IOC Enrichment Tool)
- Phase 3 ⏳ — Intermediate (Full SOC Automation Toolkit)
