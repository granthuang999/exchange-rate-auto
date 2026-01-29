# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-29 22:33:11（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9468	7.8044	0.8355	0.7231	153.1850
CNY	0.1440		1.1235	0.1203	0.1041	22.0512
HKD	0.1281	0.8901		0.1071	0.0927	19.6280
EUR	1.1969	8.3145	9.3410		0.8655	183.3453
GBP	1.3829	9.6070	10.7930	1.1554		211.8448
JPY	0.0065	0.0453	0.0509	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*