# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-29 23:51:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8370	7.8365	0.8541	0.7408	160.1850
CNY	0.1463		1.1462	0.1249	0.1084	23.4291
HKD	0.1276	0.8725		0.1090	0.0945	20.4409
EUR	1.1708	8.0049	9.1752		0.8673	187.5483
GBP	1.3499	9.2292	10.5784	1.1529		216.2325
JPY	0.0062	0.0427	0.0489	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*