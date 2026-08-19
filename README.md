# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-19 10:49:18（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7411	7.8424	0.8629	0.7385	159.3090
CNY	0.1483		1.1634	0.1280	0.1096	23.6325
HKD	0.1275	0.8596		0.1100	0.0942	20.3138
EUR	1.1589	7.8121	9.0884		0.8558	184.6205
GBP	1.3541	9.1281	10.6194	1.1684		215.7197
JPY	0.0063	0.0423	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*