# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-04 10:50:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1426	7.8001	0.8579	0.7445	148.1520
CNY	0.1400		1.0921	0.1201	0.1042	20.7420
HKD	0.1282	0.9157		0.1100	0.0954	18.9936
EUR	1.1656	8.3257	9.0921		0.8678	172.6915
GBP	1.3432	9.5938	10.4770	1.1523		198.9953
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