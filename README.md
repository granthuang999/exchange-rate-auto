# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-29 10:57:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1270	7.7895	0.8572	0.7405	146.8990
CNY	0.1403		1.0930	0.1203	0.1039	20.6116
HKD	0.1284	0.9149		0.1100	0.0951	18.8586
EUR	1.1666	8.3143	9.0871		0.8639	171.3707
GBP	1.3504	9.6246	10.5192	1.1576		198.3781
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