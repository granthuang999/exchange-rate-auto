# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-16 12:15:13（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8143	0.8424	0.7330	153.0450
CNY	0.1449		1.1320	0.1220	0.1062	22.1702
HKD	0.1280	0.8834		0.1078	0.0938	19.5852
EUR	1.1871	8.1947	9.2762		0.8701	181.6774
GBP	1.3643	9.4177	10.6607	1.1492		208.7926
JPY	0.0065	0.0451	0.0511	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*