# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-20 11:03:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1856	7.8061	0.8595	0.7423	147.5490
CNY	0.1392		1.0864	0.1196	0.1033	20.5340
HKD	0.1281	0.9205		0.1101	0.0951	18.9018
EUR	1.1635	8.3602	9.0821		0.8636	171.6684
GBP	1.3472	9.6802	10.5161	1.1579		198.7727
JPY	0.0068	0.0487	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*