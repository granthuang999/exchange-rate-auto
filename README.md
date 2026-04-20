# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-20 12:52:07（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8184	7.8328	0.8501	0.7404	158.9220
CNY	0.1467		1.1488	0.1247	0.1086	23.3078
HKD	0.1277	0.8705		0.1085	0.0945	20.2893
EUR	1.1763	8.0207	9.2140		0.8710	186.9451
GBP	1.3506	9.2091	10.5791	1.1482		214.6434
JPY	0.0063	0.0429	0.0493	0.0053	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*