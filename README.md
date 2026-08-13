# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-13 22:50:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7313	7.8473	0.8664	0.7408	159.1790
CNY	0.1486		1.1658	0.1287	0.1101	23.6476
HKD	0.1274	0.8578		0.1104	0.0944	20.2846
EUR	1.1542	7.7693	9.0574		0.8550	183.7246
GBP	1.3499	9.0865	10.5930	1.1695		214.8745
JPY	0.0063	0.0423	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*