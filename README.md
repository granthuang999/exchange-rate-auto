# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-29 11:41:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0088	7.7739	0.8490	0.7403	156.3810
CNY	0.1427		1.1092	0.1211	0.1056	22.3121
HKD	0.1286	0.9016		0.1092	0.0952	20.1162
EUR	1.1779	8.2554	9.1565		0.8720	184.1943
GBP	1.3508	9.4675	10.5010	1.1468		211.2400
JPY	0.0064	0.0448	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*