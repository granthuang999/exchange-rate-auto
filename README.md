# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-13 22:36:05（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8168	0.8423	0.7333	152.9470
CNY	0.1448		1.1316	0.1219	0.1062	22.1422
HKD	0.1279	0.8837		0.1078	0.0938	19.5664
EUR	1.1872	8.2008	9.2803		0.8706	181.5826
GBP	1.3637	9.4197	10.6598	1.1486		208.5736
JPY	0.0065	0.0452	0.0511	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*