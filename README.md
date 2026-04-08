# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-08 12:29:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8297	7.8324	0.8561	0.7457	158.4080
CNY	0.1464		1.1468	0.1253	0.1092	23.1940
HKD	0.1277	0.8720		0.1093	0.0952	20.2247
EUR	1.1681	7.9777	9.1489		0.8710	185.0345
GBP	1.3410	9.1588	10.5034	1.1480		212.4286
JPY	0.0063	0.0431	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*