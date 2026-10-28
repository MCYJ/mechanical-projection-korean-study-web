# Mechanical Projection Korean Study

전산응용기계제도기능사 독립 학습 앱의 전용 정적 웹입니다. 한국어/영어 안내, 각10개 별도 작성 가이드, 실제 빌드8 화면, 웹 전용 한 칸 좌표 예제를 제공합니다. 앱 UI와 문제는 한국어입니다.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 scripts/preview.py
```

미리보기: http://127.0.0.1:8768/mechanical-projection-korean-study-web/ko/

`content/guides.json`이 가이드 원본이며 `scripts/author_guides.py`는 초기 저작 데이터를 재생성합니다. 디자인 토큰과 반응형 규칙은 `assets/site.css`에 있습니다. 웹 미니 예제는 메모리에서만 한 칸 좌표를 계산하며 네트워크·쿠키·로컬 저장소를 사용하지 않습니다.

실제 앱 출시 확인 전에는 준비 중 CTA를 유지합니다. 공식 기관 제휴·전체 시험 대비·CAD·공식 실기 채점·합격 보장을 주장하지 않습니다. Q-net 공식 안내로 연결하며 기관 본문이나 시험 문제를 재배포하지 않습니다. 앱 문제은행·서명 파일·비공개 앱 소스는 포함하지 않습니다.

로컬 검증: `qa/static-checks-v1.json`, `qa/browser-review-v1.json`. 배포 성공과 실제 운영 HTTPS 검증을 구분합니다. ©2026 RushLabs.
