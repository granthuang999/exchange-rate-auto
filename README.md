# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-23 22:12:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1103	7.7752	0.8472	0.7397	147.6620
CNY	0.1406		1.0935	0.1192	0.1040	20.7673
HKD	0.1286	0.9145		0.1090	0.0951	18.9914
EUR	1.1804	8.3927	9.1775		0.8731	174.2941
GBP	1.3519	9.6124	10.5113	1.1453		199.6242
JPY	0.0068	0.0482	0.0527	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*