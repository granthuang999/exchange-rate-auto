import pandas as pd
from datetime import datetime, timezone, timedelta
import json

def main():
    # 基础汇率
    rates = {
        'USD_CNY': 7.1860,
        'EUR_CNY': 8.3430, 
        'GBP_CNY': 9.6250,
        'HKD_CNY': 0.9100
    }
    
    # 创建矩阵
    matrix = [
        ['Currency', 'CNY', 'HKD', 'USD', 'EUR', 'GBP'],
        ['CNY', '', '1.0989', '0.1392', '0.1198', '0.1039'],
        ['HKD', '0.9100', '', '0.1267', '0.1090', '0.0946'], 
        ['USD', '7.1860', '7.8945', '', '0.8577', '0.7460'],
        ['EUR', '8.3430', '9.1703', '1.1660', '', '0.8700'],
        ['GBP', '9.6250', '10.5769', '1.3404', '1.1494', '']
    ]
    
    # 保存CSV
    df = pd.DataFrame(matrix[1:], columns=matrix[0])
    df.to_csv('exchange_rates.csv', index=False   
    # 保存JSON
    beijing_time = datetime.now(timezone(timedelta(hours=8)))
    data = {
        'rates': rates,
        'last_updated': beijing_time.i```ormat()
    }
    with open('exchange_rates.json', 'w') as f:
        json.dump(data, f, indent=2)
    
    # 更新README
    tsv_data = """Currency\tCNY\tHKD\tUSD\tEUR\tGBP
CNY\t\t1.0989\t0.1392\t0.1198\t0.1039
HKD\t0.9100\t\t0.1267\t0.1090\t0.0946
USD\t7.1860\t7.8945\t\t0.8577\t0.7460
EUR\t8.3430\t9.1703\t1.1660\t\t0.8700
GBP\t9.6250\t10.5769\t1.3404\t1.1494\t"""
    
    readme_content = f"""# 汇率数据

更新时间: {beijing_time.strftime('%Y-%m-%d %H:%M:%S')}

## Excel数据
{tsv_data}
    
## CSV链接
https://raw.githubusercontent.com/g```thuang999/exchange-rate-auto/main/exchange_rates.csv
"""
    
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print("Update completed")

if __name__ == "__main__":
    main()
