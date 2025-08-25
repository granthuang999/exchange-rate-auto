# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-25 22:12:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1519	7.8115	0.8544	0.7403	147.3940
CNY	0.1398		1.0922	0.1195	0.1035	20.6091
HKD	0.1280	0.9156		0.1094	0.0948	18.8688
EUR	1.1704	8.3707	9.1427		0.8665	172.5117
GBP	1.3508	9.6608	10.5518	1.1541		199.1004
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