# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-11 11:26:18（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7434	7.8455	0.8661	0.7402	159.1830
CNY	0.1483		1.1634	0.1284	0.1098	23.6057
HKD	0.1275	0.8595		0.1104	0.0943	20.2897
EUR	1.1546	7.7859	9.0584		0.8546	183.7929
GBP	1.3510	9.1102	10.5992	1.1701		215.0540
JPY	0.0063	0.0424	0.0493	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*