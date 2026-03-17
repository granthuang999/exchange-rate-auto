# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-17 12:09:46（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8832	7.8344	0.8701	0.7519	159.3500
CNY	0.1453		1.1382	0.1264	0.1092	23.1506
HKD	0.1276	0.8786		0.1111	0.0960	20.3398
EUR	1.1493	7.9108	9.0040		0.8642	183.1399
GBP	1.3300	9.1544	10.4195	1.1572		211.9298
JPY	0.0063	0.0432	0.0492	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*