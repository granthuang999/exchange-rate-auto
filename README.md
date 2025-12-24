# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-24 22:12:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0134	7.7757	0.8483	0.7404	156.0250
CNY	0.1426		1.1087	0.1210	0.1056	22.2467
HKD	0.1286	0.9020		0.1091	0.0952	20.0657
EUR	1.1788	8.2676	9.1662		0.8728	183.9267
GBP	1.3506	9.4724	10.5020	1.1457		210.7307
JPY	0.0064	0.0450	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*