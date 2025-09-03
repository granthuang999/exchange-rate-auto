# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-03 22:12:38（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1420	7.7999	0.8568	0.7442	148.2170
CNY	0.1400		1.0921	0.1200	0.1042	20.7529
HKD	0.1282	0.9157		0.1098	0.0954	19.0024
EUR	1.1671	8.3357	9.1035		0.8686	172.9890
GBP	1.3437	9.5969	10.4809	1.1513		199.1629
JPY	0.0067	0.0482	0.0526	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*