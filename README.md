# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-19 22:12:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1156	7.7744	0.8500	0.7412	147.8840
CNY	0.1405		1.0926	0.1195	0.1042	20.7831
HKD	0.1286	0.9153		0.1093	0.0953	19.0219
EUR	1.1765	8.3713	9.1464		0.8720	173.9812
GBP	1.3492	9.6001	10.4889	1.1468		199.5197
JPY	0.0068	0.0481	0.0526	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*