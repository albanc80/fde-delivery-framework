# Forward Deployed Delivery

All organizations, records, quantities, results, and thresholds in the cases are fictional. The prototype uses rules, not an AI model. This course does not demonstrate customer savings, standards compliance, production security, or accredited competence. Narration uses synthetic voices.

## M01 Outcome ownership

35 practice minutes | Framework §§3,5,6,8

### M01-L01 The FDE responsibility

#### The method

A forward deployed engineer works close to the people who bear the consequences of a system. The responsibility extends from understanding an ambiguous request to helping the operation adopt a useful change. Technical work remains essential. The difference is the boundary of ownership: a deployed feature is an intermediate milestone. An outcome requires observable workflow change, a responsible operator, and evidence collected after adoption. Keep these boundaries visible when stakeholders celebrate a successful demonstration.

#### Case evidence

Northstar Support asks for an AI assistant. Twenty agents handle access, billing, and incident tickets. A polished demo receives applause, but agents still copy tickets into a spreadsheet. The deployer has delivered software while the operating workflow remains unchanged.

#### Practice

Write one statement describing the delivery milestone and another describing the operating outcome. Name who could verify each.

#### Knowledge check

Which evidence best supports an adopted outcome?

A. A successful demo
B. Observed workflow use and predefined outcome measures
C. A completed code review

### M01-L02 Six principles in a decision

#### The method

The framework gives six postures: own the outcome, stay close to reality, act to learn, know what you know, trade off on purpose, and leave capability behind. Apply them to an actual choice. Ask whose result matters, what you observed, which experiment reduces uncertainty, which claims remain assumptions, what risk you are accepting, and what will remain useful when you leave. A principle becomes practical when it changes scope, evidence, authority, or sequencing.

#### Case evidence

The sponsor requests automatic replies this Friday. You have permission to analyze synthetic tickets but no authority to send customer messages. Maya agrees to test suggestions with human review. The security reviewer has not assessed production data access.

#### Practice

Select a Friday deliverable. Explain its learning value, authority boundary, and reusable output.

#### Knowledge check

Which choice respects the permission boundary?

A. Send replies because the sponsor requested speed
B. Use production data without telling security
C. Test a reviewable suggestion with permitted data

### M01-L03 A portfolio of evidence

#### The method

The eight capabilities cover discovery, signal extraction, systems thinking, technical breadth, delivery judgment, translation and trust, shipped learning, and ownership and compounding. Treat these as observable behaviors. A portfolio should show the problem you clarified, a complete working path, a consequential trade-off, a prediction made before action, and a reusable contribution. Self-ratings identify practice priorities. They do not independently verify readiness or replace evidence from work.

#### Case evidence

You can implement APIs quickly but have never observed users after rollout. Another learner writes strong discovery notes but cannot get data to a usable screen. Both have a specific practice gap, rather than one overall score that explains everything.

#### Practice

Choose your weakest capability. Define a behavior that another person could observe and a course artifact that demonstrates it.

#### Knowledge check

What makes a capability claim stronger?

A. A high self-rating
B. A behavior someone else can verify
C. Memorizing the framework

### M01-L04 The case and the course boundary

#### The method

This course uses fictional evidence and a local prototype. You will practice a complete delivery loop while maintaining the distinction between simulated and field evidence. Each lesson produces something that feeds the next decision. Keep a dated journal, store your first prediction before examining later evidence, and separate your submission from the worked solution. Completion can demonstrate learning in this environment. Production competence also requires experience with real constraints, users, ownership, and consequences.

#### Case evidence

Northstar has a fictional baseline of 20 minutes per ticket review. A later sample reports 12 minutes. These values exist for practicing measurement and judgment. They are neither market benchmarks nor promises about AI productivity.

#### Practice

Create a dated learning journal with headings for evidence, assumptions, predictions, observed results, and decisions.

#### Knowledge check

How should you describe the sample numbers?

A. Verified industry benchmarks
B. Guaranteed productivity gains
C. Fictional data for an exercise

## M02 Recon and Immerse

45 practice minutes | Framework §4 phases1–2; §5 M1–M3

### M02-L01 The decision behind the request

#### The method

Recon starts with hypotheses and questions. Convert the request into the decision it creates. Identify who can decide, who experiences consequences, who knows the workflow, and who benefits. These roles often belong to different people. Find previous attempts before proposing a solution. Distinguish physical constraints from political conditions and habits. A habit may change. A permission requirement still governs your action even when it is organizational rather than physical.

#### Case evidence

A sponsor says, build AI. Maya says, reduce repeated triage. Luis owns the ticket API. Priya approves data access. Agents explain why the previous automation failed: it sent plausible but incorrect replies and increased their checking work.

#### Practice

Write a draft decision statement and five discovery questions. Keep the proposed solution provisional.

#### Knowledge check

Which is a useful Recon output?

A. A provisional decision and questions
B. A fixed architecture
C. A promised savings figure

### M02-L02 One ticket through the workflow

#### The method

Immerse follows actual work. Trace one item from origin to decision and identify handoffs, re-entry, waiting, and exception handling. Ask an operator to show the task and attempt a permitted version yourself. Observe what happens before and after the proposed solution. An integration can succeed technically while adding another queue or another confirmation step. Capture the entire workflow boundary so local improvement does not hide additional work elsewhere.

#### Case evidence

An agent reads a ticket, looks up the account, checks a category sheet, assigns a queue, and records the reason. Copying takes two minutes, but waiting for permission can take a day. The two delays require different interventions.

#### Practice

Draw the workflow as ordered steps. Mark a delay, a handoff, a duplicate entry, and an exception.

#### Knowledge check

Why trace the steps after the new tool?

A. To add more features
B. To identify displaced work and downstream effects
C. To avoid talking to operators

### M02-L03 Known, assumed, and unknown

#### The method

Tag important claims by evidence status. Known means supported within the available evidence and scope. Assumed means temporarily used to proceed. Unknown means material information remains missing. Attach a source and date to known claims. Identify a test and owner for important assumptions. Conflicting accounts stay visible until you understand differences in context or authority. The observed-versus-reported distinction helps investigation, but one observation does not establish universal behavior.

#### Case evidence

Maya says everyone uses the category sheet. A shift observation shows three agents using private notes instead. API documents describe a current endpoint, but Luis says its production permissions are still pending.

#### Practice

Tag four claims and identify the next test for the largest uncertainty.

#### Knowledge check

What does one observed shift establish?

A. The behavior observed in that shift
B. All agents always act that way
C. The manager is dishonest

### M02-L04 The verified Site Map

#### The method

The Site Map joins decision, people, process, technology, data, constraints, incentives, and history. Recon creates version zero. Immerse checks it and produces version one. Include verification status rather than filling gaps with plausible detail. Incentives deserve explicit attention: automation may remove visible work while increasing accountability or perceived job risk. The map is a decision aid, so emphasize dependencies that affect the proposed experiment and who can resolve them.

#### Case evidence

Agents fear that faster triage will become an individual performance target. Maya wants reliable routing. Priya needs a data boundary. Luis needs a documented fallback. These interests shape adoption even if the same software works for everyone.

#### Practice

Complete all eight Site Map fields. Leave unresolved facts explicitly unknown and attach a next action.

#### Knowledge check

What belongs in an unresolved field?

A. A plausible invented answer
B. Nothing, so the map looks complete
C. Unknown, owner, and verification action

## M03 Frame the decision

45 practice minutes | Framework §4 phase3; §8.1

### M03-L01 The outcome line

#### The method

The Frame Card outcome names a user, a workflow, its current condition, a desired condition, a metric, and constraints. Co-author it with the operator. Use a measure the operator recognizes and define its denominator. Separate desired outcome from the technology proposed to achieve it. A frame that says deploy AI specifies a solution. A frame that says reduce review time while preserving routing quality leaves room to choose the simplest useful intervention.

#### Case evidence

The fictional baseline is a median of 20 minutes across twelve simulated reviews. The team proposes a median no greater than 14 minutes for an equivalent assisted sample, with at most one misroute per twelve decisions. These are exercise thresholds agreed before reading results.

#### Practice

Write the outcome line and define review time, sample size, and routing error.

#### Knowledge check

Which frame preserves solution choice?

A. Deploy an AI agent
B. Reduce defined review time under quality constraints
C. Use the newest model

### M03-L02 The bet and change-of-mind evidence

#### The method

The bet connects a hypothesis to the smallest action and evidence that would change your mind. State it before acting. A falsifiable bet names the uncertainty rather than promising a win. Define stop conditions as well as desired performance. Practical stop conditions may include unsafe actions, unusable data, insufficient authorization, or user rejection. Record who can make the gate decision and what happens when evidence is mixed.

#### Case evidence

The hypothesis is that repeated category lookup causes avoidable review effort. A routing suggestion tests that mechanism. An automatic-reply generator changes a different part of the workflow and introduces additional risk.

#### Practice

Write a bet, a smallest action, and two pieces of evidence that would change your decision.

#### Knowledge check

When should you define disconfirming evidence?

A. Before the experiment
B. After seeing the results
C. Only if the sponsor asks

### M03-L03 Metrics and guardrails

#### The method

An outcome measure needs companion guardrails. Review speed alone can reward careless routing. Define quality, exceptions, coverage, and workload as appropriate. Keep the analysis unit consistent and compare similar tasks. A small synthetic sample supports a course decision, not a population estimate. Calculate improvement transparently and state whether it represents capacity, cost, or another benefit. Time released becomes cash savings only through an additional organizational mechanism.

#### Case evidence

A change from 20 to 12 minutes is eight minutes less per review and a 40 percent reduction in the sample median. It does not establish a 40 percent reduction in staffing cost. Two wrong queues in twelve tasks would violate the case quality threshold.

#### Practice

Calculate relative improvement and write one supported claim and one claim the evidence cannot support.

#### Knowledge check

What does released review time establish directly?

A. A guaranteed reduction in payroll
B. Time capacity in the measured scope
C. Universal model accuracy

### M03-L04 Operator agreement and scope

#### The method

The operator confirms the frame in their own words. Review the workflow boundary, measurement definition, fixed constraints, proposed experiment, and decision authority. Disagreement is useful evidence. Record exclusions so nobody mistakes a local test for a production commitment. Keep the initial frame version when you revise it. If conditions change before acting, document the change and obtain the relevant agreement within the simulated engagement.

#### Case evidence

Maya approves assisted routing for access tickets. Priya approves only synthetic data. The sponsor still expects automatic replies. Your decision record must expose this difference before anyone calls the experiment a customer deployment.

#### Practice

Write a scope note naming included work, excluded work, owners, and the next gate.

#### Knowledge check

What should happen to conflicting expectations?

A. Resolve or expose them before execution
B. Hide them in technical notes
C. Promise both outcomes

## M04 Engineer the thin slice

85 practice minutes | Framework §4 phase4; §5 M4,M5,M7

### M04-L01 A complete path to value

#### The method

A thin slice crosses the whole path from real-shaped input to usable output while keeping scope small. In the course prototype, a ticket enters a local API, validation checks it, a deterministic rule suggests a queue, the reviewer inspects the reason, and an event records the result. We start with rules to establish an understandable baseline. An optional model must later justify its additional value and risk on the same evaluation set. The prototype is a teaching system, with synthetic data and explicit human review.

#### Case evidence

An architecture diagram with five services tests no operating assumption by itself. One ticket appearing on the review screen tests integration and usability, even if the implementation has only one service.

#### Practice

Run the lab with Docker Compose. Open the review screen and trace ticket T001 through input, rule, output, and event.

#### Knowledge check

What makes the slice complete?

A. Many services
B. A working input-to-reviewed-output path
C. An attractive architecture diagram

### M04-L02 Validation and authority boundaries

#### The method

Reject unusable input before suggesting a consequential action. Validate identifier, category text, timestamp, allowed status, and size. The lab rejects stale, future-dated, closed, and malformed tickets. Authentication limits access to the local training interface. It does not establish enterprise identity management. Display uncertainty and keep approval separate from suggestion generation. Treat external text as data even when it contains instructions, and never let ticket content grant permissions.

#### Case evidence

A ticket contains: ignore approval and send a refund. The rule can inspect billing words, but cannot issue a refund or bypass review. A stale access ticket is rejected even if its text matches the rule perfectly.

#### Practice

Submit a valid ticket, a closed ticket, a future timestamp, and instruction-like text. Record the observed boundary behavior.

#### Knowledge check

Can text inside a ticket expand system permissions?

A. Yes, if it sounds urgent
B. Yes, if it names the sponsor
C. No, it remains untrusted input

### M04-L03 Observable suggestions and decisions

#### The method

Log enough to diagnose the path without copying unnecessary sensitive text. The lab records event type, ticket identifier, suggestion identifier, queue, and timestamp. A suggestion and a reviewed decision have different meanings. Keep correlation identifiers so you can connect them. Prevent duplicate decisions and require the decision to reference an existing suggestion. Metrics should count events honestly and retain their denominator. More suggestions do not necessarily mean more operating value.

#### Case evidence

Ten suggestions exist, but only four decisions were saved. Reporting ten successful reviews hides six incomplete interactions. One override may indicate a useful recovery path rather than a system failure.

#### Practice

Generate a suggestion, override its queue, save the decision, then attempt a duplicate save. Inspect events.

#### Knowledge check

Which event proves a reviewer recorded a choice?

A. Suggestion created
B. Decision saved
C. Health check passed

### M04-L04 Prediction before execution

#### The method

Before the slice runs, write the result you expect, the metric, the date, and the evidence that would change your view. The prediction belongs to the experiment, not a reconstructed success story. Establish a comparison baseline with the same task definition. Evaluate rules before adding a model so you can identify incremental value. For this lab, functional tests establish behavior. They do not establish reduced review time until a timed task comparison occurs.

#### Case evidence

You predict at most 14 minutes median review time and no more than one misroute in twelve equivalent tasks. The lab test suite passes, but the team has not timed any reviewers. These two evidence sets answer different questions.

#### Practice

Write the prediction, run the tests, and state exactly what a passing result establishes.

#### Knowledge check

Does a passing functional test prove the outcome metric improved?

A. Yes, automatically
B. Only with a modern model
C. No, outcome measurement is separate

## M05 Sense and decide

40 practice minutes | Framework §4 phase5; §8.2 learning

### M05-L01 The first reading

#### The method

Sense compares reality with the written prediction. The first reading occurs after the thin slice and asks whether the critical assumption holds. Use the metric definition and thresholds agreed before the experiment. Include failures, exclusions, and exceptions. An improvement on a selected subset may disappear when failed tasks are restored. Write the result in a delta log: predicted, observed, model update, and decision.

#### Case evidence

The twelve-task assisted sample has a median of 12 minutes and one wrong queue. It meets the fictional speed and quality thresholds. Two additional unusable tickets were rejected before review and must be reported as exclusions.

#### Practice

Write a delta entry that includes the sample denominator and excluded records.

#### Knowledge check

What should the report do with rejected inputs?

A. Hide them
B. Include them as successful reviews
C. Report their count and exclusion reason

### M05-L02 Land, iterate, pivot, or stop

#### The method

The gate decision converts evidence into action. Land when the critical assumption holds and remaining operational conditions are satisfied. Iterate when the mechanism remains plausible but a bounded defect needs correction. Pivot when evidence points toward a different problem or intervention. Stop when the approach lacks value or exceeds an unacceptable boundary. Explain the choice using evidence, risk, reversibility, and the next observable test.

#### Case evidence

Three variants appear: speed improves but errors double; category assistance has no effect because account lookup dominates; and a prototype sends unauthorized replies. Each failure demands a different decision.

#### Practice

Assign a gate decision to each variant and state the next action.

#### Knowledge check

What is the correct response to an unauthorized action?

A. Stop the action path and recover the boundary
B. Ignore it if speed improved
C. Change the metric

### M05-L03 Confounders and honest interpretation

#### The method

A before-and-after difference does not isolate causality. Changes in ticket mix, staffing, reviewer experience, incentives, or measurement can explain part of the result. Preserve task definitions and compare comparable samples. For stronger field evaluation, consider a staged or controlled design suitable for the workflow. In the course, arithmetic is verifiable but synthetic evidence cannot establish effectiveness in a real organization.

#### Case evidence

The assisted group receives only access tickets while the baseline includes complex incidents. The headline improvement looks larger, even though the samples answer different questions.

#### Practice

Identify three alternative explanations and revise the comparison plan.

#### Knowledge check

What weakens a before-and-after comparison?

A. A written metric definition
B. Different task complexity across samples
C. Reporting exclusions

### M05-L04 The second reading after adoption

#### The method

Sense occurs again after Land and an adoption period. The second reading asks whether the Frame Card outcome appears in the operator’s workflow. Distinguish available software, attempted use, reviewed decisions, and sustained use. Count eligible work rather than all work if the tool serves only one category. Examine overrides and abandonment alongside speed. The original prediction remains the comparison point unless a documented change occurred before the new test.

#### Case evidence

Two weeks later, forty of one hundred eligible tickets use assistance. Completed assisted reviews remain faster, but adoption is below the pre-agreed 70 percent exercise threshold. The tool is available without achieving the full adoption target.

#### Practice

Write the second delta entry and recommend the next gate decision.

#### Knowledge check

What does the second Sense reading evaluate?

A. Only whether the code compiles
B. Only prototype accuracy
C. Outcome and adoption after landing

## M06 Land and support adoption

55 practice minutes | Framework §4 phase6; §8.3

### M06-L01 The six landing checks

#### The method

The landing checklist covers reliability, observability, security, integration, usability, and adoption. Attach evidence to each item and name unresolved conditions. A passing health endpoint is one availability signal, not the whole reliability argument. A bearer token in a local lab is one boundary, not enterprise security approval. Keep the outcome measurement scheduled in Sense so the checklist does not quietly substitute technical readiness for realized value.

#### Case evidence

The prototype validates inputs and logs decisions. It still lacks enterprise authentication, production persistence design, restore testing, retention policy, and customer-environment validation. These gaps matter even though local tests pass.

#### Practice

Complete the checklist with evidence, status, owner, and next action for each item.

#### Knowledge check

Does the lab token establish enterprise security readiness?

A. No, its scope is local training
B. Yes, because authentication exists
C. Yes, if the demo is fast

### M06-L02 The named operating owner

#### The method

Landing requires someone on site who operates the system. Name the owner and clarify routine responsibilities, escalation, exceptions, and the authority to disable the workflow. Ownership is more than listing a person in a document. The person needs context, access, capability, and time. Keep your accountability through adoption while transferring practical capability rather than preserving dependence on you.

#### Case evidence

Maya owns the queue, but Luis alone can restore the service. If Luis is unavailable, agents need a manual fallback and an escalation contact. A nominal owner without a recovery path cannot operate independently.

#### Practice

Write an ownership table and a one-page runbook with a manual fallback.

#### Knowledge check

What makes ownership operational?

A. A name on a slide
B. Authority, capability, access, and recovery instructions
C. The engineer always being online

### M06-L03 Adoption as a workflow change

#### The method

Adoption depends on the complete task, incentives, confidence, and support. Training alone will not fix an extra queue, unclear responsibility, or fear of punitive measurement. Observe the task again after rollout and ask where the new system adds effort. Provide a visible override and a safe fallback. Plan a defined adoption period with checkpoints and a denominator that reflects eligible work.

#### Case evidence

Agents abandon the tool because they must copy the result back into the main queue. The suggestion is accurate, but the complete task takes longer. Maya also discovers agents think overrides will count against them.

#### Practice

Propose two workflow changes and a small test for each.

#### Knowledge check

Which signal most directly shows workflow adoption?

A. Attendance at a training session
B. A favorable sponsor quote
C. Sustained use in eligible tasks

### M06-L04 Recovery and a bounded rollout

#### The method

Pace rollout by consequence and reversibility. Start with a permitted boundary, observe exceptions, and retain a known manual path. Define triggers for disable, rollback, and escalation before the incident. A backup is useful only if restoration works. For production, evaluate restoration, retention, monitoring, identity, and operating support in the actual environment. The course prototype intentionally demonstrates the questions without claiming all those controls are complete.

#### Case evidence

The API becomes unavailable during a shift. Agents can still use the category sheet. Maya disables assistance, Luis diagnoses the service, and the event enters the learning log. The team can continue operating while the feature recovers.

#### Practice

Write a recovery trigger, immediate action, responsible owner, and evidence required to resume.

#### Knowledge check

What should be defined before rollout?

A. Disable triggers and a manual fallback
B. A guaranteed zero-failure promise
C. An assumption that the owner is always available

## M07 Distill and compound

40 practice minutes | Framework §4 phase7; §5 M8

### M07-L01 The pattern behind the solution

#### The method

Distill separates the transferable principle from the local implementation. Ask which conditions made the intervention useful and which conditions limited it. A reusable pattern names those conditions, the mechanism, and the evidence boundary. Copying the entire previous architecture creates an imperial playbook. A principle becomes more useful when another site can test it without inheriting assumptions that belonged only to the original environment.

#### Case evidence

Northstar benefited from reviewable category suggestions. A warehouse needs exception handling, not support queues. The reusable idea is embedding a reviewable suggestion in the existing decision step, while the category rule remains local.

#### Practice

Write one conditional pattern and name two conditions that require retesting elsewhere.

#### Knowledge check

What should transfer first?

A. Every service from the old architecture
B. The principle and its conditions
C. The old customer’s permissions

### M07-L02 A reusable technical primitive

#### The method

A primitive is a small reusable technical contribution with a clear contract. Separate stable behavior from customer-specific configuration. Input validation, correlation identifiers, and idempotent decision recording can generalize more easily than Northstar’s exact routing categories. Document inputs, outputs, failure behavior, tests, and assumptions. Reuse needs a maintainer and a version policy. A copied file without ownership may multiply defects rather than reduce future work.

#### Case evidence

The lab routing function contains category keywords. Its event-recording contract is more general: one suggestion identifier can receive only one saved decision. You can reuse that contract without adopting the same categories.

#### Practice

Extract a primitive proposal with interface, tests, owner, and local configuration.

#### Knowledge check

Which item is most reusable across domains?

A. Northstar’s sponsor name
B. A fixed access-ticket keyword list
C. A tested decision-recording contract

### M07-L03 A product signal with evidence

#### The method

A product signal connects a field observation to a product decision. Record the affected workflow, frequency within the observed scope, current workaround, consequence, and evidence. Separate a local request from a repeated pattern across sites. Propose a product hypothesis and the next validation action. Avoid presenting the loudest stakeholder’s preference as market demand. Preserve disagreement and missing information so the product team can judge transferability.

#### Case evidence

Agents abandon suggestions because copying back to the queue adds work. The product signal is a need for in-workflow review integration. One site provides evidence of friction, but not yet a general market priority.

#### Practice

Write a product-signal memo with observed evidence, hypothesis, and validation request.

#### Knowledge check

What distinguishes a product signal from a feature demand?

A. Evidence about workflow and consequences
B. Executive seniority
C. A longer feature list

### M07-L04 Capability after you leave

#### The method

The distill pack contains a pattern, primitive, playbook, product signal, site capability, and model update. Site capability requires operators who can execute and adapt the workflow without the original engineer. Test handover through a teach-back or recovery exercise. Documentation helps but does not prove capability. Keep a feedback system so new exceptions lead to updates after the engagement ends.

#### Case evidence

Maya explains how to disable assistance, restore manual triage, inspect errors, and request a rule change. Luis can recover the service from the runbook. Their demonstration is stronger evidence than receiving a handover deck.

#### Practice

Complete the six-part distill pack and design a handover test.

#### Knowledge check

Which evidence best supports successful handover?

A. A long documentation folder
B. The original engineer remains the only responder
C. Operators complete a recovery exercise independently

## M08 Judgment under pressure

50 practice minutes | Framework §§5,7,8

### M08-L01 A constraint changes mid-project

#### The method

Constraint injection tests whether the delivery plan can adapt. Revisit the frame, uncertainty, authority, and smallest useful action when conditions change. A new restriction does not justify bypassing controls. Choose a permitted fallback and state which claims it can still test. Record the change, its effect on evidence, and the next gate. A synthetic fallback can test workflow design but cannot prove a production integration now unavailable.

#### Case evidence

Priya prohibits external model calls. Luis reports the customer API will be unavailable this week. The sponsor still wants progress. The rule-based synthetic prototype can continue testing review behavior.

#### Practice

Revise the plan while preserving a useful experiment and an honest evidence boundary.

#### Knowledge check

What can a synthetic fallback prove?

A. Selected behavior within the simulation
B. Customer API readiness
C. Production access approval

### M08-L02 One decision for three audiences

#### The method

Translation preserves truth while changing the level of detail. Operators need task consequences and recovery. Engineers need contracts, failure modes, and dependencies. Executives need the decision, evidence, risk, and next commitment. Every version should keep the same authority boundary and uncertainty. Compress the messy context into one page. If one audience hears a stronger promise than another, the translation has changed the decision rather than clarified it.

#### Case evidence

The system generates reviewable routing suggestions using synthetic data. It has not been approved for production. That limit must appear in the executive summary as clearly as in the engineering note.

#### Practice

Write a three-sentence explanation for an operator, engineer, and executive.

#### Knowledge check

What must remain constant across audiences?

A. Every technical detail
B. The facts, limits, and decision
C. The same word count

### M08-L03 Failure-mode diagnosis

#### The method

Diagnose behavior before attaching a label. The framework names eleven failures, including parachuting, going native, silent assumptions, moving goalposts, fragile prototypes, bespoke loops, and hero dependency. Use the symptom to select a counter and an observable test. External review helps preserve critical distance after immersion. Do not classify disagreement as going native simply because a colleague challenges your proposed solution.

#### Case evidence

The team removes the quality threshold after errors appear. A prototype runs without an owner. Every rule change depends on the original engineer. Each symptom maps to a different failure mode.

#### Practice

Name each failure, its counter, and evidence that the counter worked.

#### Knowledge check

Which symptom indicates moving goalposts?

A. Writing a prediction before acting
B. Rejecting malformed input
C. Changing success criteria after seeing results

### M08-L04 Practice and the growth ladder

#### The method

The ladder progresses through apprentice, builder, deployment owner, multiplier, and system designer. Its exit tests concern observable work in context. Course completion does not automatically satisfy those tests. Use the daily, weekly, monthly, and quarterly cadence as a development aid. Select a manageable practice commitment, collect evidence, and seek feedback. Real workplace practice should respect data access, customer confidentiality, operating authority, and applicable procedures.

#### Case evidence

A learner finishes the prototype and calls themselves a deployment owner. They have not worked with real users or performed an outcome reading after production adoption. Their portfolio demonstrates simulated practice, with field evidence still pending.

#### Practice

Write a 30-day practice plan with one user observation, one prediction, and one review of evidence.

#### Knowledge check

Does course completion establish the deployment-owner stage?

A. No, the stage requires field evidence
B. Yes, after watching videos
C. Yes, if the self-rating is high

## M09 Capstone engagement

125 practice minutes | Framework §§4,7,8,9

### M09-L01 A fresh ambiguous engagement

#### The method

The capstone transfers the loop to Harbor Maintenance. A sponsor asks for an AI assistant to route maintenance requests. The workflow includes urgent conditions, missing asset identifiers, duplicate requests, and a supervisor who owns priority decisions. Keep safety procedures authoritative and do not automate operational control. Your first task is discovery and framing. The capstone uses synthetic records and evaluates how well you preserve evidence and authority while building a usable path.

#### Case evidence

The sponsor wants automated closure. The supervisor needs faster review and refuses automatic priority changes. Historical records include duplicates and missing asset IDs. These differences must appear in your Site Map.

#### Practice

Use the capstone brief and staged evidence pack. Submit a Site Map and Frame Card before opening later results.

#### Knowledge check

Who retains maintenance priority authority?

A. The ticket text
B. The authorized supervisor
C. The fastest routing rule

### M09-L02 Build, predict, and inject a constraint

#### The method

Adapt the lab contract to maintenance requests while preserving validation, human review, and auditable decisions. State the key uncertainty and prediction first. Implement only the smallest complete path that addresses it. Then apply the constraint card: an integration is unavailable and external model calls are prohibited. Demonstrate the permitted fallback and explain which evidence remains unavailable. Your implementation may use rules or an approved optional model, but the comparison must justify any added complexity.

#### Case evidence

The integration fails just before the review. A local fixture preserves the input contract. It demonstrates review behavior but cannot establish live integration reliability. Your decision record should say both.

#### Practice

Submit working code, test evidence, a timestamped prediction, and a revised decision after the constraint.

#### Knowledge check

What must the fallback report preserve?

A. The claim that integration passed
B. Only the favorable screenshots
C. The distinction between tested and untested behavior

### M09-L03 The portfolio and scoring rubric

#### The method

Submit a coherent portfolio rather than disconnected templates. The Site Map should support the Frame Card, the prediction should match its outcome, the build should test the critical uncertainty, and the delta log should compare against the prediction. Include the landing checklist, ownership plan, second reading, distill pack, and one-page decision memo. Score seven dimensions using observable criteria. A high aggregate score cannot compensate for an unauthorized action or fabricated evidence.

#### Case evidence

One submission has beautiful slides but no written prediction. Another has a modest prototype and clear evidence connecting every decision. Presentation quality supports readability, while the rubric evaluates delivery reasoning and behavior.

#### Practice

Score your portfolio using the rubric, then check every safety and evidence gate separately.

#### Knowledge check

Can a high score offset invented evidence?

A. No, evidence integrity is a mandatory gate
B. Yes, if the prototype works
C. Yes, if the slides are polished

### M09-L04 A field extension and the next loop

#### The method

The final lesson turns simulated practice into a bounded development plan. Identify a real workflow you may observe, the owner who can agree the frame, and the permissions needed for any experiment. Preserve confidentiality and authoritative operating procedures. Translate the loop into the domain while keeping the evidence discipline. The source’s O&G examples are draft translations, so do not infer WITSML compliance, safety approval, or real operational performance from this course.

#### Case evidence

In remote operations, a data-quality review may be a suitable first workflow. An agent that changes drilling parameters creates a different authority and consequence boundary. The same loop can guide investigation without granting the same action rights.

#### Practice

Write your next-loop proposal with owner, permitted observation, smallest action, metric, and stop condition.

#### Knowledge check

What does domain translation change?

A. It grants automatic operating permission
B. Vocabulary and context, while permissions still need verification
C. It proves standards compliance
