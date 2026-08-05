# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-05 23:54:30（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7370	7.8435	0.8659	0.7430	157.6160
CNY	0.1484		1.1642	0.1285	0.1103	23.3956
HKD	0.1275	0.8589		0.1104	0.0947	20.0951
EUR	1.1549	7.7803	9.0582		0.8581	182.0256
GBP	1.3459	9.0673	10.5565	1.1654		212.1346
JPY	0.0063	0.0427	0.0498	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*