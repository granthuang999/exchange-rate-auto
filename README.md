# 汇率数据自动更新（美元基准）

**更新时间**：2025-09-10 22:11:12（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		7.1206	7.7899	0.8524	0.7374	147.2940
CNY	0.1404		1.0940	0.1197	0.1036	20.6856
HKD	0.1284	0.9141		0.1094	0.0947	18.9083
EUR	1.1732	8.3536	9.1388		0.8651	172.7992
GBP	1.3561	9.6564	10.5640	1.1560		199.7478
JPY	0.0068	0.0483	0.0529	0.0058	0.0050	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*