# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-26 22:11:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1540	7.7985	0.8581	0.7422	147.6630
CNY	0.1398		1.0901	0.1199	0.1037	20.6406
HKD	0.1282	0.9174		0.1100	0.0952	18.9348
EUR	1.1654	8.3370	9.0881		0.8649	172.0813
GBP	1.3473	9.6389	10.5073	1.1562		198.9531
JPY	0.0068	0.0484	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*