# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-20 22:12:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1105	7.7838	0.8674	0.7642	157.8000
CNY	0.1406		1.0947	0.1220	0.1075	22.1925
HKD	0.1285	0.9135		0.1114	0.0982	20.2729
EUR	1.1529	8.1975	8.9737		0.8810	181.9230
GBP	1.3086	9.3045	10.1856	1.1350		206.4904
JPY	0.0063	0.0451	0.0493	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*