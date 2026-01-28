# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-28 11:28:41（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9445	7.8012	0.8329	0.7241	152.6560
CNY	0.1440		1.1234	0.1199	0.1043	21.9823
HKD	0.1282	0.8902		0.1068	0.0928	19.5683
EUR	1.2006	8.3377	9.3663		0.8694	183.2825
GBP	1.3810	9.5905	10.7737	1.1503		210.8217
JPY	0.0066	0.0455	0.0511	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*