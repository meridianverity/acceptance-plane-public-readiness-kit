# Scenario Card Format

Scenario cards are JSON files for public discussion. The format is intentionally simple and educational. It is not a production schema, evidence object model, API contract, conformance format, certification artifact, or implementation disclosure.

A non-production JSON shape is provided at [`scenario_card.schema.json`](scenario_card.schema.json) to help authors keep public scenario cards consistent.

## Fields

- `id`
- `title`
- `domain`
- `risk_tier`
- `action_type`
- `protected_system`
- `scenario`
- `acceptance_boundary`
- `public_evidence_categories`
- `expected_decision`
- `why`
- `human_impact`
- `learning_goal`
- `rights_boundary`

Do not treat this format as an evidence object model, API contract, conformance format, certification artifact, or production allow/deny interface.
