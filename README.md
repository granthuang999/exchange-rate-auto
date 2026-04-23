# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-23 23:44:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8255	7.8320	0.8541	0.7409	159.4170
CNY	0.1465		1.1475	0.1251	0.1085	23.3561
HKD	0.1277	0.8715		0.1091	0.0946	20.3546
EUR	1.1708	7.9915	9.1699		0.8675	186.6491
GBP	1.3497	9.2124	10.5709	1.1528		215.1667
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