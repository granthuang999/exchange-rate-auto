# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-10 11:15:59（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0616	7.7810	0.8600	0.7517	156.6540
CNY	0.1416		1.1019	0.1218	0.1064	22.1839
HKD	0.1285	0.9075		0.1105	0.0966	20.1329
EUR	1.1628	8.2112	9.0477		0.8741	182.1558
GBP	1.3303	9.3942	10.3512	1.1441		208.3996
JPY	0.0064	0.0451	0.0497	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*