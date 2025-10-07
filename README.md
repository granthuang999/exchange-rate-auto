# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-07 22:12:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7827	0.8574	0.7451	150.9800
CNY	0.1405		1.0933	0.1204	0.1047	21.2095
HKD	0.1285	0.9147		0.1102	0.0957	19.3994
EUR	1.1663	8.3024	9.0771		0.8690	176.0905
GBP	1.3421	9.5538	10.4452	1.1507		202.6305
JPY	0.0066	0.0471	0.0515	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*