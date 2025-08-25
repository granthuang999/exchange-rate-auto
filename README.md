# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-25 11:09:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1608	7.8046	0.8542	0.7404	147.3290
CNY	0.1396		1.0899	0.1193	0.1034	20.5744
HKD	0.1281	0.9175		0.1094	0.0949	18.8772
EUR	1.1707	8.3830	9.1367		0.8668	172.4760
GBP	1.3506	9.6715	10.5411	1.1537		198.9857
JPY	0.0068	0.0486	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*