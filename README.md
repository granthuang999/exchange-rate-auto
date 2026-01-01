# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-01 22:12:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9875	7.7827	0.8511	0.7422	156.7460
CNY	0.1431		1.1138	0.1218	0.1062	22.4323
HKD	0.1285	0.8978		0.1094	0.0954	20.1403
EUR	1.1750	8.2100	9.1443		0.8720	184.1687
GBP	1.3473	9.4146	10.4860	1.1467		211.1911
JPY	0.0064	0.0446	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*