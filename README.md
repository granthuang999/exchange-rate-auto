# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-06 22:40:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8819	7.8364	0.8646	0.7544	159.4680
CNY	0.1453		1.1387	0.1256	0.1096	23.1721
HKD	0.1276	0.8782		0.1103	0.0963	20.3497
EUR	1.1566	7.9596	9.0636		0.8725	184.4414
GBP	1.3256	9.1223	10.3876	1.1461		211.3839
JPY	0.0063	0.0432	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*