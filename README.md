# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-31 15:55:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7190	7.8380	0.8617	0.7382	159.5780
CNY	0.1488		1.1665	0.1282	0.1099	23.7503
HKD	0.1276	0.8572		0.1099	0.0942	20.3595
EUR	1.1605	7.7974	9.0960		0.8567	185.1897
GBP	1.3546	9.1019	10.6177	1.1673		216.1718
JPY	0.0063	0.0421	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*