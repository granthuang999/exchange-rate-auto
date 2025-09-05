# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-05 22:11:09（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1329	7.7982	0.8512	0.7382	147.0960
CNY	0.1402		1.0933	0.1193	0.1035	20.6222
HKD	0.1282	0.9147		0.1092	0.0947	18.8628
EUR	1.1748	8.3798	9.1614		0.8672	172.8102
GBP	1.3546	9.6626	10.5638	1.1531		199.2631
JPY	0.0068	0.0485	0.0530	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*