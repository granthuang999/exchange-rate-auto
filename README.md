# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-17 10:56:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1230	7.7673	0.8541	0.7439	150.2060
CNY	0.1404		1.0905	0.1199	0.1044	21.0875
HKD	0.1287	0.9170		0.1100	0.0958	19.3383
EUR	1.1708	8.3398	9.0941		0.8710	175.8647
GBP	1.3443	9.5752	10.4413	1.1481		201.9169
JPY	0.0067	0.0474	0.0517	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*