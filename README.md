# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-10 10:56:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1247	7.7804	0.8642	0.7515	152.9260
CNY	0.1404		1.0920	0.1213	0.1055	21.4642
HKD	0.1285	0.9157		0.1111	0.0966	19.6553
EUR	1.1571	8.2443	9.0030		0.8696	176.9567
GBP	1.3307	9.4806	10.3532	1.1500		203.4943
JPY	0.0065	0.0466	0.0509	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*