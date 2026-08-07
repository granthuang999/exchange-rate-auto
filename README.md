# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-07 22:44:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7343	7.8451	0.8654	0.7413	157.8490
CNY	0.1485		1.1649	0.1285	0.1101	23.4396
HKD	0.1275	0.8584		0.1103	0.0945	20.1207
EUR	1.1555	7.7817	9.0653		0.8566	182.4000
GBP	1.3490	9.0844	10.5829	1.1674		212.9354
JPY	0.0063	0.0427	0.0497	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*