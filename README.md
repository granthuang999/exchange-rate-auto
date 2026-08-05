# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-05 12:56:48（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7350	7.8427	0.8666	0.7432	157.6270
CNY	0.1485		1.1645	0.1287	0.1103	23.4042
HKD	0.1275	0.8588		0.1105	0.0948	20.0986
EUR	1.1539	7.7718	9.0500		0.8576	181.8913
GBP	1.3455	9.0622	10.5526	1.1660		212.0923
JPY	0.0063	0.0427	0.0498	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*