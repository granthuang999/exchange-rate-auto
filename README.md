# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-01 12:41:07（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8851	7.8379	0.8646	0.7553	158.8690
CNY	0.1452		1.1384	0.1256	0.1097	23.0743
HKD	0.1276	0.8784		0.1103	0.0964	20.2693
EUR	1.1566	7.9633	9.0653		0.8736	183.7486
GBP	1.3240	9.1157	10.3772	1.1447		210.3389
JPY	0.0063	0.0433	0.0493	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*