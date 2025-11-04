# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-04 11:04:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1235	7.7731	0.8685	0.7618	154.1390
CNY	0.1404		1.0912	0.1219	0.1069	21.6381
HKD	0.1286	0.9164		0.1117	0.0980	19.8298
EUR	1.1514	8.2021	8.9500		0.8771	177.4773
GBP	1.3127	9.3509	10.2036	1.1401		202.3353
JPY	0.0065	0.0462	0.0504	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*