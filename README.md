# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-30 22:12:16（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1103	7.7688	0.8631	0.7593	154.1000
CNY	0.1406		1.0926	0.1214	0.1068	21.6728
HKD	0.1287	0.9152		0.1111	0.0977	19.8358
EUR	1.1586	8.2381	9.0010		0.8797	178.5425
GBP	1.3170	9.3643	10.2315	1.1367		202.9501
JPY	0.0065	0.0461	0.0504	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*