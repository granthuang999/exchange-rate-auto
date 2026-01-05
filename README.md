# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-05 22:17:23（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9843	7.7850	0.8560	0.7431	156.7430
CNY	0.1432		1.1146	0.1226	0.1064	22.4422
HKD	0.1285	0.8971		0.1100	0.0955	20.1340
EUR	1.1682	8.1592	9.0946		0.8681	183.1110
GBP	1.3457	9.3989	10.4764	1.1519		210.9312
JPY	0.0064	0.0446	0.0497	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*