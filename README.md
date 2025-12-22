# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-22 22:14:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0362	7.7792	0.8508	0.7442	157.1320
CNY	0.1421		1.1056	0.1209	0.1058	22.3319
HKD	0.1285	0.9045		0.1094	0.0957	20.1990
EUR	1.1754	8.2701	9.1434		0.8747	184.6874
GBP	1.3437	9.4547	10.4531	1.1432		211.1422
JPY	0.0064	0.0448	0.0495	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*