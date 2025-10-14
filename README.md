# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-14 22:13:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1387	7.7749	0.8637	0.7525	151.9420
CNY	0.1401		1.0891	0.1210	0.1054	21.2843
HKD	0.1286	0.9182		0.1111	0.0968	19.5426
EUR	1.1578	8.2653	9.0019		0.8713	175.9199
GBP	1.3289	9.4866	10.3321	1.1478		201.9163
JPY	0.0066	0.0470	0.0512	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*