# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-04 22:13:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1249	7.7740	0.8705	0.7660	153.4360
CNY	0.1404		1.0911	0.1222	0.1075	21.5352
HKD	0.1286	0.9165		0.1120	0.0985	19.7371
EUR	1.1488	8.1848	8.9305		0.8800	176.2619
GBP	1.3055	9.3014	10.1488	1.1364		200.3081
JPY	0.0065	0.0464	0.0507	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*