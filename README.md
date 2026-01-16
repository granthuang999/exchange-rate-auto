# 汇率数据自动更新（美元基准）

**更新时间**：2026-01-16 22:16:24（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9681	7.7997	0.8607	0.7460	158.0780
CNY	0.1435		1.1193	0.1235	0.1071	22.6860
HKD	0.1282	0.8934		0.1104	0.0956	20.2672
EUR	1.1618	8.0959	9.0620		0.8667	183.6621
GBP	1.3405	9.3406	10.4554	1.1538		211.9008
JPY	0.0063	0.0441	0.0493	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*