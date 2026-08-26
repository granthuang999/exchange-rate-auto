# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-26 22:35:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7110	7.8389	0.8585	0.7358	159.3980
CNY	0.1490		1.1681	0.1279	0.1096	23.7518
HKD	0.1276	0.8561		0.1095	0.0939	20.3342
EUR	1.1648	7.8171	9.1309		0.8571	185.6704
GBP	1.3591	9.1207	10.6536	1.1668		216.6322
JPY	0.0063	0.0421	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*