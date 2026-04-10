# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-10 22:42:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8273	7.8318	0.8519	0.7422	159.1110
CNY	0.1465		1.1471	0.1248	0.1087	23.3051
HKD	0.1277	0.8717		0.1088	0.0948	20.3160
EUR	1.1738	8.0142	9.1933		0.8712	186.7719
GBP	1.3473	9.1987	10.5521	1.1478		214.3775
JPY	0.0063	0.0429	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*