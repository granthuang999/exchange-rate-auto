# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-13 12:01:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7436	7.8466	0.8676	0.7413	159.4320
CNY	0.1483		1.1636	0.1287	0.1099	23.6420
HKD	0.1274	0.8594		0.1106	0.0945	20.3186
EUR	1.1526	7.7727	9.0440		0.8544	183.7621
GBP	1.3490	9.0970	10.5849	1.1704		215.0708
JPY	0.0063	0.0423	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*