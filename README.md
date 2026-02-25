# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-25 22:42:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8687	7.8199	0.8485	0.7400	156.5340
CNY	0.1456		1.1385	0.1235	0.1077	22.7895
HKD	0.1279	0.8784		0.1085	0.0946	20.0174
EUR	1.1786	8.0951	9.2161		0.8721	184.4832
GBP	1.3514	9.2820	10.5674	1.1466		211.5324
JPY	0.0064	0.0439	0.0500	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*