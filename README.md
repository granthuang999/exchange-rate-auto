# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-08 22:12:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7817	0.8594	0.7445	152.6570
CNY	0.1405		1.0932	0.1207	0.1046	21.4451
HKD	0.1285	0.9148		0.1104	0.0957	19.6174
EUR	1.1636	8.2831	9.0548		0.8663	177.6321
GBP	1.3432	9.5615	10.4522	1.1543		205.0463
JPY	0.0066	0.0466	0.0510	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*