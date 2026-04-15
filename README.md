# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-15 12:39:28（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8164	7.8373	0.8481	0.7371	158.9820
CNY	0.1467		1.1498	0.1244	0.1081	23.3235
HKD	0.1276	0.8697		0.1082	0.0941	20.2853
EUR	1.1791	8.0373	9.2410		0.8691	187.4567
GBP	1.3567	9.2476	10.6326	1.1506		215.6858
JPY	0.0063	0.0429	0.0493	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*