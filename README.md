# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-31 12:29:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9084	7.8381	0.8714	0.7574	159.6200
CNY	0.1448		1.1346	0.1261	0.1096	23.1052
HKD	0.1276	0.8814		0.1112	0.0966	20.3646
EUR	1.1476	7.9279	8.9948		0.8692	183.1765
GBP	1.3203	9.1212	10.3487	1.1505		210.7473
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