# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-12 10:48:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1200	7.7822	0.8526	0.7376	147.4440
CNY	0.1404		1.0930	0.1197	0.1036	20.7084
HKD	0.1285	0.9149		0.1096	0.0948	18.9463
EUR	1.1729	8.3509	9.1276		0.8651	172.9346
GBP	1.3557	9.6529	10.5507	1.1559		199.8970
JPY	0.0068	0.0483	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*