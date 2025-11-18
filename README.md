# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-18 22:12:55（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1076	7.7840	0.8620	0.7603	155.2120
CNY	0.1407		1.0952	0.1213	0.1070	21.8375
HKD	0.1285	0.9131		0.1107	0.0977	19.9399
EUR	1.1601	8.2455	9.0302		0.8820	180.0603
GBP	1.3153	9.3484	10.2381	1.1338		204.1457
JPY	0.0064	0.0458	0.0502	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*