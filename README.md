# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-17 22:14:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0428	7.7798	0.8520	0.7485	155.4790
CNY	0.1420		1.1046	0.1210	0.1063	22.0763
HKD	0.1285	0.9053		0.1095	0.0962	19.9850
EUR	1.1737	8.2662	9.1312		0.8785	182.4871
GBP	1.3360	9.4092	10.3939	1.1383		207.7208
JPY	0.0064	0.0453	0.0500	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*