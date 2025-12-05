# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-05 11:12:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0693	7.7825	0.8581	0.7502	155.0570
CNY	0.1415		1.1009	0.1214	0.1061	21.9339
HKD	0.1285	0.9084		0.1103	0.0964	19.9238
EUR	1.1654	8.2383	9.0695		0.8743	180.6981
GBP	1.3330	9.4232	10.3739	1.1438		206.6875
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