# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-13 22:18:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9743	7.8020	0.8570	0.7426	158.9110
CNY	0.1434		1.1187	0.1229	0.1065	22.7852
HKD	0.1282	0.8939		0.1098	0.0952	20.3680
EUR	1.1669	8.1380	9.1039		0.8665	185.4271
GBP	1.3466	9.3917	10.5063	1.1541		213.9927
JPY	0.0063	0.0439	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*