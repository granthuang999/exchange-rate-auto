# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-10 22:52:01（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9106	7.8172	0.8392	0.7312	154.3930
CNY	0.1447		1.1312	0.1214	0.1058	22.3415
HKD	0.1279	0.8840		0.1074	0.0935	19.7504
EUR	1.1916	8.2347	9.3151		0.8713	183.9764
GBP	1.3676	9.4510	10.6909	1.1477		211.1502
JPY	0.0065	0.0448	0.0506	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*