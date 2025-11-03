# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-03 22:12:41（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1205	7.7729	0.8687	0.7620	154.2560
CNY	0.1404		1.0916	0.1220	0.1070	21.6636
HKD	0.1287	0.9161		0.1118	0.0980	19.8454
EUR	1.1511	8.1967	8.9477		0.8772	177.5711
GBP	1.3123	9.3445	10.2007	1.1400		202.4357
JPY	0.0065	0.0462	0.0504	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*