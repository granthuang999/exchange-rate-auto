# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-09 22:45:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9215	7.8140	0.8391	0.7331	155.5950
CNY	0.1445		1.1289	0.1212	0.1059	22.4800
HKD	0.1280	0.8858		0.1074	0.0938	19.9123
EUR	1.1918	8.2487	9.3124		0.8737	185.4308
GBP	1.3641	9.4414	10.6588	1.1446		212.2425
JPY	0.0064	0.0445	0.0502	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*