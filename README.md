# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-20 12:07:26（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9032	7.8138	0.8501	0.7437	155.1040
CNY	0.1449		1.1319	0.1231	0.1077	22.4684
HKD	0.1280	0.8835		0.1088	0.0952	19.8500
EUR	1.1763	8.1205	9.1916		0.8748	182.4538
GBP	1.3446	9.2822	10.5067	1.1431		208.5572
JPY	0.0064	0.0445	0.0504	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*