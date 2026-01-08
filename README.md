# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-08 11:23:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9858	7.7869	0.8558	0.7428	156.6600
CNY	0.1431		1.1147	0.1225	0.1063	22.4255
HKD	0.1284	0.8971		0.1099	0.0954	20.1184
EUR	1.1685	8.1629	9.0990		0.8680	183.0568
GBP	1.3463	9.4047	10.4832	1.1521		210.9047
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