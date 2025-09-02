# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-02 11:01:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1440	7.7987	0.8545	0.7391	147.6430
CNY	0.1400		1.0916	0.1196	0.1035	20.6667
HKD	0.1282	0.9161		0.1096	0.0948	18.9317
EUR	1.1703	8.3604	9.1266		0.8650	172.7829
GBP	1.3530	9.6658	10.5516	1.1561		199.7605
JPY	0.0068	0.0484	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*