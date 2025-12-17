# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-17 11:13:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0435	7.7781	0.8517	0.7458	154.9360
CNY	0.1420		1.1043	0.1209	0.1059	21.9970
HKD	0.1286	0.9056		0.1095	0.0959	19.9195
EUR	1.1741	8.2699	9.1324		0.8757	181.9138
GBP	1.3408	9.4442	10.4292	1.1420		207.7447
JPY	0.0065	0.0455	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*