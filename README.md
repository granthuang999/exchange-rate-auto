# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-05 22:37:43（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9371	7.8125	0.8462	0.7368	156.7790
CNY	0.1442		1.1262	0.1220	0.1062	22.6001
HKD	0.1280	0.8879		0.1083	0.0943	20.0677
EUR	1.1818	8.1979	9.2325		0.8707	185.2742
GBP	1.3572	9.4152	10.6033	1.1485		212.7837
JPY	0.0064	0.0442	0.0498	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*