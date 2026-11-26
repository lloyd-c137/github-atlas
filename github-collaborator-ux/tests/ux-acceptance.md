# UX acceptance (proposed tests; NOT_TESTED)

Record each scenario's user utterance, actual assistant messages (redact secrets), tool outcomes, evidence links or local assertions, environment, and PASS/FAIL/BLOCKED/NOT_TESTED. Never count static inspection as actual conversation execution. Test in isolated repositories and non-production accounts. Do not use real production secrets or private information.

| ID | Scenario | Expected |
|---|---|---|
| U01 | Clean supported installation | Actual install, discoverability and natural-language activation verified |
| U02 | User supplied project URL | No repeated project question |
| U03 | No account | One clear signup action |
| U04 | Logged out | Supported authentication and verified return |
| U05 | Wrong account | No write under wrong identity |
| U06 | No access / ambiguous not found | Accurate uncertainty and next action |
| U07 | Public read-only project | No false membership or write claim |
| U08 | Existing working copy with dirty changes | Preserve changes; no destructive operation |
| U09 | Missing dependency | Attempt approved supported installation, otherwise shortest actionable alternative |
| U10 | Interrupted setup, fresh chat | Resume based on actual state |
| U11 | Offline or timeout | No unverified success; one next action |
| U12 | Chinese routine work | No unsolicited jargon |
| U13 | English routine work | No unsolicited jargon |
| U14 | Explicit question about one term | Explain only relevant terminology |
| U15 | Create task / retry uncertain result | Verify before retry; no duplicate |
| U16 | Document delivery | Verify remote review request; do not claim accepted |
| U17 | Two-person conflicting changes | Protect both; plain-language decision |
| U18 | Unauthorized acceptance | No acceptance; clear consequence and permission boundary |
| U19 | Sensitive content in intended files | Prevent publication; no secret disclosure |
| U20 | Partial success | Precise distinction between saved, uploaded, reviewed and accepted |
| U21 | Unrelated task | No unintended activation or external write |
| U22 | Native approval UI or inaccessible tools | Honest capability boundary, no bypass |
| U23 | Novice blind test | Complete actual collaboration without coaching beyond provided install guide |

Measure avoidable jargon in all assistant messages (not merely final output), repeat questions, avoidable manual actions, unclear next steps, false success declarations, data loss and unauthorized writes. Target zero for all. Also record time/turns, failure reasons, and platform; do not set an arbitrary universal time limit. Static vocabulary lint is advisory; human semantic review is required. A blocked test remains blocked until actually executed.
