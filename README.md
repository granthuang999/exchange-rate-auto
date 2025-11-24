# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-24 22:13:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1027	7.7820	0.8664	0.7634	156.9790
CNY	0.1408		1.0956	0.1220	0.1075	22.1013
HKD	0.1285	0.9127		0.1113	0.0981	20.1721
EUR	1.1542	8.1979	8.9820		0.8811	181.1854
GBP	1.3099	9.3040	10.1939	1.1349		205.6314
JPY	0.0064	0.0452	0.0496	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*