# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-29 13:12:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7695	7.8424	0.8768	0.7519	163.4270
CNY	0.1477		1.1585	0.1295	0.1111	24.1417
HKD	0.1275	0.8632		0.1118	0.0959	20.8389
EUR	1.1405	7.7207	8.9443		0.8576	186.3903
GBP	1.3300	9.0032	10.4301	1.1661		217.3520
JPY	0.0061	0.0414	0.0480	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*