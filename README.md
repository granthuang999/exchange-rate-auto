# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-06 11:22:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9813	7.7854	0.8518	0.7378	156.3710
CNY	0.1432		1.1152	0.1220	0.1057	22.3986
HKD	0.1284	0.8967		0.1094	0.0948	20.0852
EUR	1.1740	8.1959	9.1399		0.8662	183.5771
GBP	1.3554	9.4623	10.5522	1.1545		211.9423
JPY	0.0064	0.0446	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*