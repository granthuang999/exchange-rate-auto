# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-21 22:12:32（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1080	7.7847	0.8684	0.7647	156.8380
CNY	0.1407		1.0952	0.1222	0.1076	22.0650
HKD	0.1285	0.9131		0.1116	0.0982	20.1470
EUR	1.1515	8.1852	8.9644		0.8806	180.6057
GBP	1.3077	9.2951	10.1801	1.1356		205.0974
JPY	0.0064	0.0453	0.0496	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*