# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-28 22:12:56（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1006	7.7697	0.8583	0.7540	152.0970
CNY	0.1408		1.0942	0.1209	0.1062	21.4203
HKD	0.1287	0.9139		0.1105	0.0970	19.5757
EUR	1.1651	8.2729	9.0524		0.8785	177.2073
GBP	1.3263	9.4172	10.3046	1.1383		201.7202
JPY	0.0066	0.0467	0.0511	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*