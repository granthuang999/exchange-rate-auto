# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-03 10:51:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7808	0.8526	0.7441	147.6450
CNY	0.1405		1.0930	0.1198	0.1045	20.7410
HKD	0.1285	0.9149		0.1096	0.0956	18.9756
EUR	1.1729	8.3492	9.1260		0.8727	173.1703
GBP	1.3439	9.5666	10.4567	1.1458		198.4209
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