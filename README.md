# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-29 22:12:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1189	7.7808	0.8515	0.7444	148.5770
CNY	0.1405		1.0930	0.1196	0.1046	20.8708
HKD	0.1285	0.9149		0.1094	0.0957	19.0953
EUR	1.1744	8.3604	9.1378		0.8742	174.4885
GBP	1.3434	9.5633	10.4524	1.1439		199.5930
JPY	0.0067	0.0479	0.0524	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*