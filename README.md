# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-22 12:39:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8219	7.8308	0.8516	0.7403	159.3300
CNY	0.1466		1.1479	0.1248	0.1085	23.3557
HKD	0.1277	0.8712		0.1088	0.0945	20.3466
EUR	1.1743	8.0107	9.1954		0.8693	187.0949
GBP	1.3508	9.2150	10.5779	1.1503		215.2236
JPY	0.0063	0.0428	0.0491	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*