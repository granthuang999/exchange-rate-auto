# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-24 12:48:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8353	7.8340	0.8559	0.7428	159.7340
CNY	0.1463		1.1461	0.1252	0.1087	23.3690
HKD	0.1276	0.8725		0.1093	0.0948	20.3898
EUR	1.1684	7.9861	9.1529		0.8679	186.6269
GBP	1.3463	9.2021	10.5466	1.1523		215.0431
JPY	0.0063	0.0428	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*