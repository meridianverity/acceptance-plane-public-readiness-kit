# Acceptance Boundary Patterns

The acceptance boundary is the moment where AI intention may become system consequence. Different systems expose that boundary in different places.

## Common public patterns

| Pattern | Boundary example | Public risk |
| --- | --- | --- |
| Tool-call boundary | Agent invokes a privileged API | The tool call may exceed current scope. |
| Workflow boundary | Agent triggers a business process | Downstream state changes may be irreversible. |
| Deployment boundary | Agent applies production changes | A plan may become an outage. |
| Data egress boundary | Agent exports or sends data | Sensitive information may leave authorized context. |
| Write-back boundary | Agent updates an EHR, CRM, ledger, or case file | A suggestion may become an official record. |
| Transaction boundary | Agent issues refund, payment, trade, or transfer | Analysis may become financial effect. |
| Rendering boundary | Synthetic overlay or recommendation is displayed | A user may be misled before review. |
| Sensor ingress boundary | Sensor event enters perception or control stack | Spoofed inputs may influence decisions. |
| Robotics boundary | Agent commands motion, actuation, dosage, or physical change | Digital intent becomes physical hazard. |
| Identity / delegation boundary | Agent grants, transfers, or escalates authority | Future action space changes. |

## Boundary placement rule

Place the acceptance question wherever an action can cross from intention into consequence. For public materials, name the boundary without publishing implementation-level enforcement design.
