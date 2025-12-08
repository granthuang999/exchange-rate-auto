# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-08 11:15:13（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0689	7.7792	0.8579	0.7497	155.0160
CNY	0.1415		1.1005	0.1214	0.1061	21.9293
HKD	0.1285	0.9087		0.1103	0.0964	19.9270
EUR	1.1656	8.2398	9.0677		0.8739	180.6924
GBP	1.3339	9.4290	10.3764	1.1443		206.7707
JPY	0.0065	0.0456	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*