# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-08 22:18:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9821	7.7919	0.8574	0.7452	157.0470
CNY	0.1432		1.1160	0.1228	0.1067	22.4928
HKD	0.1283	0.8961		0.1100	0.0956	20.1552
EUR	1.1663	8.1433	9.0878		0.8691	183.1666
GBP	1.3419	9.3694	10.4561	1.1506		210.7448
JPY	0.0064	0.0445	0.0496	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*