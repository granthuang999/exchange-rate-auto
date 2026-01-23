# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-23 22:18:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9637	7.7975	0.8517	0.7392	158.2530
CNY	0.1436		1.1197	0.1223	0.1062	22.7254
HKD	0.1282	0.8931		0.1092	0.0948	20.2954
EUR	1.1741	8.1762	9.1552		0.8679	185.8084
GBP	1.3528	9.4206	10.5486	1.1522		214.0869
JPY	0.0063	0.0440	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*