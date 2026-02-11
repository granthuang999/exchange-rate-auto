# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-11 22:47:00（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9117	7.8167	0.8429	0.7322	153.5890
CNY	0.1447		1.1309	0.1220	0.1059	22.2216
HKD	0.1279	0.8842		0.1078	0.0937	19.6488
EUR	1.1864	8.1999	9.2736		0.8687	182.2150
GBP	1.3657	9.4396	10.6756	1.1512		209.7637
JPY	0.0065	0.0450	0.0509	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*