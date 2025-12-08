# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-08 22:13:48（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0677	7.7801	0.8580	0.7501	155.5820
CNY	0.1415		1.1008	0.1214	0.1061	22.0131
HKD	0.1285	0.9084		0.1103	0.0964	19.9974
EUR	1.1655	8.2374	9.0677		0.8742	181.3310
GBP	1.3332	9.4223	10.3721	1.1438		207.4150
JPY	0.0064	0.0454	0.0500	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*