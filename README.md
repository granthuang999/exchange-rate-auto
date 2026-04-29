# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-29 13:19:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8353	7.8370	0.8543	0.7403	159.6700
CNY	0.1463		1.1465	0.1250	0.1083	23.3596
HKD	0.1276	0.8722		0.1090	0.0945	20.3739
EUR	1.1705	8.0011	9.1736		0.8666	186.9016
GBP	1.3508	9.2331	10.5862	1.1540		215.6828
JPY	0.0063	0.0428	0.0491	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*