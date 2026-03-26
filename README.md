# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-26 12:26:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9008	7.8190	0.8640	0.7482	159.3900
CNY	0.1449		1.1331	0.1252	0.1084	23.0973
HKD	0.1279	0.8826		0.1105	0.0957	20.3850
EUR	1.1574	7.9870	9.0498		0.8660	184.4792
GBP	1.3365	9.2232	10.4504	1.1548		213.0313
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