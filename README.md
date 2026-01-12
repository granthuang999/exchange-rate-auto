# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-12 22:18:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9725	7.7961	0.8557	0.7423	157.9220
CNY	0.1434		1.1181	0.1227	0.1065	22.6493
HKD	0.1283	0.8944		0.1098	0.0952	20.2565
EUR	1.1686	8.1483	9.1108		0.8675	184.5530
GBP	1.3472	9.3931	10.5026	1.1528		212.7469
JPY	0.0063	0.0442	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*