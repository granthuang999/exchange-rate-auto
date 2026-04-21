# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-21 12:42:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8147	7.8312	0.8489	0.7399	158.9660
CNY	0.1467		1.1492	0.1246	0.1086	23.3269
HKD	0.1277	0.8702		0.1084	0.0945	20.2991
EUR	1.1780	8.0277	9.2251		0.8716	187.2612
GBP	1.3515	9.2103	10.5841	1.1473		214.8480
JPY	0.0063	0.0429	0.0493	0.0053	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*