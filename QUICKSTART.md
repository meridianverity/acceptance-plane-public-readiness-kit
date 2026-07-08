# Quickstart — Acceptance Plane Public Readiness Kit v0.2.0

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

This builds `dist/acceptance-plane-public-readiness-kit-v0.2.0.zip`, writes a SHA-256 sidecar, and verifies archive shape, path safety, CRC, manifest entries, and file hashes.
