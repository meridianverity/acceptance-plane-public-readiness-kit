# Quickstart — Acceptance Plane Public Readiness Kit v0.3.4

Boundary: Not a product implementation. Not a standard. No patent license. No certification right.

## 1. Run the 5-minute scenario-card linter

```bash
make demo
```

## 2. Run the public readiness index sample

```bash
make readiness-demo
```

Expected shape:

```text
Readiness posture: HOLD_FOR_IMPLEMENTATION_REVIEW
Discussion maturity: 72 / 100
```

The score is an educational readiness signal. It is not certification, compliance approval, procurement approval, production readiness, or an allow/deny decision.

## 3. Check corpus coverage

```bash
make coverage-check
```

## 4. Generate a workshop packet

```bash
make workshop-demo
```

Outputs go to `/tmp/acceptance-plane-workshop-pack/` by default.

## 5. Run the full public QA gate

```bash
make qa-clean
```

## 6. Build and verify a release ZIP

```bash
make qa-full
```

This builds `dist/acceptance-plane-public-readiness-kit-v0.3.4.zip`, writes a SHA-256 sidecar, verifies archive shape/path safety/CRC/manifest entries/file hashes, and checks deterministic rebuild behavior.

## v0.3.4 public readiness operating-system checks

```bash
make report-demo
make browser-demo-check
make facilitator-check
```

Boundary: public readiness discussion only; not certification, compliance approval, production readiness, or an allow/deny decision.


## v0.3.4 language-polish and learning-goal polish gate

Run `make scenario-language-polish-check` to verify that the 300-card public educational corpus does not contain visible wording scars such as a duplicated `before` token, incorrect article before `incident`, or incorrect article before `operator`. This is editorial QA only, not certification, conformance testing, production readiness, or an allow/deny decision.
