# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-11 22:11:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1183	7.7888	0.8519	0.7377	147.2230
CNY	0.1405		1.0942	0.1197	0.1036	20.6823
HKD	0.1284	0.9139		0.1094	0.0947	18.9019
EUR	1.1738	8.3558	9.1429		0.8659	172.8172
GBP	1.3556	9.6493	10.5582	1.1548		199.5703
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*