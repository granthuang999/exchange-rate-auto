# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-03 14:41:07（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7173	7.8411	0.8613	0.7412	157.2340
CNY	0.1489		1.1673	0.1282	0.1103	23.4073
HKD	0.1275	0.8567		0.1098	0.0945	20.0525
EUR	1.1610	7.7990	9.1038		0.8606	182.5543
GBP	1.3492	9.0627	10.5789	1.1620		212.1344
JPY	0.0064	0.0427	0.0499	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*