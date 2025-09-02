# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-02 22:12:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1415	7.8063	0.8565	0.7456	148.1620
CNY	0.1400		1.0931	0.1199	0.1044	20.7466
HKD	0.1281	0.9148		0.1097	0.0955	18.9798
EUR	1.1675	8.3380	9.1142		0.8705	172.9854
GBP	1.3412	9.5782	10.4698	1.1487		198.7151
JPY	0.0067	0.0482	0.0527	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*