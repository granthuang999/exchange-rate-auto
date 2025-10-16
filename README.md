# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-16 10:58:18（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1221	7.7716	0.8568	0.7444	150.7380
CNY	0.1404		1.0912	0.1203	0.1045	21.1648
HKD	0.1287	0.9164		0.1102	0.0958	19.3960
EUR	1.1671	8.3124	9.0705		0.8688	175.9314
GBP	1.3434	9.5676	10.4401	1.1510		202.4960
JPY	0.0066	0.0472	0.0516	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*