# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-06 12:57:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7483	7.8435	0.8657	0.7429	157.7320
CNY	0.1482		1.1623	0.1283	0.1101	23.3736
HKD	0.1275	0.8604		0.1104	0.0947	20.1099
EUR	1.1551	7.7952	9.0603		0.8581	182.2017
GBP	1.3461	9.0837	10.5579	1.1653		212.3193
JPY	0.0063	0.0428	0.0497	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*