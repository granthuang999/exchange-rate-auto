# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-05 12:04:47（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8893	7.8187	0.8611	0.7498	157.0580
CNY	0.1452		1.1349	0.1250	0.1088	22.7974
HKD	0.1279	0.8811		0.1101	0.0959	20.0875
EUR	1.1613	8.0006	9.0799		0.8707	182.3923
GBP	1.3337	9.1882	10.4277	1.1484		209.4665
JPY	0.0064	0.0439	0.0498	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*