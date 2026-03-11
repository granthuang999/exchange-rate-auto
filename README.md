# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-11 12:02:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8641	7.8267	0.8597	0.7434	158.2310
CNY	0.1457		1.1402	0.1252	0.1083	23.0520
HKD	0.1278	0.8770		0.1098	0.0950	20.2168
EUR	1.1632	7.9843	9.1040		0.8647	184.0537
GBP	1.3452	9.2334	10.5282	1.1564		212.8477
JPY	0.0063	0.0434	0.0495	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*