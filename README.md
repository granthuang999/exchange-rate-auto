# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-24 22:51:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8949	7.8269	0.8630	0.7468	158.7740
CNY	0.1450		1.1352	0.1252	0.1083	23.0277
HKD	0.1278	0.8809		0.1103	0.0954	20.2857
EUR	1.1587	7.9895	9.0694		0.8654	183.9791
GBP	1.3390	9.2326	10.4806	1.1556		212.6058
JPY	0.0063	0.0434	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*