# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-06 12:01:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8996	7.8230	0.8604	0.7479	157.4980
CNY	0.1449		1.1338	0.1247	0.1084	22.8271
HKD	0.1278	0.8820		0.1100	0.0956	20.1327
EUR	1.1623	8.0191	9.0923		0.8692	183.0521
GBP	1.3371	9.2253	10.4600	1.1504		210.5870
JPY	0.0063	0.0438	0.0497	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*