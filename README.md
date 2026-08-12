# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-12 22:50:14（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7302	7.8469	0.8661	0.7401	159.2230
CNY	0.1486		1.1659	0.1287	0.1100	23.6580
HKD	0.1274	0.8577		0.1104	0.0943	20.2912
EUR	1.1546	7.7707	9.0600		0.8545	183.8390
GBP	1.3512	9.0936	10.6025	1.1702		215.1371
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*