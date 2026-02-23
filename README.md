# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-23 12:14:45（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8161	0.8458	0.7399	154.2830
CNY	0.1449		1.1322	0.1225	0.1072	22.3495
HKD	0.1279	0.8832		0.1082	0.0947	19.7391
EUR	1.1823	8.1617	9.2411		0.8748	182.4107
GBP	1.3515	9.3299	10.5637	1.1431		208.5187
JPY	0.0065	0.0447	0.0507	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*