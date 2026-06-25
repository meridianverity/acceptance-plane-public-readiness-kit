# Quickstart: 5-Minute Developer Trial

This is the shortest path for a developer to try the public readiness kit.

## 0. Boundary

This is an educational public utility. It is not a product implementation, standard, conformance suite, certification kit, patent license, or production allow/deny system.

## 1. Run the demo

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
```

Expected outcome: the linter prints `DISCUSSION_READY` for selected scenario cards and repeats that the result is not certification, compliance approval, production readiness, or an allow/deny decision.

## 2. Run the full corpus

```bash
python3 tools/scenario-card-lint/scenario_card_lint.py --summary scenarios_batch_1/*.json scenarios_batch_2/*.json
```

Expected outcome: all 100 public scenario cards are structurally ready for tabletop discussion.

## 3. Run the release QA gate

```bash
make qa
```

This runs:

- full scenario-card lint across the 100-card public corpus,
- full-repo public boundary QA,
- strict manifest verification with local-generated-file exclusions.

## 4. Understand the three words

- **ACCEPT** means the public scenario card expects enough current, scoped evidence for discussion purposes.
- **HOLD** means the scenario should pause before impact because evidence, scope, freshness, approval, or context is incomplete.
- **REFUSE** means the scenario should not proceed because the requested action conflicts with policy, authority, safety, rights, or protected-system boundaries.

These are educational labels in scenario cards, not production decisions.
