# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-10 10:50:06（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1262	7.7881	0.8540	0.7390	147.2990
CNY	0.1403		1.0929	0.1198	0.1037	20.6701
HKD	0.1284	0.9150		0.1097	0.0949	18.9133
EUR	1.1710	8.3445	9.1196		0.8653	172.4813
GBP	1.3532	9.6430	10.5387	1.1556		199.3221
JPY	0.0068	0.0484	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*