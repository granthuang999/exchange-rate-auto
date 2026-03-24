# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-24 12:10:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8928	7.8350	0.8633	0.7465	158.7200
CNY	0.1451		1.1367	0.1252	0.1083	23.0269
HKD	0.1276	0.8797		0.1102	0.0953	20.2578
EUR	1.1583	7.9842	9.0756		0.8647	183.8527
GBP	1.3396	9.2335	10.4956	1.1565		212.6189
JPY	0.0063	0.0434	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*