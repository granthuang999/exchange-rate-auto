# 汇率数据自动更新（美元基准）

**更新时间**：2026-07-24 23:20:22（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7616	7.8418	0.8787	0.7503	163.7670
CNY	0.1479		1.1598	0.1300	0.1110	24.2202
HKD	0.1275	0.8623		0.1121	0.0957	20.8839
EUR	1.1380	7.6950	8.9243		0.8539	186.3742
GBP	1.3328	9.0119	10.4516	1.1711		218.2687
JPY	0.0061	0.0413	0.0479	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*