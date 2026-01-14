# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-14 22:18:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9737	7.7965	0.8578	0.7433	158.3390
CNY	0.1434		1.1180	0.1230	0.1066	22.7052
HKD	0.1283	0.8945		0.1100	0.0953	20.3090
EUR	1.1658	8.1298	9.0889		0.8665	184.5873
GBP	1.3454	9.3821	10.4890	1.1540		213.0217
JPY	0.0063	0.0440	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*