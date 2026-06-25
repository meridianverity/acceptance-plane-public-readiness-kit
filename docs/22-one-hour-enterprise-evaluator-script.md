# One-Hour Enterprise Evaluator Script

This script helps a developer, security reviewer, buyer, or governance lead evaluate the public readiness kit without treating it as a product implementation or certification kit.

## Minute 0–5: run the demo

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
```

Expected signal: the tool prints `DISCUSSION_READY` for sample scenario cards and repeats that it is not certification, compliance approval, production readiness, or an allow/deny decision.

## Minute 5–15: inspect scenario coverage

Open `scenarios/index.csv` and confirm that the corpus spans cloud, enterprise data, healthcare, finance, public sector, education, AR/VR, sensors, robotics, and agent tool use. Confirm that the JSON cards are split into `scenarios_batch_1/` and `scenarios_batch_2/` for web-upload convenience.

## Minute 15–25: test the JSON path

```bash
make demo-json
```

Expected signal: JSON output is suitable for tabletop review notes, not for runtime enforcement.

## Minute 25–40: read the public boundary

Review:

- `PUBLIC_BOUNDARY.md`
- `PATENT_AND_TRADEMARK_NOTICE.md`
- `docs/19-license-and-rights-boundary.md`
- `docs/21-public-threat-model.md`

## Minute 40–50: run release QA

```bash
make qa-clean
```

Expected signal: scenario lint, boundary QA, and manifest verification pass.

## Minute 50–60: decide the right next question

Recommended next question:

> Which action classes in our environment require an acceptance-boundary conversation before impact?

Do not ask the public kit to certify a vendor, approve a procurement, authorize a production action, or implement an Acceptance Plane.
