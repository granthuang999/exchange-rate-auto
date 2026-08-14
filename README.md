# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-14 22:43:58（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7304	7.8469	0.8633	0.7379	158.9920
CNY	0.1486		1.1659	0.1283	0.1096	23.6230
HKD	0.1274	0.8577		0.1100	0.0940	20.2618
EUR	1.1583	7.7961	9.0894		0.8547	184.1677
GBP	1.3552	9.1210	10.6341	1.1699		215.4655
JPY	0.0063	0.0423	0.0494	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*