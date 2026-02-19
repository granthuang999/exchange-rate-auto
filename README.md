# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-19 22:41:28（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8143	0.8510	0.7438	155.1940
CNY	0.1448		1.1313	0.1232	0.1077	22.4675
HKD	0.1280	0.8840		0.1089	0.0952	19.8603
EUR	1.1751	8.1169	9.1825		0.8740	182.3666
GBP	1.3444	9.2868	10.5059	1.1441		208.6502
JPY	0.0064	0.0445	0.0504	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*