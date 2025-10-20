# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-20 22:11:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1208	7.7694	0.8580	0.7459	150.6870
CNY	0.1404		1.0911	0.1205	0.1047	21.1615
HKD	0.1287	0.9165		0.1104	0.0960	19.3949
EUR	1.1655	8.2993	9.0552		0.8693	175.6259
GBP	1.3407	9.5466	10.4161	1.1503		202.0204
JPY	0.0066	0.0473	0.0516	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*