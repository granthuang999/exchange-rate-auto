# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-04 14:45:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7112	7.8399	0.8597	0.7384	156.1120
CNY	0.1490		1.1682	0.1281	0.1100	23.2614
HKD	0.1276	0.8560		0.1097	0.0942	19.9125
EUR	1.1632	7.8064	9.1193		0.8589	181.5889
GBP	1.3543	9.0888	10.6174	1.1643		211.4193
JPY	0.0064	0.0430	0.0502	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*