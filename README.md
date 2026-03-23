# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-23 22:49:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8796	7.8332	0.8598	0.7433	158.4200
CNY	0.1454		1.1386	0.1250	0.1080	23.0275
HKD	0.1277	0.8783		0.1098	0.0949	20.2242
EUR	1.1631	8.0014	9.1105		0.8645	184.2522
GBP	1.3454	9.2555	10.5384	1.1567		213.1306
JPY	0.0063	0.0434	0.0494	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*