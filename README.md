# 汇率数据自动更新（美元基准）

**更新时间**：2026-05-01 22:47:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8268	7.8347	0.8492	0.7334	156.6440
CNY	0.1465		1.1476	0.1244	0.1074	22.9455
HKD	0.1276	0.8714		0.1084	0.0936	19.9936
EUR	1.1776	8.0391	9.2260		0.8636	184.4607
GBP	1.3635	9.3084	10.6827	1.1579		213.5860
JPY	0.0064	0.0436	0.0500	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*