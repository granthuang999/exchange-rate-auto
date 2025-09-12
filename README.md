# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-12 22:11:26（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1225	7.7832	0.8531	0.7375	147.6320
CNY	0.1404		1.0928	0.1198	0.1035	20.7276
HKD	0.1285	0.9151		0.1096	0.0948	18.9680
EUR	1.1722	8.3490	9.1234		0.8645	173.0536
GBP	1.3559	9.6576	10.5535	1.1567		200.1790
JPY	0.0068	0.0482	0.0527	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*