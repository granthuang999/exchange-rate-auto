# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-16 22:53:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8950	7.8300	0.8704	0.7521	159.1740
CNY	0.1450		1.1356	0.1262	0.1091	23.0854
HKD	0.1277	0.8806		0.1112	0.0961	20.3287
EUR	1.1489	7.9216	8.9959		0.8641	182.8745
GBP	1.3296	9.1677	10.4108	1.1573		211.6394
JPY	0.0063	0.0433	0.0492	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*