# Feature Gap Analysis: Financial Planning Simulator

> Based on web research of top financial planning tools (2025-2026)
> Date: 2026-03-29

---

## A. Existing Tab Enhancements

### Tab 2: 실수령액 (Take-Home Pay) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 1 | **연말정산 시뮬레이터** | 신용카드/체크카드 사용 비율, 의료비, 교육비, 기부금, 연금저축 등 공제 항목별 입력 -> 예상 환급액/추가납부액 계산 | KB Think, 국세청 홈택스 |
| 2 | **절세 최적화 추천** | 현재 소비 패턴 입력 시 "체크카드 비율을 X%로 올리면 Y만원 추가 환급" 등 구체적 절세 전략 자동 제안 | Quarterback 종합소득세 계산기 |
| 3 | **프리랜서/N잡러 세금 모드** | 종합소득세 기준 계산, 3.3% 원천징수 vs 근로소득세 비교, 사업자등록 시 절세 효과 시뮬레이션 | Quarterback |
| 4 | **퇴직금 시뮬레이션** | 근속연수별 퇴직금 예상액, DC/DB형 퇴직연금 비교, IRP 추가 납입 시 절세 효과 | NerdWallet |

### Tab 3: 생활비 (Living Expenses) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 5 | **비상금 계산기** | 소득/부양가족/고정지출 기반 적정 비상금 목표액 산출 (단순 3~6개월이 아닌 리스크 가중치 적용) | Emergency Fund Calculator |
| 6 | **지역별 생활비 비교** | 서울/경기/지방 도시별 주거비+생활비 차이 반영, 이직 시 실질소득 비교 | NerdWallet Cost of Living |
| 7 | **인플레이션 반영 장기 생활비** | 연간 물가상승률 적용하여 5/10/20년 후 같은 생활수준 유지에 필요한 금액 시각화 | ProjectionLab |

### Tab 4: 목표설정 (Goal Setting) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 8 | **라이프이벤트 타임라인** | 결혼/출산/내집마련/자녀교육/은퇴 등 이벤트를 타임라인에 배치, 각 이벤트의 재정 임팩트 자동 계산 | ProjectionLab |
| 9 | **역산 저축률 계산기** | "35세까지 1억 모으려면 월 X만원 저축 필요" -> 현재 지출에서 어디를 줄여야 하는지까지 제안 | Playing With FIRE |
| 10 | **Sankey 다이어그램** | 수입 -> 세금/저축/소비/투자 흐름을 Sankey 차트로 시각화 | ProjectionLab |

### Tab 6: 마일스톤 (Milestone) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 11 | **순자산 마일스톤 트래커** | 1,000만/5,000만/1억/5억 등 자산 마일스톤 달성 예상 시점 + 달성 시 축하/알림 | Monarch Money, Empower |
| 12 | **진행률 게이지** | 각 목표별 진행률을 프로그레스바/게이지로 시각화, 온트랙/오프트랙 상태 표시 | PocketSmith |
| 13 | **과거 vs 계획 비교** | 실제 자산 증가 추이 vs 초기 계획 대비 진행률 비교 그래프 | ProjectionLab Journal |

### Tab 7: 또래비교 (Peer Comparison) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 14 | **직업/학력별 세분화 비교** | 단순 나이 비교가 아닌 "같은 학력 + 같은 직종" 세그먼트 내 백분위 | 고용노동부 임금정보시스템 |
| 15 | **자산 구성 비교** | 부동산/금융자산/부채 비율을 또래 평균과 비교하는 레이더 차트 | Empower Dashboard |

### Tab 9: 이직타이밍 (Job-Hop Timing) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 16 | **연봉 협상 시뮬레이터** | 희망 인상률 입력 -> 세후 실질 인상액, 인플레이션 감안 실질 상승률 계산 | Snap-Tool 연봉협상계산기 |
| 17 | **앵커링 효과 시각화** | 초봉 차이가 5/10/20년 후 누적 소득에 미치는 영향을 그래프로 시각화 | 기존 분석 확장 |
| 18 | **이직 전후 실질소득 비교** | 연봉 + 복리후생(식대/교통비/자기계발비/스톡옵션) 포함 총보상 패키지 비교 | FindSkill AI Simulator |

### Tab 10: FIRE (Early Retirement) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 19 | **Monte Carlo 시뮬레이션** | 1,000회 시뮬레이션으로 포트폴리오 생존율(%) 계산. 시장 폭락/호황 시나리오 포함 | Portfolio Visualizer, InvestingFIRE |
| 20 | **FIRE 유형별 계산** | Lean/Standard/Fat/Coast/Barista FIRE 각각의 필요 금액 및 달성 시점 비교 | My FIRE Number, The FIRE Calculator |
| 21 | **인출 전략 비교** | 4% 룰 vs 가변 인출 vs 기대수명 기반 인출 등 전략별 자금 소진 시점 비교 | Boldin, Honest Math |
| 22 | **성공 확률 대시보드** | 80~95% 신뢰구간 범위로 결과 분포 시각화 (부채꼴 차트) | T. Rowe Price |

### Tab 11: 재테크 (Investment) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 23 | **리밸런싱 계산기** | 현재 보유 자산 입력 -> 목표 비율 대비 매수/매도 금액 자동 계산 | Portseido, WalletBurst |
| 24 | **리밸런싱 방식 선택** | 매수/매도(빠름) vs 현금흐름(저비용) vs 부분(균형) 방식 비교 | OnePortfolio |
| 25 | **백테스트** | 과거 수익률 데이터 기반 포트폴리오 성과 검증 (KOSPI/S&P500/채권 등) | Portfolio Visualizer |
| 26 | **복리 스노우볼 시각화** | 원금 vs 이자수익 분리 스택 바 차트, 시간이 갈수록 이자가 원금을 압도하는 시각적 표현 | CompoundChart, WalletBurst |
| 27 | **배당 재투자 시뮬레이션** | 배당금 재투자 vs 현금 수령 시 장기 자산 차이 비교 | Sure Dividend |
| 28 | **ISA/연금저축 절세 투자** | ISA 계좌 비과세 한도, 연금저축+IRP 세액공제 효과를 투자 수익률에 통합 계산 | Quarterback |

### Tab 12: 종합자산 (Total Asset) - Enhancements

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 29 | **순자산 추이 차트** | 월별/분기별 순자산 변화 추이 라인 차트 + 자산 구성 변화 스택 차트 | Empower, Monarch Money |
| 30 | **자산/부채 분류 대시보드** | 유동자산/비유동자산/유동부채/비유동부채로 세분화된 대차대조표 형식 | Know Your Dosh |
| 31 | **미래 순자산 예측** | 현재 추세 기반 1/3/5/10년 후 순자산 예측 곡선 | PocketSmith Forecasting |

---

## B. New Tabs to Add

### New Tab 13: 부동산 (Real Estate)

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 32 | **주택담보대출 시뮬레이터** | LTV/DTI/DSR 기준 대출 가능액 계산, 원리금균등/원금균등/만기일시 상환 비교 | 부동산계산기.com, 금융감독원 |
| 33 | **전세 vs 월세 vs 매매 비교** | 전월세전환율 적용, 5/10/20년 총비용 비교, 자가 매매 시 자산 축적 효과 포함 | 핀다, MiniWebTool |
| 34 | **청약 가점 계산기** | 무주택기간/부양가족/청약통장 가입기간 기반 가점 계산, 당첨 가능성 분석 | 한국부동산원 청약홈 |
| 35 | **내집마련 로드맵** | 목표 아파트 가격 입력 -> 필요 자기자본금/대출액/월 상환액 역산, 달성 시점 시뮬레이션 | ProjectionLab |
| 36 | **부동산 vs 금융투자 비교** | 같은 금액을 전세+투자 vs 매매로 운용 시 10/20/30년 자산 비교 | Various |

### New Tab 14: 부채관리 (Debt Management)

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 37 | **부채 상환 전략 비교** | 스노우볼(소액부터) vs 애벌런치(고금리부터) 전략별 총 이자/기간 비교 시뮬레이션 | SmartFinPro, NerdWallet |
| 38 | **대출 통합 시뮬레이터** | 여러 대출을 하나로 통합 시 이자 절감 효과 계산 | Calculator.net |
| 39 | **학자금 대출 상환 계산기** | ICL(취업후상환) 기준 소득 구간별 상환액, 총 상환 기간 시뮬레이션 | 한국장학재단 |

### New Tab 15: 보험/안전망 (Insurance & Safety Net)

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 40 | **적정 보험 계산기** | 소득/부양가족/자산 기반 필요 보장액 계산 (생명보험/실손/자동차) | Financial Mentor |
| 41 | **국민연금 수령액 시뮬레이터** | 가입기간/평균소득 기반 예상 수령액 + FIRE 계산에 통합 | 국민연금공단 |
| 42 | **4대보험 총비용 대시보드** | 연봉 구간별 4대보험 본인부담금 + 사업주부담금 총 비용 시각화 | 기존 탭 확장 가능 |

---

## C. Cross-Tab Infrastructure Features

| # | Feature | Description | Reference |
|---|---------|-------------|-----------|
| 43 | **시나리오 저장/비교** | 여러 인생 시나리오(A안/B안/C안)를 저장하고 나란히 비교하는 대시보드 | ProjectionLab |
| 44 | **데이터 영속성** | 입력한 데이터를 localStorage 또는 서버에 저장, 재방문 시 복원 | Empower, Monarch |
| 45 | **PDF/이미지 내보내기** | 시뮬레이션 결과를 PDF 리포트 또는 이미지로 내보내기 | Various |
| 46 | **모바일 반응형** | 모바일에서도 사용 가능한 반응형 UI | All modern tools |
| 47 | **다크모드** | 다크모드 지원 | UX best practice |
| 48 | **인터랙티브 차트** | Chart.js 기반 드래그/줌/호버 툴팁 지원 인터랙티브 차트 | CompoundChart |
| 49 | **가정값 프리셋** | "보수적/중립/공격적" 투자 수익률, "서울/지방" 생활비 등 프리셋 원클릭 적용 | FIREkit |
| 50 | **공유 링크** | 시뮬레이션 설정을 URL 파라미터로 인코딩하여 공유 가능 | Various |

---

## D. Priority Implementation Recommendation

### Phase 1 (High Impact, Moderate Effort)
1. **Monte Carlo 시뮬레이션** (#19) - FIRE 탭의 신뢰성 대폭 향상
2. **복리 스노우볼 시각화** (#26) - 투자 동기 부여에 매우 효과적
3. **연말정산 시뮬레이터** (#1) - 한국 직장인에게 즉시 실용적
4. **부동산 탭 신설** (#32-36) - 한국인의 최대 자산 = 부동산

### Phase 2 (High Impact, Higher Effort)
5. **Sankey 다이어그램** (#10) - 시각적 임팩트 큼
6. **라이프이벤트 타임라인** (#8) - 장기 재정 계획의 핵심
7. **부채 상환 전략** (#37) - 사회초년생에게 필수
8. **리밸런싱 계산기** (#23) - 투자 탭 완성도 향상

### Phase 3 (Nice-to-Have)
9. 데이터 영속성 (#44)
10. PDF 내보내기 (#45)
11. 시나리오 저장/비교 (#43)
12. 보험/안전망 탭 (#40-42)
