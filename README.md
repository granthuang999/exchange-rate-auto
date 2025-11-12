# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-12 11:06:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1191	7.7709	0.8635	0.7612	154.3590
CNY	0.1405		1.0916	0.1213	0.1069	21.6824
HKD	0.1287	0.9161		0.1111	0.0980	19.8637
EUR	1.1581	8.2445	8.9993		0.8815	178.7597
GBP	1.3137	9.3525	10.2087	1.1344		202.7838
JPY	0.0065	0.0461	0.0503	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*