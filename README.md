# 汇率数据自动更新（美元基准）

**更新时间**：2026-02-23 22:40:44（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9075	7.8183	0.8474	0.7400	154.6340
CNY	0.1448		1.1319	0.1227	0.1071	22.3864
HKD	0.1279	0.8835		0.1084	0.0946	19.7785
EUR	1.1801	8.1514	9.2262		0.8733	182.4805
GBP	1.3514	9.3345	10.5653	1.1451		208.9649
JPY	0.0065	0.0447	0.0506	0.0055	0.0048	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*