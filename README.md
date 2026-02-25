# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-25 12:12:03（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8713	7.8219	0.8480	0.7400	155.9510
CNY	0.1455		1.1383	0.1234	0.1077	22.6960
HKD	0.1278	0.8785		0.1084	0.0946	19.9377
EUR	1.1792	8.1029	9.2239		0.8726	183.9045
GBP	1.3514	9.2855	10.5701	1.1459		210.7446
JPY	0.0064	0.0441	0.0502	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*