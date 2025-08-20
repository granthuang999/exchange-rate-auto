# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-20 22:12:50（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1748	7.8140	0.8575	0.7423	147.1960
CNY	0.1394		1.0891	0.1195	0.1035	20.5157
HKD	0.1280	0.9182		0.1097	0.0950	18.8375
EUR	1.1662	8.3671	9.1125		0.8657	171.6571
GBP	1.3472	9.6656	10.5267	1.1552		198.2972
JPY	0.0068	0.0487	0.0531	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*