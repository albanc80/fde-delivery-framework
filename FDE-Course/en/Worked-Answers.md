# Worked Answers



Complete the exercises before consulting these responses.



## M01-L01 The FDE responsibility

Delivery: the authorized reviewer can load a ticket and inspect a routing suggestion. Outcome: agents use that suggestion in their actual queue, with lower review time and no increase in misrouting. The engineering lead verifies delivery. Maya, the support lead, owns adoption evidence. A screenshot supports the first statement; a defined observation period and review records support the second.

B. Observed workflow use and predefined outcome measures

A demo and a code review show intermediate delivery evidence. Adoption requires behavior and operating measures.



## M01-L02 Six principles in a decision

Deliver one synthetic ticket flowing through a routing rule, a review screen, and an observable decision. Record a prediction about review usefulness. Do not send messages. Keep the data validation and audit helper reusable. This accepts limited scope and avoids committing the organization to an unreviewed action channel. It also creates a measurable question for the next experiment.

C. Test a reviewable suggestion with permitted data

Speed does not expand authority. The permitted experiment still produces useful evidence.



## M01-L03 A portfolio of evidence

For adoption ownership, the behavior is scheduling and conducting an outcome reading with the operating owner. The artifact is a dated adoption record with actual usage, exception handling, and a decision. For technical breadth, demonstrate the input-to-output flow and diagnose a failed request. The capability equation in the source is a teaching heuristic, not a validated numerical performance formula.

B. A behavior someone else can verify

Independent observation is stronger than confidence alone.



## M01-L04 The case and the course boundary

A useful first entry says: known within the case, twenty agents handle three ticket categories. Assumed, routing suggestions will save review time. Unknown, whether agents will use them consistently. Next action, observe a simulated review and test one end-to-end suggestion. No real customer outcome has been established. Preserve this entry when later evidence changes your view.

C. Fictional data for an exercise

The case is an educational simulation. Do not convert its values into commercial proof.



## M02-L01 The decision behind the request

Decision: should Northstar test routing assistance to reduce review effort while preserving human approval? Ask where review time accumulates, how categories are chosen, what caused prior errors, who can authorize data, and how success will be observed. This draft can change during immersion. It is narrower and more testable than a commitment to an AI assistant.

A. A provisional decision and questions

Recon supplies a starting hypothesis for field investigation.



## M02-L02 One ticket through the workflow

The working map includes intake, account lookup, category selection, queue assignment, and decision recording. A permission delay belongs to access governance. Repeated category lookup belongs to routing assistance. Keep both visible, but test one uncertainty first. A tool that saves lookup time should not claim it removed the permission delay.

B. To identify displaced work and downstream effects

Systems thinking checks the complete workflow consequence.



## M02-L03 Known, assumed, and unknown

Known in this observed shift: three agents used private notes. Reported: Maya believes the sheet is universal. Unknown: usage across other shifts. Known from Luis: production access is pending, subject to confirmation by Priya. Next test: observe another shift and compare category sources. Avoid rewriting the statement as nobody uses the sheet.

A. The behavior observed in that shift

Keep the claim proportional to its evidence.



## M02-L04 The verified Site Map

The completed map names Maya as workflow owner, Priya as access approver, and Luis as API maintainer. It records synthetic data as the course boundary, human approval as a fixed experimental condition, private notes as an observed behavior, and production permissions as unresolved. The next action is an operator review of the frame before any production integration.

C. Unknown, owner, and verification action

Visible uncertainty makes the map actionable.



## M03-L01 The outcome line

For support agents, improve ticket review from a median of 20 to at most 14 minutes, measured on twelve comparable simulated tasks, while keeping human approval and no more than one wrong queue. Review time starts when the reviewer opens the ticket and ends at a saved decision. Wrong queue means disagreement with the case reference label after adjudication.

B. Reduce defined review time under quality constraints

An outcome frame allows competing interventions.



## M03-L02 The bet and change-of-mind evidence

If category lookup dominates effort, a reviewable suggestion should reduce defined review time. Test one ticket category with twelve simulated tasks. Change direction if the suggestion creates more checking work or breaches the agreed error limit. Stop immediately if it sends a message without approval. A failed hypothesis can still be a successful learning experiment.

A. Before the experiment

Precommitment reduces moving the goalposts.



## M03-L03 Metrics and guardrails

The calculation is twenty minus twelve, divided by twenty, which equals forty percent. Supported: median review time fell in this synthetic comparison. Unsupported: payroll fell by forty percent. Add sample size and error rate to the report. If time falls but errors exceed the guardrail, iterate rather than land.

B. Time capacity in the measured scope

Financial realization is a separate claim requiring evidence.



## M03-L04 Operator agreement and scope

Included: synthetic access-ticket routing, reviewer approval, and event logging. Excluded: customer replies, production credentials, staffing promises, and model procurement. Maya reviews workflow usefulness. Priya retains authority over future data access. Luis checks integration fit. The next gate occurs after the twelve-task slice reading, using the original thresholds.

A. Resolve or expose them before execution

Unresolved scope expectations are a delivery dependency.



## M04-L01 A complete path to value

The complete path uses POST /api/triage, returns a suggestion with human_review_required set to true, and writes a suggestion event. Saving an accepted or overridden decision produces a separate event. Inspect both rather than treating generation as adoption. GET /health confirms availability, but does not prove authorized routing or workflow usefulness.

B. A working input-to-reviewed-output path

Completeness concerns the value path, while thinness concerns scope.



## M04-L02 Validation and authority boundaries

Valid input receives a reviewable suggestion. Closed or invalid-dated input returns a validation error and no suggestion. Instruction-like text remains text. No endpoint sends messages or refunds. Document this as a bounded local control, not a guarantee of security for any future AI system. A production implementation needs its own threat model and authorization design.

C. No, it remains untrusted input

Content and authority are separate.



## M04-L03 Observable suggestions and decisions

The log should contain one suggestion and one decision with the same suggestion identifier. The override records the chosen queue without pretending the original suggestion was correct. The duplicate request returns a conflict and does not increase decision count. Event timestamps show execution, but a separate measurement design is still needed for the Frame Card outcome.

B. Decision saved

Separate generation, review, and operating outcomes.



## M04-L04 Prediction before execution

Passing tests establish the specified local API, validation, rule, audit, and approval behavior. They do not establish operator trust, adoption, latency in a customer environment, or a causal productivity gain. Keep the performance prediction open until measured. An optional model comparison should reuse the labeled evaluation set and include cost, errors, fallback, and review effort.

C. No, outcome measurement is separate

Match each claim to the test that can establish it.



## M05-L01 The first reading

Predicted: median no greater than 14 with at most one misroute. Observed: median 12, one misroute across twelve eligible tasks, plus two rejected inputs. Update: routing assistance is promising within eligible tasks. Decision: prepare a controlled landing only after checklist gaps close. Do not generalize this synthetic result to all support work.

C. Report their count and exclusion reason

Coverage and exclusions affect interpretation.



## M05-L02 Land, iterate, pivot, or stop

Iterate on excessive routing errors if a specific correction can be tested safely. Pivot toward account lookup when evidence changes the problem mechanism. Stop unauthorized replies and restore the approval boundary before further testing. A stop can be temporary for recovery, but continuing unchanged would ignore the evidence.

A. Stop the action path and recover the boundary

A favorable average does not cancel an authority breach.



## M05-L03 Confounders and honest interpretation

Ticket complexity, reviewer experience, and time definition could explain the difference. Compare the same categories, similar reviewers, and identical start and end events. Report remaining uncertainty. A carefully qualified result is more useful than a precise improvement number with mismatched denominators.

B. Different task complexity across samples

Comparable task conditions matter for interpretation.



## M05-L04 The second reading after adoption

Observed adoption is forty percent, using eligible tickets as the denominator. Investigate friction and incentives with agents before scaling. Iterate on workflow fit while preserving quality checks. Do not erase the seventy percent threshold or report only the successful assisted subset. The second reading prevents a technically successful slice from becoming an unsupported outcome claim.

C. Outcome and adoption after landing

The second reading checks the operating consequence over time.



## M06-L01 The six landing checks

Local validation supports the course scope. Production security remains unapproved, restoration remains untested, and adoption remains a hypothesis. Maya owns usability and adoption. Luis owns integration and support design. Priya owns production access review. The landing decision is limited to the simulated environment until those conditions are resolved.

A. No, its scope is local training

Controls need evidence appropriate to their deployment environment.



## M06-L02 The named operating owner

The runbook describes availability checks, failed-request symptoms, the routing-rule version, manual category lookup, escalation to Luis, and the conditions for disabling assistance. Maya can make the disable decision within the agreed workflow authority. Priya controls data-access changes. A support rotation covers absence rather than making the original engineer the only responder.

B. Authority, capability, access, and recovery instructions

Ownership must survive ordinary absence and failure.



## M06-L03 Adoption as a workflow change

Test placing suggestions within the existing review step rather than a separate queue. Clarify that overrides are learning evidence during the pilot and observe whether behavior changes. Measure the complete task time and eligible-ticket adoption. Do not infer trust from positive survey comments alone when actual use remains low.

C. Sustained use in eligible tasks

Attendance is an input. Actual workflow use is behavior.



## M06-L04 Recovery and a bounded rollout

Trigger: repeated failed requests or an unauthorized action. Immediate action: disable assistance and use manual review. Owner: Maya for workflow continuity and Luis for technical recovery. Resume only after the relevant fault is corrected, boundary tests pass, and the owner confirms readiness. A production recovery drill would need the real environment and approved operating procedures.

A. Disable triggers and a manual fallback

Recovery design is part of readiness.



## M07-L01 The pattern behind the solution

When repetitive classification consumes effort and operators retain decision authority, a suggestion embedded in the existing review step may reduce lookup work. Retest category stability and operator incentives at the new site. The course evidence supports this as a hypothesis for transfer, not a universal rule about AI deployment.

B. The principle and its conditions

Transfer the mechanism while rechecking context.



## M07-L02 A reusable technical primitive

Primitive: decision recording. Input: an existing suggestion identifier and an allowed chosen queue. Output: an auditable decision identifier. Failures: unknown suggestion, duplicate decision, or invalid queue. Tests cover each condition. Queue names remain configuration. Name a maintainer and record a version change when contract behavior changes.

C. A tested decision-recording contract

Stable contracts travel better than local assumptions.



## M07-L03 A product signal with evidence

Observed: forty percent of eligible tasks use assistance in the fictional follow-up; agents report duplicate entry. Hypothesis: an integrated review surface will increase adoption. Validation: observe the current task and test the integrated version on a bounded sample. Unknown: whether the same friction recurs at other customers. No market-size claim follows from this case.

A. Evidence about workflow and consequences

Traceable observations help product teams decide.



## M07-L04 Capability after you leave

Ask the operator to respond to one unavailable-service scenario without contacting you. Ask the maintainer to explain a rejected-input trace. Record what they can do, what remains unclear, and who will maintain the playbook. Model update: accurate suggestions need integration and trusted override handling to become useful. The next loop starts from that revised frame.

C. Operators complete a recovery exercise independently

Demonstrated capability matters more than document volume.



## M08-L01 A constraint changes mid-project

Use the local dataset and rules. Test usability, category logic, validation, and logging. Mark production integration and model benefit untested. Keep a future integration gate with Luis and Priya. This fallback creates progress without pretending it exercised the blocked customer systems.

A. Selected behavior within the simulation

The fallback’s scope governs its claims.



## M08-L02 One decision for three audiences

Operator: review the queue suggestion, override when needed, and save your choice; use manual triage if unavailable. Engineer: the local API validates input, keeps review separate, and records correlated events; production controls remain pending. Executive: the synthetic test supports a bounded pilot hypothesis; authorize the next access review rather than claiming customer savings.

B. The facts, limits, and decision

Compression changes emphasis, not evidence.



## M08-L03 Failure-mode diagnosis

Moving goalposts: restore the timestamped threshold and publish the complete result. Fragile prototype: hold landing until an owner and support conditions exist. Hero dependency: teach the maintainer and test an independent rule update. The correction needs behavior evidence, not merely a newly written policy.

C. Changing success criteria after seeing results

Post-result threshold changes distort the experiment.



## M08-L04 Practice and the growth ladder

Week one: observe a permitted workflow and map the actual decision. Week two: co-author a small frame with its owner. Week three: run an authorized bounded experiment with a written prediction. Week four: compare results and identify one reusable lesson. If workplace access is unavailable, use a second simulation and label it accordingly.

A. No, the stage requires field evidence

Keep educational achievement separate from verified career capability.



## M09-L01 A fresh ambiguous engagement

A defensible frame targets supervisor review time while preserving authorized priority and closure decisions. Missing identifiers require a clarification path. Duplicate detection supports the reviewer but does not silently delete a request. Any urgent safety text routes to human assessment under existing procedures. Record these as design boundaries before implementation.

B. The authorized supervisor

The tool assists review without assuming operating authority.



## M09-L02 Build, predict, and inject a constraint

The fallback uses synthetic fixtures, validates asset identifiers, flags urgent text for the supervisor, and saves reviewed decisions. Prediction and evidence remain separate. The record names live integration as untested and preserves the original safety boundary. A good submission explains why these controls address the case rather than merely listing features.

C. The distinction between tested and untested behavior

Fallbacks change the evidence boundary.



## M09-L03 The portfolio and scoring rubric

Use zero for absent evidence, one for description, two for partial demonstration, three for a coherent supported result, and four for strong demonstration with limitations and transfer. The proposed pass threshold is seventy percent plus all mandatory gates. This is an educational scoring design, not an accredited competency standard.

A. No, evidence integrity is a mandatory gate

Mandatory gates remain separate from the aggregate score.



## M09-L04 A field extension and the next loop

Propose observing one approved data-review task and testing a reviewable exception summary with synthetic or explicitly permitted data. Retain human judgment and authoritative procedures. Name the operational owner and define success before acting. Treat real deployment evidence as the next learning objective, not something this simulated portfolio already established.

B. Vocabulary and context, while permissions still need verification

A transferable method does not imply transferable authority.

