# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-30 22:56:18（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9119	7.8359	0.8718	0.7575	159.5200
CNY	0.1447		1.1337	0.1261	0.1096	23.0790
HKD	0.1276	0.8821		0.1113	0.0967	20.3576
EUR	1.1471	7.9283	8.9882		0.8689	182.9777
GBP	1.3201	9.1246	10.3444	1.1509		210.5875
JPY	0.0063	0.0433	0.0491	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*