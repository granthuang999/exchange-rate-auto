# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-27 22:43:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9117	7.8332	0.8671	0.7513	159.8980
CNY	0.1447		1.1333	0.1255	0.1087	23.1344
HKD	0.1277	0.8824		0.1107	0.0959	20.4129
EUR	1.1533	7.9711	9.0338		0.8665	184.4055
GBP	1.3310	9.1997	10.4262	1.1541		212.8284
JPY	0.0063	0.0432	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*