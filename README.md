# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-26 12:08:08（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8360	7.8207	0.8460	0.7376	155.9260
CNY	0.1463		1.1440	0.1238	0.1079	22.8095
HKD	0.1279	0.8741		0.1082	0.0943	19.9376
EUR	1.1820	8.0804	9.2443		0.8719	184.3097
GBP	1.3557	9.2679	10.6029	1.1470		211.3964
JPY	0.0064	0.0438	0.0502	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*