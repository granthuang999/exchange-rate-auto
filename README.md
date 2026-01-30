# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-30 12:01:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9487	7.8072	0.8387	0.7270	153.9450
CNY	0.1439		1.1235	0.1207	0.1046	22.1545
HKD	0.1281	0.8900		0.1074	0.0931	19.7183
EUR	1.1923	8.2851	9.3087		0.8668	183.5519
GBP	1.3755	9.5580	10.7389	1.1536		211.7538
JPY	0.0065	0.0451	0.0507	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*