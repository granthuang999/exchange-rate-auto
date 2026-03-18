# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-18 22:56:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8721	7.8356	0.8684	0.7507	159.4730
CNY	0.1455		1.1402	0.1264	0.1092	23.2059
HKD	0.1276	0.8770		0.1108	0.0958	20.3524
EUR	1.1515	7.9135	9.0230		0.8645	183.6400
GBP	1.3321	9.1543	10.4377	1.1568		212.4324
JPY	0.0063	0.0431	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*