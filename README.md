# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-19 10:56:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1136	7.7761	0.8487	0.7385	147.9720
CNY	0.1406		1.0931	0.1193	0.1038	20.8013
HKD	0.1286	0.9148		0.1091	0.0950	19.0291
EUR	1.1783	8.3818	9.1624		0.8702	174.3514
GBP	1.3541	9.6325	10.5296	1.1492		200.3683
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