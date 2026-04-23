# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-23 12:44:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8310	7.8318	0.8545	0.7414	159.5470
CNY	0.1464		1.1465	0.1251	0.1085	23.3563
HKD	0.1277	0.8722		0.1091	0.0947	20.3717
EUR	1.1703	7.9941	9.1654		0.8676	186.7139
GBP	1.3488	9.2136	10.5635	1.1525		215.1969
JPY	0.0063	0.0428	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*