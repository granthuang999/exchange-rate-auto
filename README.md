# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-07 22:12:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1204	7.7765	0.8640	0.7612	153.3690
CNY	0.1404		1.0921	0.1213	0.1069	21.5394
HKD	0.1286	0.9156		0.1111	0.0979	19.7221
EUR	1.1574	8.2412	9.0006		0.8810	177.5104
GBP	1.3137	9.3542	10.2161	1.1350		201.4832
JPY	0.0065	0.0464	0.0507	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*