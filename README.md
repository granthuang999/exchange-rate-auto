# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-11 22:50:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7329	7.8464	0.8663	0.7404	159.2440
CNY	0.1485		1.1654	0.1287	0.1100	23.6516
HKD	0.1274	0.8581		0.1104	0.0944	20.2952
EUR	1.1543	7.7720	9.0574		0.8547	183.8208
GBP	1.3506	9.0936	10.5975	1.1700		215.0783
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*