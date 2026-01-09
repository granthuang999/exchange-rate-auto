# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-09 11:23:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9792	7.7937	0.8575	0.7443	157.1960
CNY	0.1433		1.1167	0.1229	0.1066	22.5235
HKD	0.1283	0.8955		0.1100	0.0955	20.1696
EUR	1.1662	8.1390	9.0889		0.8680	183.3190
GBP	1.3435	9.3769	10.4712	1.1521		211.1998
JPY	0.0064	0.0444	0.0496	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*