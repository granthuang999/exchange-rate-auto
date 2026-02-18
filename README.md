# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-18 22:38:40（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8143	0.8459	0.7387	154.3460
CNY	0.1448		1.1313	0.1225	0.1069	22.3447
HKD	0.1280	0.8840		0.1083	0.0945	19.7517
EUR	1.1822	8.1659	9.2379		0.8733	182.4636
GBP	1.3537	9.3509	10.5784	1.1451		208.9427
JPY	0.0065	0.0448	0.0506	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*