# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-19 22:12:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1787	7.7999	0.8564	0.7399	147.5820
CNY	0.1393		1.0865	0.1193	0.1031	20.5583
HKD	0.1282	0.9204		0.1098	0.0949	18.9210
EUR	1.1677	8.3824	9.1078		0.8640	172.3284
GBP	1.3515	9.7023	10.5418	1.1575		199.4621
JPY	0.0068	0.0486	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*