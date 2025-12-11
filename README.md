# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-11 22:16:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0576	7.7814	0.8515	0.7452	155.1270
CNY	0.1417		1.1026	0.1207	0.1056	21.9801
HKD	0.1285	0.9070		0.1094	0.0958	19.9356
EUR	1.1744	8.2884	9.1385		0.8752	182.1809
GBP	1.3419	9.4707	10.4420	1.1426		208.1683
JPY	0.0064	0.0455	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*