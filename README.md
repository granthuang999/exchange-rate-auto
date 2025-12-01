# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-01 11:43:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0730	7.7890	0.8620	0.7559	155.4430
CNY	0.1414		1.1012	0.1219	0.1069	21.9770
HKD	0.1284	0.9081		0.1107	0.0970	19.9567
EUR	1.1601	8.2053	9.0360		0.8769	180.3283
GBP	1.3229	9.3571	10.3043	1.1404		205.6396
JPY	0.0064	0.0455	0.0501	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*