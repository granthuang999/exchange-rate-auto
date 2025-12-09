# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-09 11:12:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0696	7.7787	0.8584	0.7502	155.8870
CNY	0.1415		1.1003	0.1214	0.1061	22.0503
HKD	0.1286	0.9088		0.1104	0.0964	20.0402
EUR	1.1650	8.2358	9.0619		0.8740	181.6018
GBP	1.3330	9.4236	10.3688	1.1442		207.7939
JPY	0.0064	0.0454	0.0499	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*