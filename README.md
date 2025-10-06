# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-06 22:12:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7821	0.8541	0.7426	149.8460
CNY	0.1405		1.0932	0.1200	0.1043	21.0502
HKD	0.1285	0.9147		0.1098	0.0954	19.2552
EUR	1.1708	8.3345	9.1115		0.8695	175.4432
GBP	1.3466	9.5859	10.4795	1.1501		201.7856
JPY	0.0067	0.0475	0.0519	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*