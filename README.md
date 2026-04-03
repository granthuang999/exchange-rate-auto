# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-03 12:23:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8803	7.8380	0.8666	0.7559	159.5460
CNY	0.1453		1.1392	0.1260	0.1099	23.1888
HKD	0.1276	0.8778		0.1106	0.0964	20.3554
EUR	1.1539	7.9394	9.0445		0.8723	184.1057
GBP	1.3229	9.1021	10.3691	1.1464		211.0676
JPY	0.0063	0.0431	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*