# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-09 22:10:20（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1204	7.7869	0.8519	0.7385	146.9970
CNY	0.1404		1.0936	0.1196	0.1037	20.6445
HKD	0.1284	0.9144		0.1094	0.0948	18.8775
EUR	1.1738	8.3583	9.1406		0.8669	172.5519
GBP	1.3541	9.6417	10.5442	1.1536		199.0481
JPY	0.0068	0.0484	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*