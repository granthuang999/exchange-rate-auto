# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-16 11:23:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9653	7.7979	0.8612	0.7472	158.2550
CNY	0.1436		1.1195	0.1236	0.1073	22.7205
HKD	0.1282	0.8932		0.1104	0.0958	20.2946
EUR	1.1612	8.0879	9.0547		0.8676	183.7610
GBP	1.3383	9.3219	10.4362	1.1526		211.7974
JPY	0.0063	0.0440	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*