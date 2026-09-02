# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-03 01:30:41（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7072	7.8414	0.8628	0.7413	158.9350
CNY	0.1491		1.1691	0.1286	0.1105	23.6962
HKD	0.1275	0.8554		0.1100	0.0945	20.2687
EUR	1.1590	7.7738	9.0883		0.8592	184.2084
GBP	1.3490	9.0479	10.5779	1.1639		214.4004
JPY	0.0063	0.0422	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*