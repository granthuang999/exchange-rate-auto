# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-18 12:15:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8796	7.8380	0.8665	0.7486	158.8660
CNY	0.1454		1.1393	0.1260	0.1088	23.0923
HKD	0.1276	0.8777		0.1106	0.0955	20.2687
EUR	1.1541	7.9395	9.0456		0.8639	183.3422
GBP	1.3358	9.1900	10.4702	1.1575		212.2175
JPY	0.0063	0.0433	0.0493	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*