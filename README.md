# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-01 22:12:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7815	0.8510	0.7405	146.9940
CNY	0.1405		1.0931	0.1195	0.1040	20.6496
HKD	0.1285	0.9148		0.1094	0.0952	18.8902
EUR	1.1751	8.3649	9.1439		0.8702	172.7309
GBP	1.3504	9.6131	10.5084	1.1492		198.5064
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*