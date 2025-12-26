# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-26 22:13:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0063	7.7711	0.8477	0.7397	156.2980
CNY	0.1427		1.1092	0.1210	0.1056	22.3082
HKD	0.1287	0.9016		0.1091	0.0952	20.1127
EUR	1.1797	8.2651	9.1673		0.8726	184.3789
GBP	1.3519	9.4718	10.5057	1.1460		211.2992
JPY	0.0064	0.0448	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*