# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-17 22:48:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8167	7.8293	0.8456	0.7366	157.6850
CNY	0.1467		1.1485	0.1240	0.1081	23.1322
HKD	0.1277	0.8707		0.1080	0.0941	20.1404
EUR	1.1826	8.0614	9.2589		0.8711	186.4771
GBP	1.3576	9.2543	10.6290	1.1480		214.0714
JPY	0.0063	0.0432	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*