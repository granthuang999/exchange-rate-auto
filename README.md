# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-19 22:19:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9628	7.7970	0.8595	0.7456	157.8750
CNY	0.1436		1.1198	0.1234	0.1071	22.6741
HKD	0.1283	0.8930		0.1102	0.0956	20.2482
EUR	1.1635	8.1010	9.0716		0.8675	183.6824
GBP	1.3412	9.3385	10.4573	1.1528		211.7422
JPY	0.0063	0.0441	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*