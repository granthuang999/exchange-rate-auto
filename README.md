# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-30 22:12:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7806	0.8513	0.7437	147.7470
CNY	0.1405		1.0930	0.1196	0.1045	20.7554
HKD	0.1285	0.9149		0.1094	0.0956	18.9892
EUR	1.1747	8.3619	9.1397		0.8736	173.5546
GBP	1.3446	9.5717	10.4620	1.1447		198.6648
JPY	0.0068	0.0482	0.0527	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*