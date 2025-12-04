# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-04 22:14:14（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0714	7.7831	0.8567	0.7488	154.7150
CNY	0.1414		1.1006	0.1211	0.1059	21.8790
HKD	0.1285	0.9086		0.1101	0.0962	19.8783
EUR	1.1673	8.2542	9.0850		0.8741	180.5941
GBP	1.3355	9.4436	10.3941	1.1441		206.6173
JPY	0.0065	0.0457	0.0503	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*