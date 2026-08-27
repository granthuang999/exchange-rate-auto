# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-28 07:23:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7108	7.8381	0.8579	0.7355	159.3540
CNY	0.1490		1.1680	0.1278	0.1096	23.7459
HKD	0.1276	0.8562		0.1095	0.0938	20.3307
EUR	1.1656	7.8224	9.1364		0.8573	185.7489
GBP	1.3596	9.1241	10.6568	1.1664		216.6608
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