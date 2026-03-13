# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-13 12:04:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8838	7.8281	0.8686	0.7493	159.3530
CNY	0.1453		1.1372	0.1262	0.1088	23.1490
HKD	0.1277	0.8794		0.1110	0.0957	20.3565
EUR	1.1513	7.9252	9.0123		0.8627	183.4596
GBP	1.3346	9.1870	10.4472	1.1592		212.6692
JPY	0.0063	0.0432	0.0491	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*