# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-02 12:22:36（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8852	7.8370	0.8665	0.7555	159.3760
CNY	0.1452		1.1382	0.1258	0.1097	23.1476
HKD	0.1276	0.8786		0.1106	0.0964	20.3364
EUR	1.1541	7.9460	9.0444		0.8719	183.9308
GBP	1.3236	9.1134	10.3733	1.1469		210.9543
JPY	0.0063	0.0432	0.0492	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*