# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-03 10:49:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1423	7.8088	0.8596	0.7480	148.7920
CNY	0.1400		1.0933	0.1204	0.1047	20.8325
HKD	0.1281	0.9146		0.1101	0.0958	19.0544
EUR	1.1633	8.3089	9.0842		0.8702	173.0945
GBP	1.3369	9.5485	10.4396	1.1492		198.9198
JPY	0.0067	0.0480	0.0525	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*