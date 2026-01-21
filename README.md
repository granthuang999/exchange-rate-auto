# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-21 11:26:54（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9644	7.7967	0.8534	0.7443	158.0920
CNY	0.1436		1.1195	0.1225	0.1069	22.7000
HKD	0.1283	0.8932		0.1095	0.0955	20.2768
EUR	1.1718	8.1608	9.1360		0.8722	185.2496
GBP	1.3435	9.3570	10.4752	1.1466		212.4036
JPY	0.0063	0.0441	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*