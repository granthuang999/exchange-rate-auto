# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-25 10:50:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7234	7.8383	0.8572	0.7335	159.3260
CNY	0.1487		1.1658	0.1275	0.1091	23.6972
HKD	0.1276	0.8578		0.1094	0.0936	20.3266
EUR	1.1666	7.8434	9.1441		0.8557	185.8679
GBP	1.3633	9.1662	10.6862	1.1686		217.2134
JPY	0.0063	0.0422	0.0492	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*