# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-11 22:40:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8650	7.8257	0.8627	0.7448	158.6110
CNY	0.1457		1.1399	0.1257	0.1085	23.1043
HKD	0.1278	0.8772		0.1102	0.0952	20.2680
EUR	1.1592	7.9576	9.0712		0.8633	183.8542
GBP	1.3426	9.2172	10.5071	1.1583		212.9578
JPY	0.0063	0.0433	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*