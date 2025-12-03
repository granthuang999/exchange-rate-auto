# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-03 11:10:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0651	7.7821	0.8589	0.7559	155.7120
CNY	0.1415		1.1015	0.1216	0.1070	22.0396
HKD	0.1285	0.9079		0.1104	0.0971	20.0090
EUR	1.1643	8.2258	9.0605		0.8801	181.2924
GBP	1.3229	9.3466	10.2951	1.1363		205.9955
JPY	0.0064	0.0454	0.0500	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*