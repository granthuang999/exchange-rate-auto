# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-13 11:21:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9751	7.7980	0.8572	0.7420	158.6580
CNY	0.1434		1.1180	0.1229	0.1064	22.7463
HKD	0.1282	0.8945		0.1099	0.0952	20.3460
EUR	1.1666	8.1371	9.0971		0.8656	185.0887
GBP	1.3477	9.4004	10.5094	1.1553		213.8248
JPY	0.0063	0.0440	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*