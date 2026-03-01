#!/usr/bin/env python3
"""Simple guardrail: fail if known legacy CSF category IDs exist in index.html."""
from pathlib import Path
import sys

legacy = ["ID.BE", "ID.GV", "ID.RM", "ID.SC", "PR.AC", "PR.IP"]
text = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
found = [x for x in legacy if x in text]
if found:
    print("Legacy CSF identifiers detected:", ", ".join(found))
    sys.exit(1)
print("OK: no known legacy CSF identifiers detected")
