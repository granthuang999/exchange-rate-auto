# 汇率数据自动更新（美元基准）

**更新时间**：2026-05-04 13:26:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8271	7.8330	0.8523	0.7359	156.7670
CNY	0.1465		1.1473	0.1248	0.1078	22.9625
HKD	0.1277	0.8716		0.1088	0.0939	20.0137
EUR	1.1733	8.0102	9.1904		0.8634	183.9341
GBP	1.3589	9.2772	10.6441	1.1582		213.0276
JPY	0.0064	0.0435	0.0500	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*