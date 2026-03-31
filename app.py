#!/usr/bin/env python3
"""
소득 & 재테크 통합 시뮬레이터 웹 서버
실행: conda run python web-simulator/app.py
접속: http://localhost:9847
"""

import json
import webbrowser
from threading import Timer
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
PORT = 9847


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/simulate', methods=['POST'])
def simulate():
    params = request.json
    result = run_simulation(params)
    return jsonify(result)


def run_simulation(params):
    """서버사이드 시뮬레이션 (CSV 다운로드용)"""
    from_year = 2023
    to_year = params.get('endYear', 2060)
    it_salary = params.get('itSalary', 3500)
    growth = params.get('growth', {})

    careers = {}
    for key, config in CAREER_CONFIGS.items():
        careers[key] = calc_public(config, to_year)

    it_data = calc_it(it_salary, end_year=to_year, **growth)
    careers['it'] = it_data

    # 누적
    cums = {}
    for k, v in careers.items():
        cums[k] = cumulative(v, from_year, to_year)

    # 결과 구성
    years = list(range(from_year, to_year + 1))
    result = {
        'years': years,
        'careers': {},
    }

    for k, v in careers.items():
        name = CAREER_CONFIGS[k]['name'] if k != 'it' else f'IT({it_salary}만)'
        result['careers'][k] = {
            'name': name,
            'salaries': [v.get(y, {}).get('salary', 0) for y in years],
            'cumulative': [cums[k].get(y, 0) for y in years],
            'ranks': [v.get(y, {}).get('rank', '') for y in years],
        }

    return result


# ---- 급여 모델 (서버사이드) ----

CAREER_CONFIGS = {
    'police': {
        'name': '경찰 조기임용(03생)', 'start_year': 2024,
        'ranks': [(1,'순경',3700,0.07),(5,'경장',5000,0.05),(10,'경사',6300,0.04),
                  (16,'경위',7850,0.03),(24,'경감',9900,0.025),(32,'총경',11200,0.02)],
    },
    'civil7': {
        'name': '7급 공무원', 'start_year': 2027,
        'ranks': [(1,'7급',3400,0.06),(7,'6급',4800,0.045),(15,'5급',6500,0.035),(25,'4급',8200,0.025)],
    },
    'officer': {
        'name': '장교(소위임관)', 'start_year': 2027,
        'ranks': [(1,'소위',3300,0.08),(3,'중위',4200,0.06),(7,'대위',5500,0.05),
                  (14,'소령',7200,0.04),(18,'중령',8800,0.03),(24,'대령',10500,0.025)],
    },
    'fire': {
        'name': '소방공무원', 'start_year': 2027,
        'ranks': [(1,'소방사',3600,0.07),(5,'소방교',4900,0.05),(10,'소방장',6200,0.04),
                  (16,'소방위',7700,0.03),(24,'소방경',9700,0.025),(32,'소방령',11000,0.02)],
    },
    'civil9': {
        'name': '9급 공무원', 'start_year': 2027,
        'ranks': [(1,'9급',2900,0.07),(4,'8급',3600,0.06),(8,'7급',4400,0.05),
                  (14,'6급',5600,0.04),(22,'5급',7000,0.03)],
    },
}


def calc_public(config, end_year=2060):
    ranks = config['ranks']
    start_year = config['start_year']
    result = {}
    salary = ranks[0][2]
    rank_idx = 0
    for year in range(start_year, end_year + 1):
        seniority = year - start_year + 1
        if rank_idx + 1 < len(ranks) and seniority >= ranks[rank_idx + 1][0]:
            rank_idx += 1
            salary = ranks[rank_idx][2]
        result[year] = {'salary': round(salary), 'rank': ranks[rank_idx][1], 'seniority': seniority}
        salary *= (1 + ranks[rank_idx][3])
    return result


def calc_it(starting_salary, start_year=2027, end_year=2060, **growth):
    g = {
        'growth_early': growth.get('growth_early', 7),
        'growth_jump1': growth.get('growth_jump1', 15),
        'growth_mid': growth.get('growth_mid', 6),
        'growth_jump2': growth.get('growth_jump2', 12),
        'growth_late': growth.get('growth_late', 5),
        'growth_senior': growth.get('growth_senior', 4),
        'growth_veteran': growth.get('growth_veteran', 3),
    }
    result = {}
    salary = starting_salary
    for year in range(start_year, end_year + 1):
        seniority = year - start_year + 1
        result[year] = {'salary': round(salary), 'rank': f'{seniority}년차', 'seniority': seniority}
        if seniority == 3: gr = g['growth_jump1'] / 100
        elif seniority == 6: gr = g['growth_jump2'] / 100
        elif seniority <= 2: gr = g['growth_early'] / 100
        elif seniority <= 5: gr = g['growth_mid'] / 100
        elif seniority <= 10: gr = g['growth_late'] / 100
        elif seniority <= 15: gr = g['growth_senior'] / 100
        else: gr = g['growth_veteran'] / 100
        salary *= (1 + gr)
    return result


def cumulative(data, from_year, to_year):
    total = 0
    result = {}
    for y in range(from_year, to_year + 1):
        total += data.get(y, {}).get('salary', 0)
        result[y] = total
    return result


def open_browser():
    webbrowser.open(f'http://localhost:{PORT}')


if __name__ == '__main__':
    print(f'\n  ╔══════════════════════════════════════════╗')
    print(f'  ║  소득 & 재테크 통합 시뮬레이터            ║')
    print(f'  ║  http://localhost:{PORT}                   ║')
    print(f'  ║  종료: Ctrl+C                             ║')
    print(f'  ╚══════════════════════════════════════════╝\n')

    Timer(1.5, open_browser).start()
    app.run(host='127.0.0.1', port=PORT, debug=False)
