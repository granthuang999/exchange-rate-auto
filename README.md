# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-13 11:08:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1073	7.7701	0.8625	0.7618	154.6550
CNY	0.1407		1.0933	0.1214	0.1072	21.7600
HKD	0.1287	0.9147		0.1110	0.0980	19.9039
EUR	1.1594	8.2403	9.0088		0.8832	179.3101
GBP	1.3127	9.3296	10.1997	1.1322		203.0126
JPY	0.0065	0.0460	0.0502	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*