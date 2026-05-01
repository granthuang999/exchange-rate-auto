# 汇率数据自动更新（美元基准）

**更新时间**：2026-05-01 13:35:14（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8268	7.8327	0.8525	0.7357	157.2640
CNY	0.1465		1.1473	0.1249	0.1078	23.0363
HKD	0.1277	0.8716		0.1088	0.0939	20.0779
EUR	1.1730	8.0080	9.1879		0.8630	184.4739
GBP	1.3592	9.2793	10.6466	1.1588		213.7610
JPY	0.0064	0.0434	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*