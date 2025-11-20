# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-20 11:04:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1147	7.7854	0.8676	0.7660	157.3350
CNY	0.1406		1.0943	0.1219	0.1077	22.1141
HKD	0.1284	0.9139		0.1114	0.0984	20.2090
EUR	1.1526	8.2004	8.9735		0.8829	181.3451
GBP	1.3055	9.2881	10.1637	1.1326		205.3982
JPY	0.0064	0.0452	0.0495	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*