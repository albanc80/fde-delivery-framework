# Capstone: Harbor Maintenance
All evidence is fictional. Open the staged evidence files in order. Prepare your frame and prediction before reading later results. Planned practice: 125 minutes.

## Stage 1: discovery (25 minutes)
Sponsor request: automate maintenance request assignment and closure. Supervisor Elena owns priority and closure decisions. Twelve technicians submit requests through a form. Asset identifiers are sometimes absent. Two requests may refer to the same fault. Urgent text may describe a safety condition. No tool may change equipment, close a request, or replace an authoritative operating procedure.
Read capstone-evidence/stage-1.json. Produce a Site Map v0/v1, a say/do gap entry, and a Frame Card agreed within the role-play. Distinguish sponsor expectations from supervisor authority. Use the source frameworks' known/assumed/unknown discipline.

## Stage 2: build and predict (45 minutes)
Adapt the local lab to maintenance categories: electrical, mechanical, inspection and manual. Add an asset identifier requirement and a visible escalation flag for urgent requests. Missing identifiers need clarification. Ambiguous or unmatched requests remain manual. A duplicate flag assists review and must not delete data.
Use the provided starter function, completed support-lab implementation and tests as references. Write your maintenance tests. Keep suggestion and reviewed decision separate. Record a prediction before running your evaluation. Suggested exercise frame: median review time no greater than 12 minutes, at most one wrong final assignment in twelve eligible tasks, human approval retained. These thresholds are instructional choices.

## Stage 3: constraint injection (15 minutes)
Open stage-2-constraint.json after your first implementation. The customer integration is unavailable and external model calls are prohibited. Revise your decision record and demonstrate a permitted local fallback. List what it proves and what remains untested.

## Stage 4: two readings (20 minutes)
Open stage-3-results.json. First reading: the fictional assisted median is 11 minutes, with two wrong assignments in twelve tasks. The speed target passes; the quality guardrail fails. Decide the gate without changing the threshold.
Second reading after a revised controlled rollout: six of twenty eligible requests use assistance. The agreed adoption target was 60 percent. Investigate why usage is 30 percent. Do not report adoption only among completed users.

## Stage 5: distill and defend (20 minutes)
Submit the Site Map, Frame Card, prediction, running thin slice, tests, constraint decision, both delta entries, landing checklist, ownership and recovery plan, distill pack, and one-page executive memo. Demonstrate one independent maintainer action. Preserve versions and source references.

## Rubric: seven dimensions, 0–4 each
Discovery: evidence distinguishes the stated request from the real decision.
Delivery: a complete path tests the main uncertainty within constraints.
Engineering: validation, review boundaries, failure behavior and observability work.
Adoption: eligible-work denominator, task fit and second reading remain visible.
Judgment: options and choices weigh evidence, value, risk and reversibility.
Learning: timestamped prediction, honest deltas and revised beliefs connect.
Reuse: a conditional pattern, maintainable primitive and capability handover exist.
For each: 0 absent; 1 described; 2 partly demonstrated; 3 demonstrated with connected evidence; 4 demonstrated with limitations, transfer conditions and independent checking.
Proposed pass: at least 20/28 plus every mandatory gate. This is an educational rubric, not an accredited standard.

## Mandatory gates
No unauthorized messages, equipment actions, priority changes or closure. No invented or relabeled evidence. Prediction precedes results. Both Sense readings appear. Unmet quality or adoption thresholds are acknowledged. Simulated and real evidence remain distinct. If any gate fails, revise and reassess regardless of total score.

## Reference decision
Iterate after the first reading because two errors exceed the original limit. Diagnose ambiguous labels and missing asset handling. Preserve review authority. The failed integration makes production integration untested. After the second reading, investigate duplicate entry and trust before scaling. Distill the review and escalation contract; do not assume support ticket categories transfer to maintenance.
