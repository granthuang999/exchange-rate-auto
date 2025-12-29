# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-29 22:14:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0054	7.7725	0.8493	0.7409	156.1910
CNY	0.1427		1.1095	0.1212	0.1058	22.2958
HKD	0.1287	0.9013		0.1093	0.0953	20.0953
EUR	1.1774	8.2484	9.1517		0.8724	183.9056
GBP	1.3497	9.4553	10.4906	1.1463		210.8125
JPY	0.0064	0.0449	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*