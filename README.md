# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-01 11:05:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7819	0.8518	0.7440	147.8990
CNY	0.1405		1.0932	0.1197	0.1045	20.7767
HKD	0.1285	0.9148		0.1095	0.0956	19.0055
EUR	1.1740	8.3570	9.1358		0.8734	173.6311
GBP	1.3441	9.5679	10.4595	1.1449		198.7890
JPY	0.0068	0.0481	0.0526	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*