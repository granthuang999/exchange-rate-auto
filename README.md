# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-09 22:16:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9767	7.7938	0.8586	0.7450	157.8740
CNY	0.1433		1.1171	0.1231	0.1068	22.6287
HKD	0.1283	0.8952		0.1102	0.0956	20.2564
EUR	1.1647	8.1257	9.0773		0.8677	183.8737
GBP	1.3423	9.3647	10.4615	1.1525		211.9114
JPY	0.0063	0.0442	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*