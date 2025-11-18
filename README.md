# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-18 11:06:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1078	7.7757	0.8622	0.7601	155.1490
CNY	0.1407		1.0940	0.1213	0.1069	21.8280
HKD	0.1286	0.9141		0.1109	0.0978	19.9531
EUR	1.1598	8.2438	9.0184		0.8816	179.9455
GBP	1.3156	9.3511	10.2298	1.1343		204.1166
JPY	0.0064	0.0458	0.0501	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*