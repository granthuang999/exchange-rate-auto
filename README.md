# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-26 11:04:13（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1547	7.8104	0.8595	0.7429	147.5850
CNY	0.1398		1.0916	0.1201	0.1038	20.6277
HKD	0.1280	0.9160		0.1100	0.0951	18.8960
EUR	1.1635	8.3243	9.0871		0.8643	171.7103
GBP	1.3461	9.6308	10.5134	1.1570		198.6607
JPY	0.0068	0.0485	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*