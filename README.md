# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-12 11:16:49（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0547	7.7831	0.8518	0.7467	155.6940
CNY	0.1417		1.1033	0.1207	0.1058	22.0695
HKD	0.1285	0.9064		0.1094	0.0959	20.0041
EUR	1.1740	8.2821	9.1372		0.8766	182.7823
GBP	1.3392	9.4478	10.4233	1.1408		208.5094
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