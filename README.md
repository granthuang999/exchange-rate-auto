# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-14 11:29:48（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9754	7.7980	0.8585	0.7440	159.2000
CNY	0.1434		1.1179	0.1231	0.1067	22.8231
HKD	0.1282	0.8945		0.1101	0.0954	20.4155
EUR	1.1648	8.1251	9.0833		0.8666	185.4397
GBP	1.3441	9.3755	10.4812	1.1539		213.9785
JPY	0.0063	0.0438	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*