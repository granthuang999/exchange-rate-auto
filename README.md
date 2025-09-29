# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-29 10:59:04（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1177	7.7801	0.8526	0.7446	148.9320
CNY	0.1405		1.0931	0.1198	0.1046	20.9242
HKD	0.1285	0.9149		0.1096	0.0957	19.1427
EUR	1.1729	8.3482	9.1251		0.8733	174.6798
GBP	1.3430	9.5591	10.4487	1.1450		200.0161
JPY	0.0067	0.0478	0.0522	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*