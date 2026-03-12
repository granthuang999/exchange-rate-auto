# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-12 12:06:13（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8788	7.8248	0.8664	0.7479	159.0340
CNY	0.1454		1.1375	0.1260	0.1087	23.1194
HKD	0.1278	0.8791		0.1107	0.0956	20.3244
EUR	1.1542	7.9395	9.0314		0.8632	183.5572
GBP	1.3371	9.1975	10.4624	1.1584		212.6407
JPY	0.0063	0.0433	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*