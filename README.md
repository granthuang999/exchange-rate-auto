# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-04 00:14:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7456	7.8417	0.8687	0.7445	156.9010
CNY	0.1482		1.1625	0.1288	0.1104	23.2598
HKD	0.1275	0.8602		0.1108	0.0949	20.0085
EUR	1.1511	7.7652	9.0269		0.8570	180.6159
GBP	1.3432	9.0606	10.5328	1.1668		210.7468
JPY	0.0064	0.0430	0.0500	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*