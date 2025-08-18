# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-18 17:51:28（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP
USD		7.1777	7.8225	0.8564	0.7383
CNY	0.1393		1.0898	0.1193	0.1029
HKD	0.1278	0.9176		0.1095	0.0944
EUR	1.1677	8.3812	9.1342		0.8621
GBP	1.3545	9.7219	10.5953	1.1600	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*