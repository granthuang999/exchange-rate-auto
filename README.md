# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-04 11:13:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0690	7.7820	0.8576	0.7500	155.4350
CNY	0.1415		1.1009	0.1213	0.1061	21.9883
HKD	0.1285	0.9084		0.1102	0.0964	19.9737
EUR	1.1660	8.2428	9.0742		0.8745	181.2442
GBP	1.3333	9.4253	10.3760	1.1435		207.2467
JPY	0.0064	0.0455	0.0501	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*