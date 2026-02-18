# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-18 12:12:56（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8152	0.8443	0.7379	153.5900
CNY	0.1449		1.1321	0.1223	0.1069	22.2491
HKD	0.1280	0.8833		0.1080	0.0944	19.6527
EUR	1.1844	8.1762	9.2564		0.8740	181.9140
GBP	1.3552	9.3552	10.5911	1.1442		208.1447
JPY	0.0065	0.0449	0.0509	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*