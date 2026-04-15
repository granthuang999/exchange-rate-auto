# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-15 22:59:45（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8196	7.8346	0.8474	0.7370	158.9780
CNY	0.1466		1.1488	0.1243	0.1081	23.3119
HKD	0.1276	0.8704		0.1082	0.0941	20.2918
EUR	1.1801	8.0477	9.2455		0.8697	187.6068
GBP	1.3569	9.2532	10.6304	1.1498		215.7096
JPY	0.0063	0.0429	0.0493	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*