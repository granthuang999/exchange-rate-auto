# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-20 12:06:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8943	7.8347	0.8650	0.7460	158.3910
CNY	0.1450		1.1364	0.1255	0.1082	22.9742
HKD	0.1276	0.8800		0.1104	0.0952	20.2166
EUR	1.1561	7.9703	9.0575		0.8624	183.1110
GBP	1.3405	9.2417	10.5023	1.1595		212.3204
JPY	0.0063	0.0435	0.0495	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*