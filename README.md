# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-31 22:55:02（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8946	7.8390	0.8676	0.7563	159.2750
CNY	0.1450		1.1370	0.1258	0.1097	23.1014
HKD	0.1276	0.8795		0.1107	0.0965	20.3183
EUR	1.1526	7.9467	9.0353		0.8717	183.5811
GBP	1.3222	9.1162	10.3649	1.1472		210.5976
JPY	0.0063	0.0433	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*