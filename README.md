# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-14 12:39:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8167	7.8316	0.8496	0.7398	159.0850
CNY	0.1467		1.1489	0.1246	0.1085	23.3375
HKD	0.1277	0.8704		0.1085	0.0945	20.3132
EUR	1.1770	8.0234	9.2180		0.8708	187.2469
GBP	1.3517	9.2142	10.5861	1.1484		215.0378
JPY	0.0063	0.0428	0.0492	0.0053	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*