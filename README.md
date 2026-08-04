# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-04 12:54:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7532	7.8420	0.8685	0.7448	157.5520
CNY	0.1481		1.1612	0.1286	0.1103	23.3300
HKD	0.1275	0.8612		0.1107	0.0950	20.0908
EUR	1.1514	7.7757	9.0294		0.8576	181.4070
GBP	1.3426	9.0671	10.5290	1.1661		211.5360
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