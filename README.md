# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-20 11:26:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9601	7.7969	0.8577	0.7442	157.9320
CNY	0.1437		1.1202	0.1232	0.1069	22.6911
HKD	0.1283	0.8927		0.1100	0.0954	20.2557
EUR	1.1659	8.1148	9.0905		0.8677	184.1343
GBP	1.3437	9.3525	10.4769	1.1525		212.2171
JPY	0.0063	0.0441	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*