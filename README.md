# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-10 22:12:10（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1215	7.7810	0.8637	0.7528	152.6140
CNY	0.1404		1.0926	0.1213	0.1057	21.4300
HKD	0.1285	0.9152		0.1110	0.0967	19.6137
EUR	1.1578	8.2453	9.0089		0.8716	176.6979
GBP	1.3284	9.4600	10.3361	1.1473		202.7285
JPY	0.0066	0.0467	0.0510	0.0057	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*