# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-27 12:05:21（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8542	7.8240	0.8469	0.7411	155.7530
CNY	0.1459		1.1415	0.1236	0.1081	22.7237
HKD	0.1278	0.8760		0.1082	0.0947	19.9071
EUR	1.1808	8.0933	9.2384		0.8751	183.9096
GBP	1.3493	9.2487	10.5573	1.1428		210.1646
JPY	0.0064	0.0440	0.0502	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*