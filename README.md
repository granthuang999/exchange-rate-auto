# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-01 22:11:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1370	7.7958	0.8536	0.7385	147.2260
CNY	0.1401		1.0923	0.1196	0.1035	20.6286
HKD	0.1283	0.9155		0.1095	0.0947	18.8853
EUR	1.1715	8.3611	9.1328		0.8652	172.4766
GBP	1.3541	9.6642	10.5563	1.1559		199.3582
JPY	0.0068	0.0485	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*