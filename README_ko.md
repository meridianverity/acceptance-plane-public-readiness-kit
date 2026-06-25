# Acceptance Plane™ Public Readiness Kit v0.1.4

**개발자가 5분 안에 실행해 볼 수 있는 무료 공개 readiness kit입니다.**  
**Made by Meridian Verity Group (MVG): https://meridianverity.com/**  
**제품 구현체가 아닙니다. 표준이 아닙니다. 특허 라이선스가 아닙니다. 인증 권리가 아닙니다.**  
**Not a product implementation. Not a standard. No patent license. No certification right.**

이 키트는 agentic AI가 tool call, API 호출, 기록 변경, workflow trigger, data movement, production deploy, sensor/overlay/robotic action 같은 실제 효과를 만들기 전에 다음 질문을 묻도록 돕는 공개 교육/준비 자료입니다.

> 이 정확한 autonomous action을 이 protected system이 지금 받아들여도 되는가?

## 5분 quickstart

```bash
git clone https://github.com/meridianverity/acceptance-plane-public-readiness-kit.git
cd acceptance-plane-public-readiness-kit
make demo
```

API key, 외부 서비스, 패키지 설치가 필요 없습니다. Python standard library만 사용합니다.

전체 공개 QA gate:

```bash
make qa
```

로컬 cache까지 정리하며 확인:

```bash
make qa-clean
```

## 포함된 것

- 교육용 `scenario-card-lint`
- 100개 public scenario corpus
- Scenario card는 수동 업로드 친화적으로 `scenarios_batch_1/` 및 `scenarios_batch_2/`에 나뉘어 있으며, index/schema 자료는 `scenarios/`에 있습니다
- Acceptance Plane™ 공개 vocabulary와 Open Profile
- RFP / procurement 질문지
- board, nonprofit, public-sector, policy adoption 자료
- public-interest covenant
- full-repo boundary QA, manifest verification, QA report, file tree provenance
- premature hosted-project claim을 피하는 AAIF feedback inquiry 문안

## 의도적으로 제외한 것

production verifier, exact API schema, cryptographic binding, PermitReceipt implementation, non-bypassable interceptor, signed conformance suite, certificate registry, hardware adapter, domain-specific runtime implementation, unpublished patent claim language는 포함하지 않았습니다.

핵심 전략은 이것입니다.

> **카테고리는 공개하고, readiness layer는 열고, production mechanism은 보호합니다.**

## 시작 순서

1. `make demo` 실행
2. `docs/00-executive-summary.md` 읽기
3. `docs/01-open-profile.md` 읽기
4. `scenarios/index.csv`에서 100개 scenario 확인
5. `templates/rfp_questionnaire.md`와 `adoption/procurement_scorecard.md` 사용
6. AAIF/standard/foundation 쪽 접촉 전 `AAIF_FEEDBACK_INQUIRY.md` 확인
7. GitHub 공개 전 `GITHUB_UPLOAD_GUIDE.md`와 `RELEASE_CHECKLIST.md` 확인

## 공개 표현

정확한 표현:

> free public readiness kit with a 5-minute educational scenario-card linter for developers

피해야 할 표현:

> free version, open-source implementation, reference implementation, standard, conformance kit, certification kit

## 라이선스와 권리 경계

software files는 MIT License, docs/scenarios/templates/adoption materials는 CC BY 4.0입니다. 단, 이 공개 키트는 특허 라이선스, 상표 라이선스, 제품 구현 라이선스, 인증 권리, compliance approval, endorsement를 부여하지 않습니다.

## public-good 방향

이 키트는 “우리 제품을 사라”가 아니라, 병원, 학교, 작은 도시, nonprofit, public-sector buyer, auditor, 시민사회가 먼저 물어야 할 질문을 무료로 제공합니다.

> AI가 사람의 삶에 영향을 주기 전에, 이 행동을 받아들여도 된다는 충분한 증거가 있는가?


## 엔터프라이즈 평가 경로

빠르게 검토하려면 `make demo`를 실행한 뒤 `docs/21-public-threat-model.md`, `docs/22-one-hour-enterprise-evaluator-script.md`, `docs/23-archive-and-license-boundary.md`, `docs/24-release-integrity.md`를 순서대로 보면 된다.

이 경로도 제품 구현, 표준, 인증, 적합성, 조달 승인, 운영 배포 판단이 아니다.
