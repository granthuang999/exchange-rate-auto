# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-27 22:13:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0813	7.7777	0.8623	0.7553	156.2880
CNY	0.1412		1.0983	0.1218	0.1067	22.0705
HKD	0.1286	0.9105		0.1109	0.0971	20.0944
EUR	1.1597	8.2121	9.0197		0.8759	181.2455
GBP	1.3240	9.3755	10.2975	1.1417		206.9218
JPY	0.0064	0.0453	0.0498	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*