# 汇率数据自动更新（美元基准）

**更新时间**：2026-03-30 12:38:27（北京时间）

## Excel 表格（制表符分隔）

Currency	USD	CNY	HKD	EUR	GBP	JPY
USD		6.9070	7.8326	0.8679	0.7534	159.7530
CNY	0.1448		1.1340	0.1257	0.1091	23.1291
HKD	0.1277	0.8818		0.1108	0.0962	20.3959
EUR	1.1522	7.9583	9.0248		0.8681	184.0684
GBP	1.3273	9.1678	10.3963	1.1520		212.0427
JPY	0.0063	0.0432	0.0490	0.0054	0.0047	

## CSV 文件链接

https://raw.githubusercontent.com/granthuang999/exchange-rate-auto/main/exchange_rates.csv

### 数据源说明
- 优先使用 Yahoo Finance 实时汇率
- Yahoo 失败时使用 Wise 汇率
- 最后备选 ExchangeRate-API
- 以美元为基准计算所有交叉汇率

---
*数据仅供参考，交易请以银行报价为准*