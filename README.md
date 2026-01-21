# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-21 22:22:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9638	7.7972	0.8532	0.7450	158.0260
CNY	0.1436		1.1197	0.1225	0.1070	22.6925
HKD	0.1283	0.8931		0.1094	0.0955	20.2670
EUR	1.1721	8.1620	9.1388		0.8732	185.2157
GBP	1.3423	9.3474	10.4660	1.1452		212.1154
JPY	0.0063	0.0441	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*