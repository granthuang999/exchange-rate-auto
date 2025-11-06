# 汇率数据自动更新（美元基准）

**更新时间**：2025-11-06 11:07:47（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1232	7.7746	0.8690	0.7657	153.9480
CNY	0.1404		1.0914	0.1220	0.1075	21.6122
HKD	0.1286	0.9162		0.1118	0.0985	19.8014
EUR	1.1507	8.1970	8.9466		0.8811	177.1554
GBP	1.3060	9.3029	10.1536	1.1349		201.0552
JPY	0.0065	0.0463	0.0505	0.0056	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*