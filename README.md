# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-31 11:20:42（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9880	7.7825	0.8515	0.7429	156.4720
CNY	0.1431		1.1137	0.1219	0.1063	22.3915
HKD	0.1285	0.8979		0.1094	0.0955	20.1056
EUR	1.1744	8.2067	9.1398		0.8725	183.7604
GBP	1.3461	9.4064	10.4758	1.1462		210.6232
JPY	0.0064	0.0447	0.0497	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*