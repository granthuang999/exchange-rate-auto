# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-22 11:25:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0400	7.7808	0.8533	0.7465	157.4350
CNY	0.1420		1.1052	0.1212	0.1060	22.3629
HKD	0.1285	0.9048		0.1097	0.0959	20.2338
EUR	1.1719	8.2503	9.1185		0.8748	184.5013
GBP	1.3396	9.4307	10.4230	1.1431		210.8975
JPY	0.0064	0.0447	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*