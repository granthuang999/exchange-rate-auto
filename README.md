# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-08 02:30:08（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7103	7.8393	0.8601	0.7385	154.3480
CNY	0.1490		1.1682	0.1282	0.1101	23.0017
HKD	0.1276	0.8560		0.1097	0.0942	19.6890
EUR	1.1627	7.8018	9.1144		0.8586	179.4536
GBP	1.3541	9.0864	10.6152	1.1647		209.0020
JPY	0.0065	0.0435	0.0508	0.0056	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*