# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-19 22:41:29（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.8993	7.8318	0.8681	0.7486	158.2730
CNY	0.1449		1.1352	0.1258	0.1085	22.9404
HKD	0.1277	0.8809		0.1108	0.0956	20.2090
EUR	1.1519	7.9476	9.0218		0.8623	182.3212
GBP	1.3358	9.2163	10.4619	1.1596		211.4253
JPY	0.0063	0.0436	0.0495	0.0055	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*