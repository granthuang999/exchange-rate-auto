# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-24 10:55:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1242	7.7726	0.8612	0.7507	152.8470
CNY	0.1404		1.0910	0.1209	0.1054	21.4546
HKD	0.1287	0.9166		0.1108	0.0966	19.6648
EUR	1.1612	8.2724	9.0253		0.8717	177.4814
GBP	1.3321	9.4901	10.3538	1.1472		203.6060
JPY	0.0065	0.0466	0.0509	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*