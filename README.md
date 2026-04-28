# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-28 13:23:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8292	7.8351	0.8535	0.7391	159.0670
CNY	0.1464		1.1473	0.1250	0.1082	23.2922
HKD	0.1276	0.8716		0.1089	0.0943	20.3018
EUR	1.1716	8.0014	9.1800		0.8660	186.3702
GBP	1.3530	9.2399	10.6009	1.1548		215.2172
JPY	0.0063	0.0429	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*