# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-20 10:49:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7235	7.8420	0.8562	0.7350	158.4330
CNY	0.1487		1.1664	0.1273	0.1093	23.5641
HKD	0.1275	0.8574		0.1092	0.0937	20.2031
EUR	1.1680	7.8527	9.1591		0.8584	185.0420
GBP	1.3605	9.1476	10.6694	1.1649		215.5551
JPY	0.0063	0.0424	0.0495	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*