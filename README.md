# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-22 11:40:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9615	7.7961	0.8554	0.7446	158.4240
CNY	0.1436		1.1199	0.1229	0.1070	22.7572
HKD	0.1283	0.8929		0.1097	0.0955	20.3209
EUR	1.1690	8.1383	9.1140		0.8705	185.2046
GBP	1.3430	9.3493	10.4702	1.1488		212.7639
JPY	0.0063	0.0439	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*