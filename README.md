# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-01 03:45:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7192	7.8380	0.8607	0.7381	159.7840
CNY	0.1488		1.1665	0.1281	0.1098	23.7802
HKD	0.1276	0.8573		0.1098	0.0942	20.3858
EUR	1.1618	7.8067	9.1065		0.8576	185.6442
GBP	1.3548	9.1034	10.6192	1.1661		216.4802
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