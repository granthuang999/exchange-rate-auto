# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-18 18:01:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1775	7.8214	0.8559	0.7385	147.3960
CNY	0.1393		1.0897	0.1192	0.1029	20.5358
HKD	0.1279	0.9177		0.1094	0.0944	18.8452
EUR	1.1684	8.3859	9.1382		0.8628	172.2117
GBP	1.3541	9.7190	10.5909	1.1590		199.5884
JPY	0.0068	0.0487	0.0531	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*