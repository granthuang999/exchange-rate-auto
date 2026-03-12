# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-12 22:41:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8684	7.8268	0.8679	0.7488	159.1610
CNY	0.1456		1.1395	0.1264	0.1090	23.1729
HKD	0.1278	0.8775		0.1109	0.0957	20.3354
EUR	1.1522	7.9138	9.0181		0.8628	183.3863
GBP	1.3355	9.1725	10.4525	1.1591		212.5548
JPY	0.0063	0.0432	0.0492	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*