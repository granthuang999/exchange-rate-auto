# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-19 12:11:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8144	0.8481	0.7414	155.2000
CNY	0.1448		1.1313	0.1228	0.1073	22.4683
HKD	0.1280	0.8839		0.1085	0.0949	19.8608
EUR	1.1791	8.1447	9.2140		0.8742	182.9973
GBP	1.3488	9.3168	10.5401	1.1439		209.3337
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