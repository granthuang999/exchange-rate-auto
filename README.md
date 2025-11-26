# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-26 22:13:41（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0770	7.7777	0.8652	0.7580	156.6630
CNY	0.1413		1.0990	0.1223	0.1071	22.1369
HKD	0.1286	0.9099		0.1112	0.0975	20.1426
EUR	1.1558	8.1796	8.9895		0.8761	181.0714
GBP	1.3193	9.3364	10.2608	1.1414		206.6794
JPY	0.0064	0.0452	0.0496	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*