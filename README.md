# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-21 11:04:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1117	7.7839	0.8667	0.7646	157.3870
CNY	0.1406		1.0945	0.1219	0.1075	22.1307
HKD	0.1285	0.9136		0.1113	0.0982	20.2196
EUR	1.1538	8.2055	8.9811		0.8822	181.5934
GBP	1.3079	9.3012	10.1804	1.1335		205.8423
JPY	0.0064	0.0452	0.0495	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*