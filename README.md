# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-29 00:08:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8369	7.8358	0.8533	0.7400	159.5010
CNY	0.1463		1.1461	0.1248	0.1082	23.3294
HKD	0.1276	0.8725		0.1089	0.0944	20.3554
EUR	1.1719	8.0123	9.1829		0.8672	186.9225
GBP	1.3514	9.2391	10.5889	1.1531		215.5419
JPY	0.0063	0.0429	0.0491	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*