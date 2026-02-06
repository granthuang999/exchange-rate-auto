# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-06 22:35:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9383	7.8126	0.8458	0.7353	156.8490
CNY	0.1441		1.1260	0.1219	0.1060	22.6063
HKD	0.1280	0.8881		0.1083	0.0941	20.0764
EUR	1.1823	8.2032	9.2369		0.8694	185.4445
GBP	1.3600	9.4360	10.6251	1.1503		213.3129
JPY	0.0064	0.0442	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*