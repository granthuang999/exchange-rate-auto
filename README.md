# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-10 22:41:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8761	7.8239	0.8585	0.7430	157.6860
CNY	0.1454		1.1378	0.1249	0.1081	22.9325
HKD	0.1278	0.8789		0.1097	0.0950	20.1544
EUR	1.1648	8.0094	9.1135		0.8655	183.6762
GBP	1.3459	9.2545	10.5301	1.1555		212.2288
JPY	0.0063	0.0436	0.0496	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*