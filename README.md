# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-22 22:11:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1787	7.8156	0.8554	0.7411	147.2970
CNY	0.1393		1.0887	0.1192	0.1032	20.5186
HKD	0.1279	0.9185		0.1094	0.0948	18.8465
EUR	1.1690	8.3922	9.1368		0.8664	172.1966
GBP	1.3493	9.6865	10.5459	1.1542		198.7546
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