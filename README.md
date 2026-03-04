# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-04 22:32:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8964	7.8153	0.8593	0.7477	157.3080
CNY	0.1450		1.1332	0.1246	0.1084	22.8102
HKD	0.1280	0.8824		0.1100	0.0957	20.1282
EUR	1.1637	8.0256	9.0950		0.8701	183.0653
GBP	1.3374	9.2235	10.4525	1.1493		210.3892
JPY	0.0064	0.0438	0.0497	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*