# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-09 12:18:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9328	7.8138	0.8455	0.7350	156.7510
CNY	0.1442		1.1271	0.1220	0.1060	22.6101
HKD	0.1280	0.8873		0.1082	0.0941	20.0608
EUR	1.1827	8.1996	9.2416		0.8693	185.3944
GBP	1.3605	9.4324	10.6310	1.1503		213.2667
JPY	0.0064	0.0442	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*