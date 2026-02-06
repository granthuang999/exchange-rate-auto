# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-06 12:06:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9390	7.8111	0.8480	0.7381	156.7160
CNY	0.1441		1.1257	0.1222	0.1064	22.5848
HKD	0.1280	0.8884		0.1086	0.0945	20.0632
EUR	1.1792	8.1828	9.2112		0.8704	184.8066
GBP	1.3548	9.4012	10.5827	1.1489		212.3235
JPY	0.0064	0.0443	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*