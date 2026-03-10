# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-10 12:00:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8863	7.8226	0.8613	0.7454	157.8910
CNY	0.1452		1.1360	0.1251	0.1082	22.9283
HKD	0.1278	0.8803		0.1101	0.0953	20.1840
EUR	1.1610	7.9952	9.0823		0.8654	183.3171
GBP	1.3416	9.2384	10.4945	1.1555		211.8205
JPY	0.0063	0.0436	0.0495	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*