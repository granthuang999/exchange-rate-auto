# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-13 12:52:15（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8321	7.8325	0.8554	0.7460	159.7270
CNY	0.1464		1.1464	0.1252	0.1092	23.3789
HKD	0.1277	0.8723		0.1092	0.0952	20.3929
EUR	1.1690	7.9870	9.1565		0.8721	186.7278
GBP	1.3405	9.1583	10.4993	1.1466		214.1113
JPY	0.0063	0.0428	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*