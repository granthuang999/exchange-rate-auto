# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-13 12:12:26（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9057	7.8157	0.8424	0.7344	152.8870
CNY	0.1448		1.1318	0.1220	0.1063	22.1392
HKD	0.1279	0.8836		0.1078	0.0940	19.5615
EUR	1.1871	8.1976	9.2779		0.8718	181.4898
GBP	1.3617	9.4032	10.6423	1.1471		208.1795
JPY	0.0065	0.0452	0.0511	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*