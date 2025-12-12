# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-12 22:13:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0541	7.7852	0.8527	0.7483	156.0560
CNY	0.1418		1.1036	0.1209	0.1061	22.1227
HKD	0.1284	0.9061		0.1095	0.0961	20.0452
EUR	1.1727	8.2727	9.1301		0.8776	183.0140
GBP	1.3364	9.4268	10.4038	1.1395		208.5474
JPY	0.0064	0.0452	0.0499	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*