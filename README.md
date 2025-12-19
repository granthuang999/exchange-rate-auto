# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-19 11:17:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0401	7.7804	0.8527	0.7473	155.8440
CNY	0.1420		1.1052	0.1211	0.1061	22.1366
HKD	0.1285	0.9049		0.1096	0.0960	20.0303
EUR	1.1727	8.2562	9.1244		0.8764	182.7653
GBP	1.3382	9.4207	10.4113	1.1410		208.5428
JPY	0.0064	0.0452	0.0499	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*