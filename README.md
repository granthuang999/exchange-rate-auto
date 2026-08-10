# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-10 11:43:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7458	7.8446	0.8656	0.7416	158.2050
CNY	0.1482		1.1629	0.1283	0.1099	23.4524
HKD	0.1275	0.8599		0.1103	0.0945	20.1674
EUR	1.1553	7.7932	9.0626		0.8567	182.7692
GBP	1.3484	9.0963	10.5779	1.1672		213.3293
JPY	0.0063	0.0426	0.0496	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*