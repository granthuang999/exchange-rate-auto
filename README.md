# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-17 22:49:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8858	7.8370	0.8666	0.7488	158.8680
CNY	0.1452		1.1381	0.1259	0.1087	23.0718
HKD	0.1276	0.8786		0.1106	0.0955	20.2715
EUR	1.1539	7.9458	9.0434		0.8641	183.3233
GBP	1.3355	9.1958	10.4661	1.1573		212.1635
JPY	0.0063	0.0433	0.0493	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*