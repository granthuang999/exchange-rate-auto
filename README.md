# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-09 12:08:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9197	7.8128	0.8675	0.7516	158.8260
CNY	0.1445		1.1291	0.1254	0.1086	22.9527
HKD	0.1280	0.8857		0.1110	0.0962	20.3289
EUR	1.1527	7.9766	9.0061		0.8664	183.0847
GBP	1.3305	9.2066	10.3949	1.1542		211.3172
JPY	0.0063	0.0436	0.0492	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*