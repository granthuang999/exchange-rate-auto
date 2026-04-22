# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-22 23:04:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8261	7.8327	0.8532	0.7409	159.4100
CNY	0.1465		1.1475	0.1250	0.1085	23.3530
HKD	0.1277	0.8715		0.1089	0.0946	20.3519
EUR	1.1721	8.0006	9.1804		0.8684	186.8378
GBP	1.3497	9.2133	10.5719	1.1516		215.1572
JPY	0.0063	0.0428	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*