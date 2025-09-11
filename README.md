# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-11 10:55:22（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1208	7.7884	0.8546	0.7393	147.4600
CNY	0.1404		1.0938	0.1200	0.1038	20.7083
HKD	0.1284	0.9143		0.1097	0.0949	18.9333
EUR	1.1701	8.3323	9.1135		0.8651	172.5486
GBP	1.3526	9.6318	10.5348	1.1560		199.4589
JPY	0.0068	0.0483	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*