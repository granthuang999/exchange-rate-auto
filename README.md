# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-22 22:13:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1123	7.7705	0.8493	0.7406	147.8850
CNY	0.1406		1.0925	0.1194	0.1041	20.7929
HKD	0.1287	0.9153		0.1093	0.0953	19.0316
EUR	1.1774	8.3743	9.1493		0.8720	174.1258
GBP	1.3503	9.6034	10.4922	1.1468		199.6827
JPY	0.0068	0.0481	0.0525	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*