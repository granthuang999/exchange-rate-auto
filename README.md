# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-24 22:43:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8830	7.8222	0.8491	0.7416	156.0400
CNY	0.1453		1.1365	0.1234	0.1077	22.6703
HKD	0.1278	0.8799		0.1086	0.0948	19.9484
EUR	1.1777	8.1062	9.2123		0.8734	183.7711
GBP	1.3484	9.2813	10.5477	1.1450		210.4099
JPY	0.0064	0.0441	0.0501	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*