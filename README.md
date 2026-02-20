# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-20 22:34:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8150	0.8499	0.7421	155.4500
CNY	0.1449		1.1321	0.1231	0.1075	22.5185
HKD	0.1280	0.8833		0.1088	0.0950	19.8912
EUR	1.1766	8.1224	9.1952		0.8732	182.9039
GBP	1.3475	9.3023	10.5309	1.1453		209.4731
JPY	0.0064	0.0444	0.0503	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*