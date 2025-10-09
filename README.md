# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-09 22:12:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1213	7.7804	0.8623	0.7491	152.9850
CNY	0.1404		1.0926	0.1211	0.1052	21.4827
HKD	0.1285	0.9153		0.1108	0.0963	19.6629
EUR	1.1597	8.2585	9.0228		0.8687	177.4151
GBP	1.3349	9.5065	10.3863	1.1511		204.2251
JPY	0.0065	0.0465	0.0509	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*