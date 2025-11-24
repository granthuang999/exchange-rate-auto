# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-24 11:17:22（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1071	7.7824	0.8682	0.7637	156.6600
CNY	0.1407		1.0950	0.1222	0.1075	22.0427
HKD	0.1285	0.9132		0.1116	0.0981	20.1300
EUR	1.1518	8.1860	8.9638		0.8796	180.4423
GBP	1.3094	9.3061	10.1904	1.1368		205.1329
JPY	0.0064	0.0454	0.0497	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*