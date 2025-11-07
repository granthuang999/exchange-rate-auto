# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-07 11:05:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1215	7.7750	0.8664	0.7622	153.1650
CNY	0.1404		1.0918	0.1217	0.1070	21.5074
HKD	0.1286	0.9159		0.1114	0.0980	19.6997
EUR	1.1542	8.2196	8.9739		0.8797	176.7832
GBP	1.3120	9.3433	10.2007	1.1367		200.9512
JPY	0.0065	0.0465	0.0508	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*