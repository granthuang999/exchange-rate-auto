# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-20 22:37:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8852	7.8337	0.8669	0.7509	159.0930
CNY	0.1452		1.1378	0.1259	0.1091	23.1065
HKD	0.1277	0.8789		0.1107	0.0959	20.3088
EUR	1.1535	7.9423	9.0365		0.8662	183.5194
GBP	1.3317	9.1693	10.4324	1.1545		211.8698
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