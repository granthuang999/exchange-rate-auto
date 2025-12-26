# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-26 11:18:21（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0066	7.7741	0.8478	0.7400	156.2320
CNY	0.1427		1.1095	0.1210	0.1056	22.2978
HKD	0.1286	0.9013		0.1091	0.0952	20.0965
EUR	1.1795	8.2644	9.1697		0.8728	184.2793
GBP	1.3514	9.4684	10.5055	1.1457		211.1243
JPY	0.0064	0.0448	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*