# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-27 12:27:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9129	7.8302	0.8663	0.7496	159.5730
CNY	0.1447		1.1327	0.1253	0.1084	23.0834
HKD	0.1277	0.8829		0.1106	0.0957	20.3792
EUR	1.1543	7.9798	9.0387		0.8653	184.2006
GBP	1.3340	9.2221	10.4458	1.1557		212.8775
JPY	0.0063	0.0433	0.0491	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*