# 汇率数据自动更新（美元基准）

**更新时间**：2026-09-02 01:30:39（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7088	7.8408	0.8623	0.7397	160.1610
CNY	0.1491		1.1687	0.1285	0.1103	23.8733
HKD	0.1275	0.8556		0.1100	0.0943	20.4266
EUR	1.1597	7.7801	9.0929		0.8578	185.7370
GBP	1.3519	9.0696	10.6000	1.1657		216.5216
JPY	0.0062	0.0419	0.0490	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*