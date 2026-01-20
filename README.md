# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-20 22:22:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9595	7.7975	0.8522	0.7436	157.7860
CNY	0.1437		1.1204	0.1225	0.1068	22.6720
HKD	0.1282	0.8925		0.1093	0.0954	20.2355
EUR	1.1734	8.1665	9.1498		0.8726	185.1514
GBP	1.3448	9.3592	10.4861	1.1460		212.1920
JPY	0.0063	0.0441	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*