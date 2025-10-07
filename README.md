# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-07 10:52:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7824	0.8542	0.7420	150.4980
CNY	0.1405		1.0933	0.1200	0.1042	21.1418
HKD	0.1285	0.9147		0.1098	0.0953	19.3383
EUR	1.1707	8.3335	9.1107		0.8686	176.1859
GBP	1.3477	9.5937	10.4884	1.1512		202.8275
JPY	0.0066	0.0473	0.0517	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*