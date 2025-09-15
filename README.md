# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-15 11:01:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1194	7.7750	0.8524	0.7374	147.5040
CNY	0.1405		1.0921	0.1197	0.1036	20.7186
HKD	0.1286	0.9157		0.1096	0.0948	18.9716
EUR	1.1732	8.3522	9.1213		0.8651	173.0455
GBP	1.3561	9.6547	10.5438	1.1560		200.0325
JPY	0.0068	0.0483	0.0527	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*