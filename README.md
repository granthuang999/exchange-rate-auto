# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-10 22:12:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1183	7.7732	0.8643	0.7593	154.0450
CNY	0.1405		1.0920	0.1214	0.1067	21.6407
HKD	0.1286	0.9157		0.1112	0.0977	19.8174
EUR	1.1570	8.2359	8.9936		0.8785	178.2309
GBP	1.3170	9.3748	10.2373	1.1383		202.8777
JPY	0.0065	0.0462	0.0505	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*