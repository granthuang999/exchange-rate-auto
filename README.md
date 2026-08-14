# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-14 11:56:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7433	7.8466	0.8665	0.7410	159.3830
CNY	0.1483		1.1636	0.1285	0.1099	23.6358
HKD	0.1274	0.8594		0.1104	0.0944	20.3124
EUR	1.1541	7.7822	9.0555		0.8552	183.9388
GBP	1.3495	9.1003	10.5892	1.1694		215.0918
JPY	0.0063	0.0423	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*