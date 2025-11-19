# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-19 22:12:26（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1089	7.7871	0.8644	0.7626	156.3460
CNY	0.1407		1.0954	0.1216	0.1073	21.9930
HKD	0.1284	0.9129		0.1110	0.0979	20.0776
EUR	1.1569	8.2241	9.0087		0.8822	180.8723
GBP	1.3113	9.3219	10.2113	1.1335		205.0170
JPY	0.0064	0.0455	0.0498	0.0055	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*