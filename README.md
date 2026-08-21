# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-21 10:54:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7213	7.8418	0.8546	0.7324	158.9280
CNY	0.1488		1.1667	0.1271	0.1090	23.6454
HKD	0.1275	0.8571		0.1090	0.0934	20.2668
EUR	1.1701	7.8648	9.1760		0.8570	185.9677
GBP	1.3654	9.1771	10.7070	1.1668		216.9962
JPY	0.0063	0.0423	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*