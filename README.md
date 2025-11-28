# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-28 22:12:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0743	7.7827	0.8633	0.7559	156.0260
CNY	0.1414		1.1001	0.1220	0.1069	22.0553
HKD	0.1285	0.9090		0.1109	0.0971	20.0478
EUR	1.1583	8.1945	9.0151		0.8756	180.7321
GBP	1.3229	9.3588	10.2959	1.1421		206.4109
JPY	0.0064	0.0453	0.0499	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*