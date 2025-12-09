# 汇率数据自动更新（美元基准）

**更新时间**：2025-12-09 22:14:57（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.0628	7.7817	0.8595	0.7512	156.4080
CNY	0.1416		1.1018	0.1217	0.1064	22.1453
HKD	0.1285	0.9076		0.1105	0.0965	20.0995
EUR	1.1635	8.2173	9.0538		0.8740	181.9756
GBP	1.3312	9.4020	10.3590	1.1442		208.2109
JPY	0.0064	0.0452	0.0498	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*