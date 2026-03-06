# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-06 22:30:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9065	7.8185	0.8649	0.7496	157.9360
CNY	0.1448		1.1320	0.1252	0.1085	22.8677
HKD	0.1279	0.8834		0.1106	0.0959	20.2003
EUR	1.1562	7.9853	9.0398		0.8667	182.6061
GBP	1.3340	9.2136	10.4302	1.1538		210.6937
JPY	0.0063	0.0437	0.0495	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*