# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-03 11:11:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1159	7.7713	0.8669	0.7611	154.0600
CNY	0.1405		1.0921	0.1218	0.1070	21.6501
HKD	0.1287	0.9157		0.1116	0.0979	19.8242
EUR	1.1535	8.2084	8.9645		0.8780	177.7137
GBP	1.3139	9.3495	10.2106	1.1390		202.4176
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