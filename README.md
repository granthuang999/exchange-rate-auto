# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-28 10:57:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1494	7.7916	0.8580	0.7399	147.2440
CNY	0.1399		1.0898	0.1200	0.1035	20.5953
HKD	0.1283	0.9176		0.1101	0.0950	18.8978
EUR	1.1655	8.3326	9.0811		0.8624	171.6131
GBP	1.3515	9.6627	10.5306	1.1596		199.0053
JPY	0.0068	0.0486	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*