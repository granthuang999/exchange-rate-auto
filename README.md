# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-27 23:28:47（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8223	7.8368	0.8521	0.7380	159.2710
CNY	0.1466		1.1487	0.1249	0.1082	23.3456
HKD	0.1276	0.8705		0.1087	0.0942	20.3235
EUR	1.1736	8.0065	9.1970		0.8661	186.9159
GBP	1.3550	9.2443	10.6190	1.1546		215.8144
JPY	0.0063	0.0428	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*