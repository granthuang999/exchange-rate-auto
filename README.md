# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-03 22:36:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8817	7.8364	0.8674	0.7571	159.5510
CNY	0.1453		1.1387	0.1260	0.1100	23.1848
HKD	0.1276	0.8782		0.1107	0.0966	20.3602
EUR	1.1529	7.9337	9.0344		0.8728	183.9417
GBP	1.3208	9.0896	10.3505	1.1457		210.7397
JPY	0.0063	0.0431	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*