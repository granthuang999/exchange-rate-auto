# 汇率数据自动更新（美元基准）

**更新时间**：2026-08-19 22:23:34（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.7186	7.8399	0.8570	0.7344	158.3510
CNY	0.1488		1.1669	0.1276	0.1093	23.5690
HKD	0.1276	0.8570		0.1093	0.0937	20.1981
EUR	1.1669	7.8397	9.1481		0.8569	184.7736
GBP	1.3617	9.1484	10.6752	1.1669		215.6196
JPY	0.0063	0.0424	0.0495	0.0054	0.0046	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*