# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-12 12:15:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9008	7.8168	0.8423	0.7337	152.5290
CNY	0.1449		1.1327	0.1221	0.1063	22.1031
HKD	0.1279	0.8828		0.1078	0.0939	19.5130
EUR	1.1872	8.1928	9.2803		0.8711	181.0863
GBP	1.3630	9.4055	10.6539	1.1480		207.8901
JPY	0.0066	0.0452	0.0512	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*