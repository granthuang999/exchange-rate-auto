# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-26 11:08:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0840	7.7768	0.8630	0.7580	155.7590
CNY	0.1412		1.0978	0.1218	0.1070	21.9874
HKD	0.1286	0.9109		0.1110	0.0975	20.0287
EUR	1.1587	8.2086	9.0114		0.8783	180.4855
GBP	1.3193	9.3456	10.2596	1.1385		205.4868
JPY	0.0064	0.0455	0.0499	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*