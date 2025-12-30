# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-30 22:13:51（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9921	7.7827	0.8502	0.7418	156.1680
CNY	0.1430		1.1131	0.1216	0.1061	22.3349
HKD	0.1285	0.8984		0.1092	0.0953	20.0660
EUR	1.1762	8.2241	9.1540		0.8725	183.6838
GBP	1.3481	9.4259	10.4916	1.1461		210.5257
JPY	0.0064	0.0448	0.0498	0.0054	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*