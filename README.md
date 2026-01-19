# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-19 11:42:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9627	7.7955	0.8602	0.7469	157.8900
CNY	0.1436		1.1196	0.1235	0.1073	22.6765
HKD	0.1283	0.8932		0.1103	0.0958	20.2540
EUR	1.1625	8.0943	9.0624		0.8683	183.5503
GBP	1.3389	9.3221	10.4371	1.1517		211.3938
JPY	0.0063	0.0441	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*