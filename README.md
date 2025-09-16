# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-16 22:12:47（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1140	7.7818	0.8446	0.7318	146.6570
CNY	0.1406		1.0939	0.1187	0.1029	20.6153
HKD	0.1285	0.9142		0.1085	0.0940	18.8462
EUR	1.1840	8.4229	9.2136		0.8664	173.6408
GBP	1.3665	9.7212	10.6338	1.1541		200.4058
JPY	0.0068	0.0485	0.0531	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*