# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-26 22:56:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9083	7.8250	0.8659	0.7484	159.5550
CNY	0.1448		1.1327	0.1253	0.1083	23.0961
HKD	0.1278	0.8828		0.1107	0.0956	20.3904
EUR	1.1549	7.9782	9.0368		0.8643	184.2649
GBP	1.3362	9.2308	10.4556	1.1570		213.1948
JPY	0.0063	0.0433	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*