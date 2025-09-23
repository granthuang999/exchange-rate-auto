# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-23 10:52:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1126	7.7709	0.8469	0.7402	147.7620
CNY	0.1406		1.0926	0.1191	0.1041	20.7747
HKD	0.1287	0.9153		0.1090	0.0953	19.0148
EUR	1.1808	8.3984	9.1757		0.8740	174.4740
GBP	1.3510	9.6090	10.4984	1.1442		199.6244
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