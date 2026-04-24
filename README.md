# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-24 23:01:26（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8354	7.8341	0.8540	0.7407	159.5090
CNY	0.1463		1.1461	0.1249	0.1084	23.3357
HKD	0.1276	0.8725		0.1090	0.0945	20.3609
EUR	1.1710	8.0040	9.1734		0.8673	186.7787
GBP	1.3501	9.2283	10.5766	1.1530		215.3490
JPY	0.0063	0.0429	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*