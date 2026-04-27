# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-27 13:16:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8282	7.8360	0.8526	0.7387	159.2790
CNY	0.1465		1.1476	0.1249	0.1082	23.3266
HKD	0.1276	0.8714		0.1088	0.0943	20.3266
EUR	1.1729	8.0087	9.1907		0.8664	186.8156
GBP	1.3537	9.2435	10.6078	1.1542		215.6207
JPY	0.0063	0.0429	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*