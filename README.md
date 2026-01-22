# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-22 22:22:47（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9725	7.7974	0.8534	0.7446	158.6800
CNY	0.1434		1.1183	0.1224	0.1068	22.7580
HKD	0.1282	0.8942		0.1094	0.0955	20.3504
EUR	1.1718	8.1703	9.1369		0.8725	185.9386
GBP	1.3430	9.3641	10.4719	1.1461		213.1077
JPY	0.0063	0.0439	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*