# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-04 12:00:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9160	7.8137	0.8611	0.7496	157.3770
CNY	0.1446		1.1298	0.1245	0.1084	22.7555
HKD	0.1280	0.8851		0.1102	0.0959	20.1412
EUR	1.1613	8.0316	9.0741		0.8705	182.7627
GBP	1.3340	9.2263	10.4238	1.1487		209.9480
JPY	0.0064	0.0439	0.0496	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*