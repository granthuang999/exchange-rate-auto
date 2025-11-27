# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-27 11:05:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0794	7.7772	0.8614	0.7546	156.1180
CNY	0.1413		1.0986	0.1217	0.1066	22.0524
HKD	0.1286	0.9103		0.1108	0.0970	20.0738
EUR	1.1609	8.2185	9.0286		0.8760	181.2375
GBP	1.3252	9.3817	10.3064	1.1415		206.8884
JPY	0.0064	0.0453	0.0498	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*