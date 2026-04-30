# 汇率数据自动更新（美元基准）

**更新时间**：2026-04-30 13:23:08（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8401	7.8354	0.8571	0.7427	160.5030
CNY	0.1462		1.1455	0.1253	0.1086	23.4650
HKD	0.1276	0.8730		0.1094	0.0948	20.4843
EUR	1.1667	7.9805	9.1418		0.8665	187.2629
GBP	1.3464	9.2098	10.5499	1.1540		216.1074
JPY	0.0062	0.0426	0.0488	0.0053	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*