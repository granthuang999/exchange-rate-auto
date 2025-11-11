# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-11 22:12:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1160	7.7721	0.8618	0.7592	153.8250
CNY	0.1405		1.0922	0.1211	0.1067	21.6168
HKD	0.1287	0.9156		0.1109	0.0977	19.7919
EUR	1.1604	8.2571	9.0184		0.8809	178.4927
GBP	1.3172	9.3730	10.2372	1.1351		202.6146
JPY	0.0065	0.0463	0.0505	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*