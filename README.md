# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-05 00:07:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7527	7.8431	0.8677	0.7435	157.5170
CNY	0.1481		1.1615	0.1285	0.1101	23.3265
HKD	0.1275	0.8610		0.1106	0.0948	20.0835
EUR	1.1525	7.7823	9.0390		0.8569	181.5339
GBP	1.3450	9.0823	10.5489	1.1670		211.8588
JPY	0.0063	0.0429	0.0498	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*