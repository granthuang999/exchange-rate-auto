# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-05 22:13:21（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0699	7.7854	0.8579	0.7489	155.1580
CNY	0.1414		1.1012	0.1213	0.1059	21.9463
HKD	0.1284	0.9081		0.1102	0.0962	19.9294
EUR	1.1656	8.2409	9.0750		0.8729	180.8579
GBP	1.3353	9.4404	10.3958	1.1455		207.1812
JPY	0.0064	0.0456	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*