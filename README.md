# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-03 12:07:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8815	7.8170	0.8550	0.7461	157.2350
CNY	0.1453		1.1359	0.1242	0.1084	22.8489
HKD	0.1279	0.8803		0.1094	0.0954	20.1145
EUR	1.1696	8.0485	9.1427		0.8726	183.9006
GBP	1.3403	9.2233	10.4771	1.1460		210.7425
JPY	0.0064	0.0438	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*