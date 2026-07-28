# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-28 23:58:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7560	7.8404	0.8770	0.7515	163.6670
CNY	0.1480		1.1605	0.1298	0.1112	24.2254
HKD	0.1275	0.8617		0.1119	0.0958	20.8748
EUR	1.1403	7.7035	8.9400		0.8569	186.6214
GBP	1.3307	8.9900	10.4330	1.1670		217.7871
JPY	0.0061	0.0413	0.0479	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*