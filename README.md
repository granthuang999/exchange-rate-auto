# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-09 23:13:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8351	7.8345	0.8560	0.7459	159.2690
CNY	0.1463		1.1462	0.1252	0.1091	23.3016
HKD	0.1276	0.8724		0.1093	0.0952	20.3292
EUR	1.1682	7.9849	9.1525		0.8714	186.0619
GBP	1.3407	9.1636	10.5034	1.1476		213.5259
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