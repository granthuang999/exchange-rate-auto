# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-03 13:33:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7519	7.8413	0.8667	0.7422	156.4100
CNY	0.1481		1.1613	0.1284	0.1099	23.1653
HKD	0.1275	0.8611		0.1105	0.0947	19.9469
EUR	1.1538	7.7904	9.0473		0.8564	180.4661
GBP	1.3473	9.0971	10.5649	1.1677		210.7383
JPY	0.0064	0.0432	0.0501	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*