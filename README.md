# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-21 11:02:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1718	7.8083	0.8583	0.7434	147.3660
CNY	0.1394		1.0888	0.1197	0.1037	20.5480
HKD	0.1281	0.9185		0.1099	0.0952	18.8730
EUR	1.1651	8.3558	9.0974		0.8661	171.6952
GBP	1.3452	9.6473	10.5035	1.1546		198.2324
JPY	0.0068	0.0487	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*