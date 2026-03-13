# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-13 22:36:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8956	7.8270	0.8712	0.7533	159.2320
CNY	0.1450		1.1351	0.1263	0.1092	23.0918
HKD	0.1278	0.8810		0.1113	0.0962	20.3439
EUR	1.1478	7.9151	8.9842		0.8647	182.7732
GBP	1.3275	9.1539	10.3903	1.1565		211.3793
JPY	0.0063	0.0433	0.0492	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*