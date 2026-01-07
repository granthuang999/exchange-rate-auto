# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-07 11:22:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9844	7.7878	0.8545	0.7400	156.6100
CNY	0.1432		1.1150	0.1223	0.1060	22.4228
HKD	0.1284	0.8968		0.1097	0.0950	20.1097
EUR	1.1703	8.1737	9.1139		0.8660	183.2768
GBP	1.3514	9.4384	10.5241	1.1547		211.6351
JPY	0.0064	0.0446	0.0497	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*