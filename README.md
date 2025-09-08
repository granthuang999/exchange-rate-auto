# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-08 11:00:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1343	7.7941	0.8533	0.7404	148.0540
CNY	0.1402		1.0925	0.1196	0.1038	20.7524
HKD	0.1283	0.9153		0.1095	0.0950	18.9957
EUR	1.1719	8.3608	9.1341		0.8677	173.5076
GBP	1.3506	9.6357	10.5269	1.1525		199.9649
JPY	0.0068	0.0482	0.0526	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*