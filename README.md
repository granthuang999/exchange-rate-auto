# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-23 11:26:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9628	7.7973	0.8512	0.7413	158.7050
CNY	0.1436		1.1199	0.1222	0.1065	22.7933
HKD	0.1282	0.8930		0.1092	0.0951	20.3538
EUR	1.1748	8.1800	9.1604		0.8709	186.4485
GBP	1.3490	9.3927	10.5184	1.1483		214.0901
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