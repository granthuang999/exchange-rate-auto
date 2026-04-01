# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-01 22:57:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8715	7.8379	0.8601	0.7501	158.5000
CNY	0.1455		1.1406	0.1252	0.1092	23.0663
HKD	0.1276	0.8767		0.1097	0.0957	20.2223
EUR	1.1627	7.9892	9.1128		0.8721	184.2809
GBP	1.3332	9.1608	10.4491	1.1466		211.3052
JPY	0.0063	0.0434	0.0495	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*