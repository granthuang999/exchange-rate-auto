# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-05 22:39:35（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8907	7.8195	0.8620	0.7495	157.6690
CNY	0.1451		1.1348	0.1251	0.1088	22.8814
HKD	0.1279	0.8812		0.1102	0.0959	20.1636
EUR	1.1601	7.9939	9.0713		0.8695	182.9107
GBP	1.3342	9.1937	10.4330	1.1501		210.3656
JPY	0.0063	0.0437	0.0496	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*