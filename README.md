# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-16 23:19:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8211	7.8246	0.8487	0.7390	159.1940
CNY	0.1466		1.1471	0.1244	0.1083	23.3385
HKD	0.1278	0.8718		0.1085	0.0944	20.3453
EUR	1.1783	8.0371	9.2195		0.8707	187.5739
GBP	1.3532	9.2302	10.5881	1.1484		215.4181
JPY	0.0063	0.0428	0.0492	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*