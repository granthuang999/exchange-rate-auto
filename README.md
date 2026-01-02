# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-02 11:23:52（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9926	7.7897	0.8500	0.7415	156.7030
CNY	0.1430		1.1140	0.1216	0.1060	22.4098
HKD	0.1284	0.8977		0.1091	0.0952	20.1167
EUR	1.1765	8.2266	9.1644		0.8724	184.3565
GBP	1.3486	9.4303	10.5053	1.1463		211.3324
JPY	0.0064	0.0446	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*