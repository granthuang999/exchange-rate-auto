# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-24 22:12:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1230	7.7695	0.8597	0.7501	152.7730
CNY	0.1404		1.0908	0.1207	0.1053	21.4478
HKD	0.1287	0.9168		0.1107	0.0965	19.6632
EUR	1.1632	8.2854	9.0375		0.8725	177.7050
GBP	1.3332	9.4961	10.3580	1.1461		203.6702
JPY	0.0065	0.0466	0.0509	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*