# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-28 22:12:21（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1303	7.7950	0.8555	0.7394	147.0080
CNY	0.1402		1.0932	0.1200	0.1037	20.6174
HKD	0.1283	0.9147		0.1097	0.0949	18.8593
EUR	1.1689	8.3347	9.1116		0.8643	171.8387
GBP	1.3524	9.6434	10.5423	1.1570		198.8207
JPY	0.0068	0.0485	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*