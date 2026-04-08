# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-08 23:01:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8287	7.8306	0.8548	0.7436	158.2730
CNY	0.1464		1.1467	0.1252	0.1089	23.1776
HKD	0.1277	0.8721		0.1092	0.0950	20.2121
EUR	1.1699	7.9887	9.1607		0.8699	185.1579
GBP	1.3448	9.1833	10.5307	1.1495		212.8470
JPY	0.0063	0.0431	0.0495	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*