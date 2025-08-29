# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-29 22:11:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1303	7.7937	0.8559	0.7421	147.0010
CNY	0.1402		1.0930	0.1200	0.1041	20.6164
HKD	0.1283	0.9149		0.1098	0.0952	18.8615
EUR	1.1684	8.3308	9.1059		0.8670	171.7502
GBP	1.3475	9.6083	10.5022	1.1533		198.0879
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