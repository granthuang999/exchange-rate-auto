# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-05 11:47:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9821	7.7891	0.8563	0.7453	157.1810
CNY	0.1432		1.1156	0.1226	0.1067	22.5120
HKD	0.1284	0.8964		0.1099	0.0957	20.1796
EUR	1.1678	8.1538	9.0962		0.8704	183.5583
GBP	1.3417	9.3682	10.4510	1.1489		210.8963
JPY	0.0064	0.0444	0.0496	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*