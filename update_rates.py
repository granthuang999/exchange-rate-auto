import requests
import csv
import json
from datetime import datetime, timezone, timedelta

# 目标货币顺序
CURRENCIES = ['USD', 'CNY', 'HKD', 'EUR', 'GBP']

# Wise 公共接口模板
WISE_API = 'https://wise.com/rates/live?source={source}&target={target}'

def fetch_wise_rate(source: str, target: str) -> float:
    url = WISE_API.format(source=source, target=target)
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    return round(float(data['rate']), 4)

def fetch_base_rates() -> dict:
    """
    以 USD 为基准获取其他货币汇率：USD→CNY、USD→HKD、USD→EUR、USD→GBP
    返回字典 { 'USD_CNY': 7.1860, ... }
    """
    pairs = [('USD', 'CNY'), ('USD', 'HKD'), ('USD', 'EUR'), ('USD', 'GBP')]
    base = {}
    for src, tgt in pairs:
        key = f'{src}_{tgt}'
        base[key] = fetch_wise_rate(src, tgt)
    return base

def build_matrix(base: dict) -> list:
    """
    构建以 USD 为基准的全交叉汇率矩阵：
    - 首行首列为 USD, CNY, HKD, EUR, GBP
    - USD→X 用 base ；X→Y 用 (1 / USD→X) * USD→Y
    """
    fmt = lambda x: f'{x:.4f}'
    # 取基本汇率
    usd_cny = base['USD_CNY']
    usd_hkd = base['USD_HKD']
    usd_eur = base['USD_EUR']
    usd_gbp = base['USD_GBP']

    # 交叉率计算函数
    def rate(src: str, tgt: str) -> str:
        if src == tgt:
            return ''
        if src == 'USD':
            return fmt(base[f'USD_{tgt}'])
        if tgt == 'USD':
            return fmt(1 / base[f'USD_{src}'])
        # src→tgt = (src→USD) * (USD→tgt)
        src_usd = 1 / base[f'USD_{src}']
        usd_tgt = base[f'USD_{tgt}']
        return fmt(src_usd * usd_tgt)

    matrix = [['Currency'] + CURRENCIES]
    for src in CURRENCIES:
        row = [src] + [rate(src, tgt) for tgt in CURRENCIES]
        matrix.append(row)
    return matrix

def save_csv(matrix: list):
    with open('exchange_rates.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(matrix)

def save_json(base: dict):
    data = {
        'base_rates': base,
        'last_updated': datetime.now(timezone(timedelta(hours=8))).isoformat()
    }
    with open('exchange_rates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_readme(matrix: list):
    now = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        '# 汇率数据自动更新',
        '',
        f'**更新时间**：{now}（北京时间）',
        '',
        '## Excel 表格（制表符分隔，复制粘贴）',
        ''
    ]
    for row in matrix:
        lines.append('\t'.join(row))
    lines += [
        '',
        '## CSV 文件直链',
        '',
        'https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv',
        '',
        '---',
        '*数据仅供参考*'
    ]
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

def main():
    base = fetch_base_rates()
    matrix = build_matrix(base)
    save_csv(matrix)
    save_json(base)
    update_readme(matrix)
    print('Exchange rates updated successfully!')

if __name__ == '__main__':
    main()
