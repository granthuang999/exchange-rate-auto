# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-25 22:12:41（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0054	7.7744	0.8484	0.7395	155.9990
CNY	0.1427		1.1098	0.1211	0.1056	22.2684
HKD	0.1286	0.9011		0.1091	0.0951	20.0657
EUR	1.1787	8.2572	9.1636		0.8716	183.8744
GBP	1.3523	9.4732	10.5130	1.1473		210.9520
JPY	0.0064	0.0449	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*