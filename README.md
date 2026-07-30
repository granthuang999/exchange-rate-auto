# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-30 23:45:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7412	7.8429	0.8676	0.7430	159.3170
CNY	0.1483		1.1634	0.1287	0.1102	23.6333
HKD	0.1275	0.8595		0.1106	0.0947	20.3135
EUR	1.1526	7.7699	9.0398		0.8564	183.6296
GBP	1.3459	9.0729	10.5557	1.1677		214.4240
JPY	0.0063	0.0423	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*