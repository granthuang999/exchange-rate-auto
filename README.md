# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-18 11:14:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0419	7.7799	0.8515	0.7480	155.7320
CNY	0.1420		1.1048	0.1209	0.1062	22.1151
HKD	0.1285	0.9051		0.1094	0.0961	20.0172
EUR	1.1744	8.2700	9.1367		0.8784	182.8914
GBP	1.3369	9.4143	10.4009	1.1384		208.1979
JPY	0.0064	0.0452	0.0500	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*