# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-29 07:18:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7255	7.8391	0.8630	0.7387	160.0380
CNY	0.1487		1.1656	0.1283	0.1098	23.7957
HKD	0.1276	0.8579		0.1101	0.0942	20.4154
EUR	1.1587	7.7932	9.0835		0.8560	185.4438
GBP	1.3537	9.1045	10.6120	1.1683		216.6482
JPY	0.0062	0.0420	0.0490	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*