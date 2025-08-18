import requests
import csv
import json
from datetime import datetime, timezone, timedelta
import time

CURRENCIES = ['USD', 'CNY', 'HKD', 'EUR', 'GBP', 'JPY']

# ---------- 1. Yahoo Finance API (免费接口) ----------
def fetch_yahoo_rates() -> dict:
    """使用 Yahoo Finance 查询 API 获取汇率"""
    rates = {}
    symbols = {
        'USD_CNY': 'USDCNY=X',
        'USD_HKD': 'USDHKD=X', 
        'USD_EUR': 'USDEUR=X',
        'USD_GBP': 'USDGBP=X',
        'USD_JPY': 'USDJPY=X'
    }
    
    for key, symbol in symbols.items():
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'chart' in data and data['chart']['result']:
                    result = data['chart']['result'][0]
                    if 'meta' in result and 'regularMarketPrice' in result['meta']:
                        price = result['meta']['regularMarketPrice']
                        if price and price > 0:
                            rates[key] = round(price, 6)
                            print(f"Yahoo {key}: {price}")
            
            time.sleep(0.2)  # 避免请求过快
            
        except Exception as e:
            print(f"Yahoo {key} failed: {e}")
            continue
    
    return rates

# ---------- 2. Wise API 备选 ----------
def fetch_wise_rate(target: str) -> float:
    """从 Wise 获取 USD 到目标货币的汇率"""
    try:
        url = f"https://wise.com/rates/live?source=USD&target={target}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Accept': 'application/json'
        }
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if 'rate' in data:
                rate = float(data['rate'])
                print(f"Wise USD_{target}: {rate}")
                return round(rate, 6)
        
    except Exception as e:
        print(f"Wise USD_{target} failed: {e}")
    
    return None

# ---------- 3. ExchangeRate-API 作为最后备选 ----------
def fetch_exchangerate_api() -> dict:
    """使用 ExchangeRate-API 获取基于 USD 的汇率"""
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            rates = data.get('rates', {})
            result = {}
            
            for target in ['CNY', 'HKD', 'EUR', 'GBP']:
                if target in rates:
                    result[f'USD_{target}'] = round(rates[target], 6)
                    print(f"ExchangeRate-API USD_{target}: {rates[target]}")
            
            return result
            
    except Exception as e:
        print(f"ExchangeRate-API failed: {e}")
    
    return {}

# ---------- 4. 获取基础汇率 ----------
def get_base_rates() -> dict:
    """按优先级获取汇率：Yahoo -> Wise -> ExchangeRate-API"""
    print("尝试从 Yahoo Finance 获取汇率...")
    base = fetch_yahoo_rates()
    
    # 检查缺失的货币对，用 Wise 补充
    missing = []
    for target in ['CNY', 'HKD', 'EUR', 'GBP', 'JPY']:
        key = f'USD_{target}'
        if key not in base:
            missing.append(target)
    
    if missing:
        print(f"Yahoo 缺失 {missing}，尝试 Wise...")
        for target in missing:
            wise_rate = fetch_wise_rate(target)
            if wise_rate:
                base[f'USD_{target}'] = wise_rate
    
    # 如果还有缺失，使用 ExchangeRate-API
    still_missing = [target for target in ['CNY', 'HKD', 'EUR', 'GBP', 'JPY'] 
                    if f'USD_{target}' not in base]
    
    if still_missing:
        print(f"仍缺失 {still_missing}，尝试 ExchangeRate-API...")
        api_rates = fetch_exchangerate_api()
        base.update(api_rates)
    
    # 最终检查
    required = ['USD_CNY', 'USD_HKD', 'USD_EUR', 'USD_GBP', 'USD_JPY']
    final_missing = [k for k in required if k not in base]
    
    if final_missing:
        raise RuntimeError(f'无法获取基础汇率：{final_missing}')
    
    print(f"最终基础汇率：{base}")
    return base

# ---------- 5. 构建交叉矩阵 ----------
def build_matrix(base: dict) -> list:
    """以 USD 为基准构建交叉汇率矩阵"""
    fmt = lambda x: f'{x:.4f}'
    
    def get_rate(src: str, tgt: str) -> str:
        if src == tgt:
            return ''
        if src == 'USD':
            return fmt(base[f'USD_{tgt}'])
        if tgt == 'USD':
            return fmt(1 / base[f'USD_{src}'])
        # 交叉汇率：src->USD->tgt
        src_to_usd = 1 / base[f'USD_{src}']
        usd_to_tgt = base[f'USD_{tgt}']
        return fmt(src_to_usd * usd_to_tgt)
    
    matrix = [['Currency'] + CURRENCIES]
    for src in CURRENCIES:
        row = [src] + [get_rate(src, tgt) for tgt in CURRENCIES]
        matrix.append(row)
    
    return matrix

# ---------- 6. 文件保存 ----------
def save_csv(matrix: list):
    with open('exchange_rates.csv', 'w', newline='', encoding='utf-8') as f:
        csv.writer(f).writerows(matrix)

def save_json(base: dict):
    data = {
        'base_rates': base,
        'last_updated': datetime.now(timezone(timedelta(hours=8))).isoformat(),
        'source': 'Yahoo Finance -> Wise -> ExchangeRate-API'
    }
    with open('exchange_rates.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_readme(matrix: list):
    beijing_time = datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
    lines = [
        '# 汇率数据自动更新（美元基准）',
        '',
        f'**更新时间**：{beijing_time}（北京时间）',
        '',
        '## Excel 表格（制表符分隔）',
        ''
    ]
    
    for row in matrix:
        lines.append('\t'.join(row))
    
    lines += [
        '',
        '## CSV 文件链接',
        '',
        'https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv',
        '',
        '### 数据源说明',
        '- 优先使用 Yahoo Finance 实时汇率',
        '- Yahoo 失败时使用 Wise 汇率',
        '- 最后备选 ExchangeRate-API',
        '- 以美元为基准计算所有交叉汇率',
        '',
        '---',
        '*数据仅供参考，交易请以银行报价为准*'
    ]
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))

# ---------- 7. 主程序 ----------
def main():
    try:
        base = get_base_rates()
        matrix = build_matrix(base)
        save_csv(matrix)
        save_json(base)
        save_readme(matrix)
        print('汇率数据更新成功！')
    except Exception as e:
        print(f'更新失败：{e}')
        raise

if __name__ == '__main__':
    main()
