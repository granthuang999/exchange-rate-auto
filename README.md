# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-05 01:16:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7001	7.8407	0.8606	0.7398	156.0940
CNY	0.1493		1.1702	0.1284	0.1104	23.2973
HKD	0.1275	0.8545		0.1098	0.0944	19.9082
EUR	1.1620	7.7854	9.1107		0.8596	181.3781
GBP	1.3517	9.0566	10.5984	1.1633		210.9949
JPY	0.0064	0.0429	0.0502	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*