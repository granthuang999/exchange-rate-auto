# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-04 12:04:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9367	7.8142	0.8453	0.7297	156.3270
CNY	0.1442		1.1265	0.1219	0.1052	22.5362
HKD	0.1280	0.8877		0.1082	0.0934	20.0055
EUR	1.1830	8.2062	9.2443		0.8632	184.9367
GBP	1.3704	9.5062	10.7088	1.1584		214.2346
JPY	0.0064	0.0444	0.0500	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*