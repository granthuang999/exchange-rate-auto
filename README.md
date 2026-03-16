# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-16 12:32:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8992	7.8286	0.8734	0.7545	159.6070
CNY	0.1449		1.1347	0.1266	0.1094	23.1341
HKD	0.1277	0.8813		0.1116	0.0964	20.3877
EUR	1.1450	7.8992	8.9634		0.8639	182.7422
GBP	1.3254	9.1441	10.3759	1.1576		211.5401
JPY	0.0063	0.0432	0.0490	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*