# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-04 22:36:32（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9410	7.8118	0.8467	0.7303	156.5310
CNY	0.1441		1.1255	0.1220	0.1052	22.5516
HKD	0.1280	0.8885		0.1084	0.0935	20.0378
EUR	1.1811	8.1977	9.2262		0.8625	184.8719
GBP	1.3693	9.5043	10.6967	1.1594		214.3379
JPY	0.0064	0.0443	0.0499	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*