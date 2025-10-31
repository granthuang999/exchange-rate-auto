# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-31 11:05:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1089	7.7677	0.8641	0.7603	153.8950
CNY	0.1407		1.0927	0.1216	0.1070	21.6482
HKD	0.1287	0.9152		0.1112	0.0979	19.8122
EUR	1.1573	8.2269	8.9894		0.8799	178.0986
GBP	1.3153	9.3501	10.2166	1.1365		202.4135
JPY	0.0065	0.0462	0.0505	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*