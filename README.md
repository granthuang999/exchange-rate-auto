# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-06 22:13:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1178	7.7750	0.8667	0.7633	153.5190
CNY	0.1405		1.0923	0.1218	0.1072	21.5683
HKD	0.1286	0.9155		0.1115	0.0982	19.7452
EUR	1.1538	8.2125	8.9708		0.8807	177.1305
GBP	1.3101	9.3250	10.1860	1.1355		201.1254
JPY	0.0065	0.0464	0.0506	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*