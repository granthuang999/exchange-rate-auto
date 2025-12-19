# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-19 22:13:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0405	7.7808	0.8523	0.7474	157.0170
CNY	0.1420		1.1051	0.1211	0.1062	22.3020
HKD	0.1285	0.9049		0.1095	0.0961	20.1801
EUR	1.1733	8.2606	9.1292		0.8769	184.2274
GBP	1.3380	9.4200	10.4105	1.1404		210.0843
JPY	0.0064	0.0448	0.0496	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*