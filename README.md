# 汇率数据自动更新（美元基准）

**更新时间**：2025-08-18 22:14:03（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1829	7.8188	0.8561	0.7388	147.7670
CNY	0.1392		1.0885	0.1192	0.1029	20.5721
HKD	0.1279	0.9187		0.1095	0.0945	18.8989
EUR	1.1681	8.3903	9.1330		0.8630	172.6048
GBP	1.3535	9.7224	10.5831	1.1588		200.0095
JPY	0.0068	0.0486	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*