# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-24 22:10:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1306	7.7774	0.8519	0.7445	148.7440
CNY	0.1402		1.0907	0.1195	0.1044	20.8600
HKD	0.1286	0.9168		0.1095	0.0957	19.1252
EUR	1.1738	8.3702	9.1295		0.8739	174.6027
GBP	1.3432	9.5777	10.4465	1.1443		199.7905
JPY	0.0067	0.0479	0.0523	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*