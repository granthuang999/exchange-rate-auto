# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-05 10:54:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1345	7.7983	0.8567	0.7432	148.1700
CNY	0.1402		1.0930	0.1201	0.1042	20.7681
HKD	0.1282	0.9149		0.1099	0.0953	19.0003
EUR	1.1673	8.3279	9.1027		0.8675	172.9544
GBP	1.3455	9.5997	10.4929	1.1527		199.3676
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