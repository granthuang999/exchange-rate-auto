# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-09 10:55:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1273	7.7798	0.8584	0.7453	152.4310
CNY	0.1403		1.0915	0.1204	0.1046	21.3869
HKD	0.1285	0.9161		0.1103	0.0958	19.5932
EUR	1.1650	8.3030	9.0631		0.8682	177.5757
GBP	1.3417	9.5630	10.4385	1.1518		204.5230
JPY	0.0066	0.0468	0.0510	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*