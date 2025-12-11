# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-11 11:18:19（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0607	7.7794	0.8549	0.7479	155.6820
CNY	0.1416		1.1018	0.1211	0.1059	22.0491
HKD	0.1285	0.9076		0.1099	0.0961	20.0121
EUR	1.1697	8.2591	9.0998		0.8748	182.1055
GBP	1.3371	9.4407	10.4017	1.1431		208.1588
JPY	0.0064	0.0454	0.0500	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*