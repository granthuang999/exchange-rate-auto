# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-02 22:13:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9875	7.7921	0.8530	0.7430	156.8660
CNY	0.1431		1.1151	0.1221	0.1063	22.4495
HKD	0.1283	0.8967		0.1095	0.0954	20.1314
EUR	1.1723	8.1917	9.1349		0.8710	183.8992
GBP	1.3459	9.4044	10.4873	1.1480		211.1252
JPY	0.0064	0.0445	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*