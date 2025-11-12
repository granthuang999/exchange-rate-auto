# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-12 22:13:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1146	7.7707	0.8643	0.7637	154.9650
CNY	0.1406		1.0922	0.1215	0.1073	21.7813
HKD	0.1287	0.9156		0.1112	0.0983	19.9422
EUR	1.1570	8.2316	8.9907		0.8836	179.2954
GBP	1.3094	9.3160	10.1751	1.1317		202.9134
JPY	0.0065	0.0459	0.0501	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*