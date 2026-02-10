# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-10 12:25:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9103	7.8164	0.8395	0.7309	155.2960
CNY	0.1447		1.1311	0.1215	0.1058	22.4731
HKD	0.1279	0.8841		0.1074	0.0935	19.8680
EUR	1.1912	8.2314	9.3108		0.8706	184.9863
GBP	1.3682	9.4545	10.6942	1.1486		212.4723
JPY	0.0064	0.0445	0.0503	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*