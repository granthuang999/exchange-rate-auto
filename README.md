# 汇率数据自动更新（美元基准）

**更新时间**：2025-10-28 11:01:53（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1014	7.7684	0.8576	0.7489	152.4120
CNY	0.1408		1.0939	0.1208	0.1055	21.4622
HKD	0.1287	0.9141		0.1104	0.0964	19.6195
EUR	1.1660	8.2806	9.0583		0.8733	177.7192
GBP	1.3353	9.4824	10.3731	1.1451		203.5145
JPY	0.0066	0.0466	0.0510	0.0056	0.0049	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*