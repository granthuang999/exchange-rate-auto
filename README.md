# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-25 22:52:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9009	7.8172	0.8628	0.7471	159.0270
CNY	0.1449		1.1328	0.1250	0.1083	23.0444
HKD	0.1279	0.8828		0.1104	0.0956	20.3432
EUR	1.1590	7.9983	9.0603		0.8659	184.3150
GBP	1.3385	9.2369	10.4634	1.1549		212.8591
JPY	0.0063	0.0434	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*