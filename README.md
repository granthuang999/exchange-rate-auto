# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-03 22:11:33（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1185	7.7812	0.8507	0.7423	147.3750
CNY	0.1405		1.0931	0.1195	0.1043	20.7031
HKD	0.1285	0.9148		0.1093	0.0954	18.9399
EUR	1.1755	8.3678	9.1468		0.8726	173.2397
GBP	1.3472	9.5898	10.4826	1.1460		198.5383
JPY	0.0068	0.0483	0.0528	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*