# 전산제도 입체·좌표 학습 전용 웹 컨텍스트

- 서비스 HRDK-0472 / app.mcyj.examprep.hrdk0472 / RushLabs. 기존 앱 저장소는 private 유지.
- 앱 심사 제출 요청의 marketing-release-policy에 따라 앱별 독립 정적 GitHub Pages 웹을 준비한다. 기존 중앙 portfolio171과 verified-website-records에서 정확 서비스/패키지/앱명 일치0. GitHub mechanical 검색의 결과는 별도 기계경비지도사 웹으로 본 앱이 아니다. 미색인 저장소까지 부재를 단정하지 않는다.
- 현재 앱은 iOS 빌드7 심사 대기, 새8의 입체·좌표 투영 노트 검증 중. 스토어 출시/승인 링크는 게시하지 않고 출시 준비 중 CTA 사용.
- 실제 새8 화면과 제도지·원형부품·치수선의 검토된 그림 아이콘을 재사용. 은행·서명키·원본 앱 소스 공개 금지.
- 한국어/영어 우선, 독자 가이드10개씩과 기능/학습흐름/공식시험출처/FAQ/지원/문의/개인정보/이용/404 구성. 앱 화면과 문제는 한국어임을 분리한다.
- 가상3×3×3 채움 투영 모형만 설명한다. CAD, 숨은선, 치수·공차·규격도면 적합성, 공식 실기 채점/기출/합격보장 아님. 사이트는 오프라인 앱 기능 검증 범위만 소개한다.
- canonical/hreflang/sitemap/robots/OG/정확한 구조화 데이터, 모바일 keep-all, 키보드 접근성, 실제 HTTPS 배포/링크/화면 검증이 완료 게이트다.
- 공식 시험 URL https://www.q-net.or.kr/crf005.do?id=crf00503s02&jmCd=6151&jmInfoDivCcd=B0 (2026-10-28 재확인). 시험 일정·수수료는 복제하지 않고 공식 안내로 연결한다.
- 구현/게시/운영 QA는 아직 미완료.

## 2026-10-28 로컬 구현·검증
- 한국어/영어 각10개 독자 가이드, 기능/흐름/공식출처/FAQ/지원/문의/개인정보/이용/404를 구현했다. 실제 빌드8 화면3개와 검토한 제도 그림 아이콘만 재사용했다. 앱은행·서명·앱 소스는 없다.
-42HTML/41indexable routes, 내부링크1048, canonical/hreflang/alt/구조화데이터·미검증Store링크0·전송폼0·JS네트워크/저장0 검사를 통과했다. Chrome390px40페이지 가로넘침/깨진이미지0,320px가이드해설과좌표(2,1,2)→XZ(2,2)/XY(2,1)/YZ(1,2)를 실제키보드로 확인했다. 입력컨테이너를 전송없는group으로 바꾼 뒤4관련페이지와기능을재확인했다. 임시viewport는복구했다.
- 출시는준비중이며 실제배포/HTTPS운영검증은 다음 게이트다.

## 2026-10-28 운영 게시 검증
- 공개 전용 저장소 https://github.com/MCYJ/mechanical-projection-korean-study-web 와 GitHub Pages https://mcyj.github.io/mechanical-projection-korean-study-web/ 를 게시했다. 앱 원본 저장소 가시성은 변경하지 않았다.
- 첫 배포는 Pages 활성화 이전 configure-pages가 실행돼 실패했다. 활성화를 직접 확인한 뒤 동일 커밋5e2efd11be8eb8968248fd91a5513c29393c0d61/동일 run40637670523의두번째시도 성공을 확인했다. 실패 원본을 보존했다.
- 인증된 원격 소스20파일과 로컬blob일치, 실제HTTPS50리소스 전체바이트와404상태/본문을 확인했다. 운영Chrome한국어데스크톱·영어모바일·실제언어전환·키보드좌표예제·가이드해설을 확인했다. 임시viewport는복구했다. 최초이미지초기페인트는스크롤후실제로표시됨을직접점검했다.
- 앱은 출시준비중으로표시한다. 앱심사승인·공개를주장하지않으며다운로드링크는0이다. 검증 qa/production-summary-v1.json 및qa/production-browser-review-v1.json. 이문서/QA추가는사이트빌드입력을바꾸지않는다.
