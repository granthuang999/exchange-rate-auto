# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-10 12:40:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8299	7.8344	0.8549	0.7449	159.1900
CNY	0.1464		1.1471	0.1252	0.1091	23.3078
HKD	0.1276	0.8718		0.1091	0.0951	20.3194
EUR	1.1697	7.9891	9.1641		0.8713	186.2089
GBP	1.3425	9.1689	10.5174	1.1477		213.7065
JPY	0.0063	0.0429	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*