# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-13 23:08:37（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8298	7.8327	0.8539	0.7431	159.6170
CNY	0.1464		1.1468	0.1250	0.1088	23.3707
HKD	0.1277	0.8720		0.1090	0.0949	20.3783
EUR	1.1711	7.9984	9.1729		0.8702	186.9270
GBP	1.3457	9.1910	10.5406	1.1491		214.7988
JPY	0.0063	0.0428	0.0491	0.0053	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*