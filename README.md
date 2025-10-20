# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-20 11:09:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1248	7.7666	0.8569	0.7442	150.8760
CNY	0.1404		1.0901	0.1203	0.1045	21.1762
HKD	0.1288	0.9174		0.1103	0.0958	19.4263
EUR	1.1670	8.3146	9.0636		0.8685	176.0719
GBP	1.3437	9.5738	10.4362	1.1514		202.7358
JPY	0.0066	0.0472	0.0515	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*