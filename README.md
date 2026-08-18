# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-18 22:23:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7305	7.8434	0.8627	0.7381	159.4650
CNY	0.1486		1.1654	0.1282	0.1097	23.6929
HKD	0.1275	0.8581		0.1100	0.0941	20.3311
EUR	1.1592	7.8017	9.0917		0.8556	184.8441
GBP	1.3548	9.1187	10.6265	1.1688		216.0480
JPY	0.0063	0.0422	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*