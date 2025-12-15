# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-15 22:17:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0465	7.7818	0.8510	0.7470	155.1520
CNY	0.1419		1.1043	0.1208	0.1060	22.0183
HKD	0.1285	0.9055		0.1094	0.0960	19.9378
EUR	1.1751	8.2803	9.1443		0.8778	182.3173
GBP	1.3387	9.4331	10.4174	1.1392		207.7001
JPY	0.0064	0.0454	0.0502	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*