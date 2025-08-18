# update_rates.py  —— USD 基准 · Yahoo→Wise 双层数据源
import yfinance as yf
import requests
import csv, json
from datetime import datetime, timezone, timedelta

CURRENCIES = ['USD', 'CNY', 'HKD', 'EUR', 'GBP']
YF_TICKERS = {
    'USD_CNY': 'USDCNY=X',
    'USD_HKD': 'HKD=X',           # Yahoo 已固定为 1 HKD = ? USD，需要倒数处理
    'USD_EUR': 'EURUSD=X',
    'USD_GBP': 'GBPUSD=X'
}
WISE_TEMPLATE = 'https://wise.com/rates/live?source=USD&target={}'

# ---------- 1. Yahoo Finance ----------
def fetch_yahoo_rates() -> dict:
    rates = {}
    for k, ticker in YF_TICKERS.items():
        try:
            data = yf.Ticker(ticker)
            price = data.fast_info['lastPrice']
            if price and price > 0:
                # HKD=X 返回 1 HKD = ? USD，需倒数
                rates[k] = round(1 / price, 6) if k == 'USD_HKD' else round(price, 6)
        except Exception:
            pass
    return rates

# ---------- 2. Wise 备选（逐个币种） ----------
def fetch_wise_rate(target: str) -> float:
    try:
        r = requests.get(WISE_TEMPLATE.format(target), timeout=10)
        r.raise_for_status()
        return round(float(r.json()['rate']), 6)
    except Exception:
        return None

# ---------- 3. 获取基础汇率 USD→X ----------
def get_base_rates() -> dict:
    base = fetch_yahoo_rates()
    # 若某币种缺失则用 Wise
    for tgt in ['CNY', 'HKD', 'EUR', 'GBP']:
        key = f'USD_{tgt}'
        if key not in base:
            wise_rate = fetch_wise_rate(tgt)
            if wise_rate:
                base[key] = wise_rate
    # 若仍有缺口则抛错并退出
    missing = [k for k in ['USD_CNY', 'USD_HKD', 'USD_EUR', 'USD_GBP'] if k not in base]
    if missing:
        raise RuntimeError(f'基础汇率缺失：{missing}')
    return base

# ---------- 4. 构建交叉矩阵 ----------
def build_matrix(b: dict) -> list:
    u2cny, u2hkd, u2eur, u2gbp = b['USD_CNY'], b['USD_HKD'], b['USD_EUR'], b['USD_GBP']
    fmt = lambda x: f'{x:.6f}'
    def val(src, tgt):
        if src == tgt: return ''
        if src == 'USD': return fmt(b[f'USD_{tgt}'])
        if tgt == 'USD': return fmt(1 / b[f'USD_{src}'])
        return fmt((1 / b[f'USD_{src}']) * b[f'USD_{tgt}'])
    m = [['Currency'] + CURRENCIES]
    for s in CURRENCIES:
        m.append([s] + [val(s, t) for t in CURRENCIES])
    return m

# ---------- 5. 写文件 ----------
def save_csv(matrix):
    with open('exchange_rates.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(matrix)

def save_json(base):
    with open('exchange_rates.json', 'w', encoding='utf-8') as f:
        json.dump(
            {'base_rates': base,
             'last_updated': datetime.now(timezone.utc).astimezone(
                 timezone(timedelta(hours=8))).isoformat(),
             'source': 'Yahoo Finance → Wise fallback'},
            f, ensure_ascii=False, indent=2)

def save_readme(matrix):
    ts = datetime.now(timezone.utc).astimezone(
        timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        '# 汇率自动表（USD 基准）', '',
        f'更新时间（北京时间）：{ts}', '',
        '## 制表符格式，可粘贴 Excel', ''
    ] + ['\t'.join(r) for r in matrix] + [
        '', 'CSV：',
        'https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv',
        '', '> 数据来源：先 Yahoo Finance，若失败则 Wise；无更多备用。',
        ''
    ]
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# ---------- 6. 主入口 ----------
def main():
    base = get_base_rates()
    matrix = build_matrix(base)
    save_csv(matrix)
    save_json(base)
    save_readme(matrix)
    print('Update completed.')

if __name__ == '__main__':
    main()
