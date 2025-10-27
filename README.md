# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-27 11:14:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1113	7.7676	0.8595	0.7504	152.9720
CNY	0.1406		1.0923	0.1209	0.1055	21.5111
HKD	0.1287	0.9155		0.1107	0.0966	19.6936
EUR	1.1635	8.2738	9.0373		0.8731	177.9779
GBP	1.3326	9.4767	10.3513	1.1454		203.8539
JPY	0.0065	0.0465	0.0508	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*