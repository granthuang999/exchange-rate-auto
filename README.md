# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-26 22:41:15（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8404	7.8227	0.8467	0.7383	156.0950
CNY	0.1462		1.1436	0.1238	0.1079	22.8196
HKD	0.1278	0.8744		0.1082	0.0944	19.9541
EUR	1.1811	8.0789	9.2390		0.8720	184.3569
GBP	1.3545	9.2651	10.5956	1.1468		211.4249
JPY	0.0064	0.0438	0.0501	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*