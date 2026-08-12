# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-12 11:56:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7456	7.8467	0.8666	0.7404	159.4240
CNY	0.1482		1.1632	0.1285	0.1098	23.6338
HKD	0.1274	0.8597		0.1104	0.0944	20.3173
EUR	1.1539	7.7840	9.0546		0.8544	183.9649
GBP	1.3506	9.1108	10.5979	1.1704		215.3214
JPY	0.0063	0.0423	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*