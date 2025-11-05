# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-05 11:05:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1270	7.7747	0.8699	0.7681	153.3230
CNY	0.1403		1.0909	0.1221	0.1078	21.5130
HKD	0.1286	0.9167		0.1119	0.0988	19.7208
EUR	1.1496	8.1929	8.9375		0.8830	176.2536
GBP	1.3019	9.2787	10.1220	1.1325		199.6133
JPY	0.0065	0.0465	0.0507	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*