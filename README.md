# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-31 22:12:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1164	7.7705	0.8667	0.7626	153.9750
CNY	0.1405		1.0919	0.1218	0.1072	21.6366
HKD	0.1287	0.9158		0.1115	0.0981	19.8153
EUR	1.1538	8.2109	8.9656		0.8799	177.6566
GBP	1.3113	9.3318	10.1895	1.1365		201.9079
JPY	0.0065	0.0462	0.0505	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*