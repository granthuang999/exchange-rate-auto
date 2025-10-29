# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-29 11:09:32（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0997	7.7699	0.8585	0.7541	151.9710
CNY	0.1409		1.0944	0.1209	0.1062	21.4053
HKD	0.1287	0.9137		0.1105	0.0971	19.5589
EUR	1.1648	8.2699	9.0506		0.8784	177.0192
GBP	1.3261	9.4148	10.3035	1.1384		201.5263
JPY	0.0066	0.0467	0.0511	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*