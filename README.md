# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-27 13:40:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7678	7.8421	0.8766	0.7488	163.5670
CNY	0.1478		1.1587	0.1295	0.1106	24.1684
HKD	0.1275	0.8630		0.1118	0.0955	20.8576
EUR	1.1408	7.7205	8.9460		0.8542	186.5925
GBP	1.3355	9.0382	10.4729	1.1707		218.4388
JPY	0.0061	0.0414	0.0479	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*