# scenario-card-lint

Educational scenario-card linter for Acceptance Plane™ public scenario cards.

This tool checks whether a public scenario card contains enough high-level fields to support tabletop discussion. It does not verify evidence, issue receipts, authorize actions, certify systems, score compliance, or implement production controls.

## Run one card

```bash
python3 tools/scenario-card-lint/scenario_card_lint.py scenarios_batch_1/AP-SCEN-001.json
```

## Run the 5-minute demo cards

```bash
python3 tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/AP-SCEN-001.json scenarios_batch_1/AP-SCEN-050.json scenarios_batch_2/AP-SCEN-100.json
```

## JSON output

```bash
python3 tools/scenario-card-lint/scenario_card_lint.py --format json scenarios_batch_1/AP-SCEN-001.json
# or
python3 tools/scenario-card-lint/scenario_card_lint.py --json-report scenarios_batch_1/AP-SCEN-001.json
```

## Boundary

The output is an educational completeness report. It must not be used for production allow/deny decisions, procurement approval, certification, conformance status, compliance status, or patent/trademark rights.
