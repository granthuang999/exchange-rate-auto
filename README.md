# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-10 11:13:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1194	7.7753	0.8650	0.7605	153.9210
CNY	0.1405		1.0921	0.1215	0.1068	21.6199
HKD	0.1286	0.9156		0.1112	0.0978	19.7961
EUR	1.1561	8.2305	8.9888		0.8792	177.9434
GBP	1.3149	9.3615	10.2239	1.1374		202.3945
JPY	0.0065	0.0463	0.0505	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*