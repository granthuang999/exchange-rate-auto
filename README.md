# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-25 22:34:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7190	7.8384	0.8567	0.7334	159.2490
CNY	0.1488		1.1666	0.1275	0.1092	23.7013
HKD	0.1276	0.8572		0.1093	0.0936	20.3165
EUR	1.1673	7.8429	9.1495		0.8561	185.8865
GBP	1.3635	9.1614	10.6878	1.1681		217.1380
JPY	0.0063	0.0422	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*