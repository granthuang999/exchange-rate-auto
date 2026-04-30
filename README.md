# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-30 23:43:32（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8272	7.8334	0.8521	0.7362	156.6130
CNY	0.1465		1.1474	0.1248	0.1078	22.9396
HKD	0.1277	0.8716		0.1088	0.0940	19.9930
EUR	1.1736	8.0122	9.1931		0.8640	183.7965
GBP	1.3583	9.2736	10.6403	1.1574		212.7316
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