# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-21 23:04:25（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8202	7.8300	0.8506	0.7402	159.3170
CNY	0.1466		1.1481	0.1247	0.1085	23.3596
HKD	0.1277	0.8710		0.1086	0.0945	20.3470
EUR	1.1756	8.0181	9.2053		0.8702	187.2996
GBP	1.3510	9.2140	10.5782	1.1491		215.2351
JPY	0.0063	0.0428	0.0491	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*