# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-15 10:59:31（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1253	7.7755	0.8600	0.7490	151.0510
CNY	0.1403		1.0913	0.1207	0.1051	21.1992
HKD	0.1286	0.9164		0.1106	0.0963	19.4265
EUR	1.1628	8.2852	9.0413		0.8709	175.6407
GBP	1.3351	9.5131	10.3812	1.1482		201.6702
JPY	0.0066	0.0472	0.0515	0.0057	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*