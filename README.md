# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-04 01:23:18（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7075	7.8400	0.8590	0.7382	155.4250
CNY	0.1491		1.1688	0.1281	0.1101	23.1718
HKD	0.1276	0.8555		0.1096	0.0942	19.8246
EUR	1.1641	7.8085	9.1269		0.8594	180.9371
GBP	1.3546	9.0863	10.6204	1.1636		210.5459
JPY	0.0064	0.0432	0.0504	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*