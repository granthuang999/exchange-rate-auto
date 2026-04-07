# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-07 22:59:45（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8562	7.8357	0.8639	0.7549	159.9580
CNY	0.1459		1.1429	0.1260	0.1101	23.3304
HKD	0.1276	0.8750		0.1103	0.0963	20.4140
EUR	1.1575	7.9363	9.0701		0.8738	185.1580
GBP	1.3247	9.0823	10.3798	1.1444		211.8930
JPY	0.0063	0.0429	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*