# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-16 12:45:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8168	7.8305	0.8465	0.7365	158.7060
CNY	0.1467		1.1487	0.1242	0.1080	23.2816
HKD	0.1277	0.8705		0.1081	0.0941	20.2677
EUR	1.1813	8.0529	9.2504		0.8701	187.4849
GBP	1.3578	9.2557	10.6320	1.1494		215.4868
JPY	0.0063	0.0430	0.0493	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*